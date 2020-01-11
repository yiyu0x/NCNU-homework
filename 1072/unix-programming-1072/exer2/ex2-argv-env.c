#include <stdio.h>
extern char **environ;

int main(int argc, char* argv[]){
	printf("argc is %d\n", argc);
	for(int i=0; i<argc; i++)
		printf("argv[%d]: %s\n", i, argv[i]);
	for(int i=0; environ[i]!=NULL; i++)
     	printf("environ[%d]: %s\n", i, environ[i]);
    printf("\n");
    printf("argc      is resided at %p\n", &argc);
    printf("argv      is resided at %p\n", &argv);
    printf("environ   is resided at %p\n", &environ);
    printf("argv[]    is resided at %p\n", argv);
    printf("environ[] is resided at %p\n", environ);
    for(int i=0; i<=argc; i++)
    	printf("value of argv[%2d] is %p\n", i, argv[i]);
    for(int i=0; environ[i]!=NULL; i++)
    	printf("value of env [%2d] is %p\n", i, environ[i]);
}
