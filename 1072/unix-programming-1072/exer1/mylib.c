#include <stdio.h>
#include "mylib.h"
void transpose(char *s) {
	char* pos = s;
	while(*pos != '\0') {
		if ((*pos >= 65 && *pos <= 90) || 
			(*pos >= 97 && *pos <= 122)) 
			*pos ^= 0x20;
		pos++;
	}
	printf("%s\n", s);
}