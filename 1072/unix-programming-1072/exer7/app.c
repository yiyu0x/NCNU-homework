#include <stdio.h>
#include <string.h>
#include <sys/wait.h>
#include <sys/types.h>
#include <errno.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int get_treesize(char *s) {
    int i, level;

    for(level=0, i=0; s[i]; i++){
        if(s[i] == 'd') level += 1;
        if(s[i] == 'u') level -= 1;
        if(level == 0) return i+1;
    }

    return i;
}

int main(int argc, char *argv[]) {

    char label, *labels, *t_begin, *t_end;
    int  j, status;
    pid_t childpid;
    int amountOfChilds;
    int num = strlen(argv[2]);
    int fd[2], fd2[2];
    int parent[2];
    // create two dimensional array
    int **childs = malloc(2 * sizeof(int *));
    for (int i = 0; i < 2; i++)
        childs[i] = (int *)malloc(sizeof(int) * num);

    t_begin = argv[1]; 
    t_end   = t_begin + strlen(t_begin) - 1;
    labels  = argv[2];
newborn:
    label = *labels;  
    labels += 1;
    t_begin = t_begin + 1;
    while(t_begin < t_end) {
        
        if (pipe(fd) < 0) perror("pipe 1 error");
        if (pipe(fd2) < 0) perror("pipe 2 error");

        j = get_treesize(t_begin);
        if((childpid = fork()) == 0){
            t_end  = t_begin + j - 1;
            parent[0] = fd[0];
            parent[1] = fd2[1];
            amountOfChilds = 0;
            goto newborn;
        } else {
            t_begin += j;
            labels  += j/2;
            childs[amountOfChilds][0] = fd[1];
            childs[amountOfChilds][1] = fd2[0];
            amountOfChilds++;
        }
    }

    fprintf(stderr, "I'm %c, my pid=%ld, and my ppid=%ld\n",
            label, getpid(), getppid());


    char ch[2];
    int nbytes = 0;
    while (1) {
        // root
        if (label == argv[2][0]) {
            read(STDIN_FILENO, ch, 2);
        } else {
            read(parent[0], ch, 2);
            // printf("debug: im %c, i got %c, i have %d childs \n", label, ch[0], amountOfChilds);
        }
        if (ch[0] == label) ch[0] = 'X';
        char ack[4];
        for(int i = 0; i < amountOfChilds; i++) {
            write(childs[i][0], ch, 2);
            // printf("debug: im %c, im waiting for childs\n", label);
            int bytes = read(childs[i][1], ack, 3);
            // printf("debug: %c: send '%c' to channel %d\n", label, ch[0], childs[i][0]);
        }
        // break;
        if (ch[0] == 'X')
            fprintf(stderr, "I'm %c, my pid=%ld, and my ppid=%ld\n",
                                            label, getpid(), getppid());
        if (label != argv[2][0]) {
            // printf("im %c my parent number is %d\n", label, parent[1]);
            int bytes = write(parent[1], "ACK", 3);
            // printf("im %c, i write %d bytes\n", label, bytes);
        }
        if (ch[0] == 'q') break;
    }

}
