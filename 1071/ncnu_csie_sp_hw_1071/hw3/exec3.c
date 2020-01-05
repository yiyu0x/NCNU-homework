#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define BUFF_SIZE 80
#define LABEL_SIZE 8
#define OPCODE_SIZE 5
#define OPERAND_SIZE 17

char *remove_space(char* str) {
	int len = strlen(str);
	int index = 0;
	for ( int i=0; i<len&&str[i]!='\n'; i++ )
		if ( str[i] != ' ' )
			str[index++] = str[i];
	str[index] = '\0';
	return str;
}

char* get_label(char* str) {
	//label 1-8
	char* label = malloc( LABEL_SIZE * sizeof(char) );
	strncpy(label, str, 8);
	
	return remove_space(label);
}

char* get_opcode(char* str) {
	//opcode 10-15
	int start = 9;
	char* opcode = malloc( OPCODE_SIZE * sizeof(char) );
	strncpy(opcode, str + start, OPCODE_SIZE);

	return remove_space(opcode);
}

char *get_operand(char* str) {
	//opcode 18-35
	int start = 17;
	char* operand = malloc( OPERAND_SIZE * sizeof(char) );
	//some case, the str not have enough length (like "         rsub")
	if ( strlen(str) >= start )
		strncpy(operand, str + start, OPERAND_SIZE);
	return remove_space(operand);
}

char* upper(char* str) {
	int len = strlen(str);
	if ( ( str[0] == 'C' || str[0] == 'c' ) && str[1] == '\'' ) {
		if ( str[0] == 'c' ) 
			str[0] -= 32;
		return str;
	}

	for ( int i=0; i<len; i++ ) {
		if ( str[i] >= 97 && str[i] <= 122 ) {
			str[i] -= 32;
		}
	}
	return str;
}

int main() {

	char buff[BUFF_SIZE];
	char *label;
	char *opcode;
	char *operand;

	while( fgets(buff, BUFF_SIZE, stdin) ) {
		if ( buff[0] != '.' ) {
			label = upper(get_label(buff));
			opcode = upper(get_opcode(buff));
			operand = upper(get_operand(buff));
			if ( strlen(operand) )
				printf("%-9s%-8s%s\n", label, opcode, operand);
			else
				printf("%-9s%s\n", label, opcode);
		}
	}

}
