#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <poll.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>
#include <signal.h>
#define PID_LEN 6
int fd_p_s[2];
void sig_handler(int signal) {
	char str[PID_LEN];
	sprintf(str, "%d", getpid());
    if (signal == SIGUSR1) {
    	int bytesAonce = 3;
	    write(STDOUT_FILENO, "f", 1);
		write(STDOUT_FILENO, str, PID_LEN);
		write(STDOUT_FILENO, "0", bytesAonce);
		write(STDOUT_FILENO, "1", bytesAonce);
    } else if (signal == SIGUSR2) {
    	write(STDOUT_FILENO, "p", 1);
    	write(STDOUT_FILENO, str, PID_LEN);
    } else if (signal == SIGINT) {
    	write(STDOUT_FILENO, "q", 1);
    	write(STDOUT_FILENO, str, PID_LEN);
    }

}


int main(int argc, char *argv[]) {
		


	// int mode = 1;
	int i;
	int fd_p[2];
	
	if (pipe(fd_p_s) == -1) return -1;
	pid_t childpid;
	int root = 0;
	int size = atoi(argv[1]);
	int id = 0;
	for (i = 0; i < size - 1; i++) {
		id = i;
		if (pipe(fd_p) == -1) return -1;
		//parent
		if ((childpid = fork()) > 0) {
			// first process
			if (i == 0) {
				dup2(fd_p_s[0], STDIN_FILENO);
				root = 1;	
			}
			dup2(fd_p[1], STDOUT_FILENO);
		}
		else {
			dup2(fd_p[0], STDIN_FILENO);
			//last process
			if (i == size - 2) {
				dup2(fd_p_s[1], STDOUT_FILENO);
				id = size - 1;
			}
		}
		close(fd_p[0]);
		close(fd_p[1]);

		//make chain
		if (childpid > 0) break;
	}


	fprintf(stderr, "I am %d\n", getpid());

	struct sigaction new_act;
    sigemptyset( &new_act.sa_mask );
    new_act.sa_handler = sig_handler;
    new_act.sa_flags = 0;
    sigaction( SIGINT, &new_act, 0 );
    sigaction( SIGUSR1, &new_act, 0 );
    sigaction( SIGUSR2, &new_act, 0 );

    //Add SIGINT, SIGUSR1/SIGUSR2 signals to the signal-set of new_set.
    sigset_t new_set, old_set;
    sigemptyset( &new_set );
    sigaddset( &new_set, SIGINT ); 
    sigaddset( &new_set, SIGUSR1 ); 
    sigaddset( &new_set, SIGUSR2 ); 

    

	int bytesAonce = 3;
	while (1) {

		int bytes;
		char str[5];
		char header[PID_LEN];
		char mode[1];

		while ((bytes = read(STDIN_FILENO, mode, 1)) <= 0);
		if (mode[0] == 'f') {
			while ((bytes = read(STDIN_FILENO, header, PID_LEN)) <= 0);
			int pid = atoi(header);
			// fprintf(stderr, "im child %d, i receive header is : %d\n", getpid(), pid);
			// if (pid == getpid()) break;
			while ((bytes = read(STDIN_FILENO, str, bytesAonce)) <= 0);
			int num1 = atoi(str);
			while ((bytes = read(STDIN_FILENO, str, bytesAonce)) <= 0);
			int num2 = atoi(str);
			fprintf(stderr, "I am %d, I got %2d %2d\n", getpid(), num1, num2);
			if (pid == getpid()) {
				continue;
			}
			int tmp = num1;
			num1 = num2;
			num2 += tmp;
			write(STDOUT_FILENO, "f", 1);
			write(STDOUT_FILENO, header, PID_LEN);
			sprintf(str, "%d", num1);
			write(STDOUT_FILENO, str, bytesAonce);
			sprintf(str, "%d", num2);
			write(STDOUT_FILENO, str, bytesAonce);
		} else if (mode[0] == 'p') {
			char header[PID_LEN];
			while ((bytes = read(STDIN_FILENO, header, PID_LEN)) <= 0);
			int pid = atoi(header);
			fprintf(stderr, "I am %d\n", getpid());
			if (pid == getpid()) {
				continue;
			}
			write(STDOUT_FILENO, "p", 1);
			write(STDOUT_FILENO, header, PID_LEN);
		} else if (mode[0] == 'q') {
			while ((bytes = read(STDIN_FILENO, header, PID_LEN)) <= 0);
			int pid = atoi(header);
			if (pid == getpid()) {
				exit(0);
			}
			write(STDOUT_FILENO, "q", 1);
			write(STDOUT_FILENO, header, PID_LEN);
			exit(0);
		}
	}
}