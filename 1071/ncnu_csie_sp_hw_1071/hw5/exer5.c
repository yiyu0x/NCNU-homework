#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LABEL_SIZE 7
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
    strncpy(label, str, LABEL_SIZE-1);
    return remove_space(label);
}
char* get_start_addr(char* str) {
    int start = 7;
    char* label = malloc( 6 * sizeof(char) );
    strncpy(label, str+start, 6);
    return remove_space(label);
}
char* get_end_addr(char* str) {
    int start = 14;
    char* label = malloc( 6 * sizeof(char) );
    strncpy(label, str+start, 6);
    return remove_space(label);
}
char* get_opcode_addr_label(char* str) {
    if (strlen(str) <= 24) return "0000";

    int start = 24;
    char* label = malloc( 8 * sizeof(char) );
    strncpy(label, str+start, 8);
    // printf("-->%s\n", label);
    if (label[0]=='C' && label[1]=='\'')
        return "eof";
    if (label[0]=='X' && label[1]=='\'') {
        return label;
    }
    return remove_space(label);
}
char* get_opcode_label(char* str) {
    int start = 16;
    char* label = malloc( 8 * sizeof(char) );
    strncpy(label, str+start, 8);
    return remove_space(label);
}
char* get_addr_intfile(char* str) {
    char* label = malloc( 6 * sizeof(char) );
    strncpy(label, str, 6);
    return remove_space(label);
}
char* get_init_start(char* str) {
    char* label = malloc( 7 * sizeof(char) );
    strncpy(label, str, 7);
    return remove_space(label);
}
char* get_opcode(char* str) {
    if (!strcmp(str, "BYTE"))
        return "";
    if (!strcmp(str, "WORD"))
        return "00";
    if (!strcmp(str, "ADD"))
        return "18";
    if (!strcmp(str, "AND"))
        return "40";
    if (!strcmp(str, "COMP"))
        return "28";
    if (!strcmp(str, "DIV"))
        return "24";
    if (!strcmp(str, "J"))
        return "3C";
    if (!strcmp(str, "JEQ"))
        return "30";
    if (!strcmp(str, "JGT"))
        return "34";
    if (!strcmp(str, "JLT"))
        return "38";
    if (!strcmp(str, "JSUB"))
        return "48";
    if (!strcmp(str, "LDA"))
        return "00";
    if (!strcmp(str, "LDCH"))
        return "50";
    if (!strcmp(str, "LDL"))
        return "08";
    if (!strcmp(str, "LDX"))
        return "04";
    if (!strcmp(str, "MUL"))
        return "20";
    if (!strcmp(str, "OR"))
        return "44";
    if (!strcmp(str, "RD"))
        return "D8";
    if (!strcmp(str, "RSUB"))
        return "4C";
    if (!strcmp(str, "STA"))
        return "0C";
    if (!strcmp(str, "STCH"))
        return "54";
    if (!strcmp(str, "STL"))
        return "14";
    if (!strcmp(str, "STSW"))
        return "E8";
    if (!strcmp(str, "STX"))
        return "10";
    if (!strcmp(str, "SUB"))
        return "1C";
    if (!strcmp(str, "TD"))
        return "E0";
    if (!strcmp(str, "TIX"))
        return "2C";
    if (!strcmp(str, "WD"))
        return "DC";
    return "**";
}
char* get_opcode_addr(char* str) {
    // if (!strcmp("", str)) return "0000";
    if (!strcmp(str, "eof")) {
        return "454F46";
    }

    if (str[0]=='X' && str[1]=='\'') {
        char* s = malloc( 10 * sizeof(char) );
        strncpy(s, str+2, strlen(str)-4);
        return s;
    }
    if (!strcmp(str, "F3")) {
        return "F3";
    }
    char filename[] = "SYMTAB";
    FILE *file = fopen(filename, "r");
    size_t buffer_size = 80;
    char *buffer = malloc(buffer_size * sizeof(char));

    while(-1 != getline(&buffer, &buffer_size, file)) { 
        char* label = get_label(buffer);
        if (!strcmp(label, str)) {
            // printf("%s --> %s\n", label, get_start_addr(buffer));  
            char* addr = get_start_addr(buffer);
            char* addr_no_zero = malloc( 4 * sizeof(char) );
            
            strncpy(addr_no_zero, addr+2, 4);
            // printf("%s\n", addr_no_zero);
            return addr_no_zero;
        }
    }

    if (!strcmp(str, "BUFFER,X"))
        return "9042";
    char *fstr = (char*)malloc(4 * sizeof(char));
    sprintf(fstr, "%04X", atoi(str));
    // printf("-->%s\n", fstr);
    return fstr;
}

int main (int argc, char **argv) {
    // the file we want to read from
    char filename[] = "SYMTAB";
    char filename_intfile[] = "INTFILE";

    // open the file for reading
    FILE *file = fopen(filename, "r");
    FILE *file_intfile = fopen(filename_intfile, "r");

    if(NULL == file || NULL == file_intfile) {
        return 1;
    }

    size_t buffer_size = 80;
    char *buffer = malloc(buffer_size * sizeof(char));

    //header
    int line_number = 0;
    char *first_label;
    char *start_addr;
    char *end_addr;
    getline(&buffer, &buffer_size, file);
    first_label = get_label(buffer);
    start_addr = get_start_addr(buffer);
    char *start_addr_bk = start_addr;
    end_addr = get_end_addr(buffer);    
    printf("H%s   %s%s\n", first_label, start_addr, end_addr);
    //line1
    printf("T%s", start_addr);
    //30 byte --> hex --> 1E
    printf("1E");

    int head3 = 0;
    int head4 = 0;
    int head5 = 0;
    int head3_flag = 0;
    int head4_flag = 0;
    int head5_flag = 0;
    int counter = 0;
    while(-1 != getline(&buffer, &buffer_size, file_intfile)){
        //debug
        if (line_number > 0 && line_number < 11) {
            char *op_label = get_opcode_label(buffer);
            char *op_addr_label = get_opcode_addr_label(buffer);
            char *op_code= get_opcode(op_label);
            char *addr= get_opcode_addr(op_addr_label);

            printf("%s%s",op_code, addr);
        }
        if (line_number==11) {
            printf("\n");
            start_addr = get_addr_intfile(buffer);
            //line2
            printf("T%s", start_addr);
            printf("1E");
            //30 byte --> hex --> 1E, 30/3=10
        }
        if (line_number >= 11 && line_number < 21) {
            char *op_label = get_opcode_label(buffer);
            char *op_addr_label = get_opcode_addr_label(buffer);
            char *op_code= get_opcode(op_label);
            char *addr= get_opcode_addr(op_addr_label);

            printf("%s%s",op_code, addr);
        }
//////////////LINE3////////////////////////////////////////////////
        if (line_number >= 21 && head3 == 0) {
            char *op_label = get_opcode_label(buffer);
            if ( !strcmp(op_label, "RESW") || !strcmp(op_label, "RESB")) {
                line_number++;
                continue;
                // printf("%s\n", op_label);
            } else {
                printf("\n");
                start_addr = get_addr_intfile(buffer);
                // //line3
                printf("T%s", start_addr);
                printf("1E");
                head3 = 1;
            }
 
        }

        if (head3 == 1 && head3_flag == 0) {
            counter++;
            char *op_label = get_opcode_label(buffer);
            char *op_addr_label = get_opcode_addr_label(buffer);
            char *op_code= get_opcode(op_label);
            char *addr= get_opcode_addr(op_addr_label);

            printf("%s%s",op_code, addr);
            //buffer,x.   9042
            if (counter == 10) {
                counter = 0;
                head3_flag = 1;
                head4 = 1;
                continue;
            }
        }

        if (head4 == 1 && head4_flag == 0) {
            if (counter == 0) {
                char* start_addr = get_init_start(buffer);
                printf("\nT%s", start_addr);
                printf("1C");
            }
            counter++;
            char *op_label = get_opcode_label(buffer);
            char *op_addr_label = get_opcode_addr_label(buffer);
            char *op_code= get_opcode(op_label);
            char *addr= get_opcode_addr(op_addr_label);
            printf("%s%s",op_code, addr);
            if (counter == 10) {
                counter = 0;
                head4_flag = 1;
                head5 = 1;
                continue;
            }
        }
//////////////LINE4////////////////////////////////////////////////
        if (head5 == 1 && head5_flag == 0) {
            if (counter == 0) {
                char* start_addr = get_init_start(buffer);
                printf("\nT%s", start_addr);
                printf("19");
            }
            counter++;
            char *op_label = get_opcode_label(buffer);
            char *op_addr_label = get_opcode_addr_label(buffer);
            char *op_code= get_opcode(op_label);
            char *addr= get_opcode_addr(op_addr_label);
            printf("%s%s",op_code, addr);
            if (counter == 9) {
                counter = 0;
                head5_flag = 1;
                // head5 = 1;
                continue;
            }
        }
        line_number++; 
    }
    printf("\nE%s\n", start_addr_bk);
    fflush(stdout);
    fclose(file);
    free(buffer);

    return 0;
}