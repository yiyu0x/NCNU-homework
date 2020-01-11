#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <stdbool.h>
extern char ** environ;
static char ** env = NULL; 
void showEnv() {
	for (int i = 0; environ[i] != NULL; i++)
		printf("%s\n", environ[i]);
}
void sys(char **argv, int start, int end) {
	char cmd[100] = "";
	strcat(cmd, argv[start]);
	for (int i = start + 1; i < end; i++) {
		strcat(cmd, " ");
		strcat(cmd, argv[i]);
	}
	// printf("cmd: %s\n", cmd);
	system(cmd);
}
void clear() {
	for (int i = 0; environ[i] != NULL; i++)
		environ[i] = NULL;
}
void updateenv(char *s) {
	int key_pos = 0;
	char *tmp = s;
	while (*tmp) {
		key_pos++;
		if (*tmp == '=') break;
		tmp++;
	}
	int counter = 0;
	for (int i = 0; environ[i] != NULL; i++) {
		if (strncmp(environ[i], s, key_pos) == 0) {
			environ[i] = s;
			return;
		}
		counter++;
	}
	environ[counter++] = s;
	environ[counter] = NULL;
	return;

}
int main(int argc, char **argv, char **envp) {

	if (argc == 1) {
		showEnv();
	}
	else if (argc >= 2) {
		// if argv[1] equal "-i", just clear env
		int i = 1;
		if (!strcmp(argv[1], "-i")) {
			//---C LIB clearenv();
			clear();
			i = 2;
			// if argv only has -i (ex. ./a.out -i)
			if (argc == 2) return 0;
		}
		bool isCmd = false;
		for (; i < argc; i++) {
		// handle each string is a key, value pair or not,
		// if not, put it into system func.
			if (strstr(argv[i], "=") && !isCmd) {
				//---putenv(argv[i]);
				updateenv(argv[i]);
			} else {
				isCmd = true;
				sys(argv, i, argc);
				exit(0);
			}
		}
		showEnv();
	}
	return 0;
}