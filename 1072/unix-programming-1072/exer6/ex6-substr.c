#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#define BLKSIZE 1024
char* replace(char* str, char* old, char* new) {

    int newLen = strlen(new);
    int oldLen = strlen(old);
    int len = strlen(str);
    int counter = 0;
    int i;
    for (i = 0; i < len; i++) {
        if (strstr(str, old) == &str[i]) {
            counter += newLen - oldLen;
        }
    }
    char *newStr = (char*)malloc(len + counter + 1);
    i = 0;
    while (*str) {
        if (strstr(str, old) == str) {
            strcpy(&newStr[i], new);
            i += newLen;
            str += oldLen;
        } else {
            newStr[i++] = *str++;
        }
    }
    newStr[i] = '\0';
    return newStr;
}
int main(int argc, char *argv[]) {

    char buff[BLKSIZE];
    char* result = NULL;
    // two args, so read from stdin
	if (argc == 3) {
        int bytes = read(0, buff, BLKSIZE);
        buff[bytes - 1] = '\n';
        buff[bytes] = '\0';
        result = replace(buff, argv[1], argv[2]);
        write(1, result, strlen(result));
    // with files name, so read from files
    } else if (argc > 3) {
        int fd;
        for (int i = 3; i < argc; i++) {
            char* file = argv[i];
            fd = open(argv[i], O_RDONLY);
            int bytes = read(fd, buff, BLKSIZE);
            result = replace(buff, argv[1], argv[2]);
            write(1, result, strlen(result));
        }
    }
}