#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>
int lock = 1;
void createChild(int child[], int index, int times) {
	if (times == 0) exit(0);
	for (int i = 0; i < child[index]; i++) {
		// child
		if (fork() == 0) {
			if (i == 0) {
				createChild(child, index + 1, times - 1);
				wait(NULL);
			}
			printf("I'm %d, my parent is %d\n", getpid(), getppid());
			exit(0);
		} else {
			wait(NULL);
		}
	}
}
int main(int argc, char *argv[]) {
	
	if (argc == 1) {
		printf("I'm %d, my parent is %d\n", getpid(), getppid());
		return 0;
	}
	// printf("argc:%d\n", argc);
	int child[argc];
	for (int i = 1; i < argc; i++) {
		child[i - 1] = atoi(argv[i]);
	}
	child[argc - 1] = 0;
	createChild(child, 0, argc);
	printf("I'm %d, my parent is %d\n", getpid(), getppid());

	return 0;
}
