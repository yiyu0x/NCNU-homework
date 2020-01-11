#include <stdio.h>
#include <string.h>
#include <sys/wait.h>
#include <errno.h>

pid_t r_wait(int *stat_loc) {
   int retval;

   while (((retval = wait(stat_loc)) == -1) && (errno == EINTR)) ;
   return retval;
}

int get_treesize(char *s) {
    int i, level;

    for(level=0, i=0; s[i]; i++){
        if(s[i] == 'd') level += 1;
        if(s[i] == 'u') level -= 1;
        if(level == 0) return i+1;
    }

    return i;
}

main(int argc, char *argv[]) {
    char label, *labels, *t_begin, *t_end;
    int  j, status;
    pid_t childpid;

    t_begin = argv[1]; 
    t_end   = t_begin + strlen(t_begin) - 1;
    labels  = argv[2];

newborn:
    label = *labels;  
    labels += 1;
    t_begin = t_begin + 1;
    while(t_begin < t_end ) {
        j = get_treesize(t_begin);
        if((childpid = fork()) == 0 ){
            t_end  = t_begin + j - 1;
            goto newborn;
        } else {
            // wait(NULL);
            t_begin += j;
            labels  += j/2;
        }
    }

    fprintf(stderr, "I'm %c, my pid=%ld, and my ppid=%ld\n",
            label, getpid(), getppid());

    int signalSum = 0;
    // leaf
    if (childpid == 0)
        while (1) pause();
    else {
        // interal node 會卡住 造成無法偵測錯誤訊號
        while (r_wait(&status) > 0) {
            if (WIFSIGNALED(status)) {
                printf("Child %d is terminated with signal %d.\n", childpid, WTERMSIG(status));
                signalSum += WTERMSIG(status);
            }
            if (WIFEXITED(status)) {
                signalSum += WEXITSTATUS(status);
            }
        }
        // if it is root process, dont print anything
        if (label != argv[2][0])
            printf("Child %d exits with value %d.\n", getpid(), signalSum);
        exit(signalSum);
    }
}
