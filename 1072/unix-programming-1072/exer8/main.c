#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <poll.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>

ssize_t r_read(int fd, void *buf, size_t size) {
   ssize_t retval;

   while (retval = read(fd, buf, size), retval == -1 && errno == EINTR) ;
   return retval;
}    

int main(int argc, char *argv[]) {
	
	int mode = 1;
	int i;
	
	int fd_p[2];
	int fd_p_s[2];
	int fd_anti_cw_s[2];
	
	if (pipe(fd_p_s) == -1) return -1;
	if (pipe(fd_anti_cw_s) == -1) return -1;
	pid_t childpid;
	int root = 0;
	int size = atoi(argv[1]);
	int fd_anti_cw[size*2];

	int fd[2];
    struct pollfd *pollfd;
    int numnow = 0;
    int numfds = 3;

	if ((pollfd = (void *)calloc(numfds, sizeof(struct pollfd))) == NULL)
		return 0;

	pollfd->fd = STDIN_FILENO;
	pollfd->events = POLLRDNORM;

	int id = 0;
	for (i = 0; i < size - 1; i++) {
		id = i;
		if (pipe(fd_anti_cw+2*id) == -1) return -1;
		if (pipe(fd_p) == -1) return -1;
		//parent
		if ((childpid = fork()) > 0) {
			// first process
			if (i == 0) {
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
				fd_anti_cw[id*2] = -1;
				fd_anti_cw[id*2+1] = -1;
			}
		}
		close(fd_p[0]);
		close(fd_p[1]);

		//make chain
		if (childpid > 0) break;
	}

	(pollfd+1)->fd = fd_anti_cw_s[0];
	(pollfd+1)->events = POLLRDNORM;
	(pollfd+2)->fd = fd_anti_cw[id*2];
	(pollfd+2)->events = POLLRDNORM;

	int bytesAonce = 3;
	while (1) {
		if (root == 1) {
			char mode;
			read(STDIN_FILENO, &mode, 1);
			if (mode == 'f') {
				write(STDOUT_FILENO, "0", bytesAonce);
				write(STDOUT_FILENO, "1", bytesAonce);
				char str[5];
				int bytes;
				while ((bytes = read(fd_p_s[0], str, bytesAonce)) <= 0);
				int num1 = atoi(str);
				while ((bytes = read(fd_p_s[0], str, bytesAonce)) <= 0);
				int num2 = atoi(str);
				fprintf(stderr, "I am  root. I got %2d %2d\n", num1, num2);
			} else if (mode == 'p') {
				char ack;
				write(fd_anti_cw_s[1], "*", 1);
				while ((read(fd_anti_cw[id*2], &ack, 1) <= 0));//root
				if (ack == '*')
					fprintf(stderr, "I'am %d, the root\n", getpid());
			} else if (mode == 'q') {
				return 0;
			}
		} else {
			char str[5];
			while (1) {        /* Continue monitoring until descriptors done */
      			int numready = poll(pollfd, numfds, -1); 
      			for (i = 0; i < numfds && numready > 0; i++)  {
         			if ((pollfd + i)->revents) {
            			if ((pollfd + i)->revents & (POLLRDNORM | POLLIN) ) {
           					if (i == 0) {
           						char str[5];
								int bytes;
								while ((bytes = read(STDIN_FILENO, str, bytesAonce)) <= 0);
								int num1 = atoi(str);
								while ((bytes = read(STDIN_FILENO, str, bytesAonce)) <= 0);
								int num2 = atoi(str);
								fprintf(stderr, "I am  %d, I got %2d %2d\n", getpid(), num1, num2);
								int tmp = num1;
								num1 = num2;
								num2 += tmp;
								sprintf(str, "%d", num1);
								write(STDOUT_FILENO, str, bytesAonce);
								sprintf(str, "%d", num2);
								write(STDOUT_FILENO, str, bytesAonce);
           					} else {
								char ack;
								int bytes;
								if (fd_anti_cw[id*2+1] == -1) {
									while ((bytes = read(fd_anti_cw_s[0], &ack, 1)) <= 0);	
								} else {
									while ((bytes = read(fd_anti_cw[id*2], &ack, 1)) <= 0);				
								}
								if (ack == '*') {
									fprintf(stderr, "I'am %d\n", getpid());
									write(fd_anti_cw[(id-1)*2+1], "*", 1);
								}
           					}
               			}
               		}
               	}
      		}
		}
	}
}
