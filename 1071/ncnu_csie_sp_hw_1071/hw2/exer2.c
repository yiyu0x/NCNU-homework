#include <stdio.h>

int main(void) {
    int ch;
    while((ch = getc(stdin)) != EOF)
        putc(ch, stdout);
    
    return 0;
}
