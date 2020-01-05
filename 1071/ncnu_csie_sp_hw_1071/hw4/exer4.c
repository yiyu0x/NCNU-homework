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
	int addr;
	int after_start = 0;
	FILE *fin, *fout_intfile, *fout_symtab;
	fout_intfile = fopen("INTFILE","w");
	fout_symtab = fopen("SYMTAB","w");
	int addr_head;
	int addr_tail;

	while( fgets(buff, BUFF_SIZE, stdin) ) {
		label = upper(get_label(buff));
		opcode = upper(get_opcode(buff));
		operand = upper(get_operand(buff));
		//if opcode equal to "START"
		if ( !strcmp(opcode, "START") || after_start) {
			//first instruction
			if ( after_start == 0 ) addr = (int)strtol(operand, 0, 16);
			after_start += 1;
			//second instruction
			if ( after_start == 2 ) after_start = 0;
			addr_head = addr;
		} else if ( !strcmp(opcode, "END") ) 
			addr_tail = addr;

		//write string into file
		if ( strlen(operand) ) {
			fprintf(fout_intfile, "%06X %-9s%-8s%s\n",addr, label, opcode, operand);
			//if this line have label
			if ( strlen(label) ) {
				if ( after_start ) {
					fprintf(fout_symtab, "%-6s %06X xxxxxx\n",label, addr);	
				} else {
					fprintf(fout_symtab, "%-6s %06X\n",label, addr);
					// printf("%-6s %06X\n",label, addr);	
				}
			}
		} else {
			if ( !strcmp("ENDRD", label) )
				fprintf(fout_symtab, "%-6s %06X\n",label, addr);
				// printf("%s\n", label);
			fprintf(fout_intfile, "%06X %-9s%s\n",addr, label, opcode);
		}

		//update address
		if ( !strcmp(opcode, "BYTE") && !after_start ) {
			int c_counter = 0;
			if ( operand[0]=='c' || operand[0]=='C' ) {
				c_counter = strlen(operand)-3;
				addr += c_counter;
			} else if ( operand[0]=='x' || operand[0]=='X' ) {
				c_counter = (strlen(operand)-3)/2;
				addr += c_counter;
			}

			else
				addr += 1;
		}
		else if ( !strcmp(opcode, "RESB") && !after_start )
			addr += atoi(operand);
		else if ( !strcmp(opcode, "RESW") && !after_start )
			addr += 3 * atoi(operand);
		else if ( !after_start )
			addr += 3;
	}
	// printf("%X\n", addr_tail - addr_head);
	fseek(fout_symtab, 14, SEEK_SET);
	fprintf(fout_symtab, "%06X", addr_tail - addr_head);
	fclose(fout_intfile);
	fclose(fout_symtab);
}