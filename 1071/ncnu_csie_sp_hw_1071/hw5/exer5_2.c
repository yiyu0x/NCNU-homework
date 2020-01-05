#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define INPUT_STR 80
char *code_map[26] = {"00","04","48","14","28",
                      "30","3C","0C","08","4C",
                      "E0","D8","38","2C","10",
                      "18","DC","54","50","xx",
                      "20","1C","","","24",
                      "454F46"};
char *new_addr;
char **obj = NULL;

void get_head(char *s, char *p_name, char *start, char *end) {
  int i;
  for (i = 0; i <= 5; i++)  //Get Program Name
    p_name[i] = s[i];
  p_name[i] = '\0';
  for (i = 7; i <= 12; i++) //Get Start Address
    start[i-7] = s[i];
  start[i-7] = '\0';
  for (i = 14; i <= 19; i++) //Get End Address
    end[i-14] = s[i];
  end[i-14] = '\0';
}
char *copy_str(char *s, int st, int en) {
  int idx;
  char *str=malloc(sizeof(char)*1024);
  if (en < st)
    str[0] = '\0';
  else {
    for (idx = st; idx <= en; idx++)
      str[idx-st] = s[idx];
    str[idx-st-1] = '\0';
  }
  return str;
}
char *read_symtab(char *name) {
  char str_buf[INPUT_STR];
  char *p_name = malloc(sizeof(char) * 6);
  char *s_address = malloc(sizeof(char) * 6);
  char *e_address = malloc(sizeof(char) * 6);
  char *buf_addr = malloc(sizeof(char) * 6);
  char *str = malloc(sizeof(char) * 20);
  char *err_ch;
  int line_count;
  FILE *fp = fopen(name,"r");
  line_count = 0;
  new_addr = malloc(sizeof(char) * 4);
  while (fgets(str_buf, INPUT_STR, fp)) {
    line_count ++;
		if (line_count == 1)
		  get_head(str_buf, p_name, s_address, e_address);
    if (strstr(str_buf, "BUFFER") != NULL ) {  //get BUFFER data
      buf_addr = copy_str(str_buf, 9, 13);
      int hex_a = strtol(buf_addr, &err_ch, 16);
      int dir_a = 1;
      dir_a <<= 15; //set bit 15 is 1
      sprintf(new_addr, "%X", hex_a + dir_a); //new_addr is direct adress 
    }
  }
  fclose(fp);
  //printf("Program=%s start=%s end=%s\n", p_name, s_address, e_address);
  sprintf(str, "H%-6s%s%s", p_name, s_address, e_address);
  return str;
}
int check_byte(char *s) {
  if (strstr(s, "EOF") != NULL)
    return 19; // EOF ASCII is "454F46"
  if ((strstr(s, "INPUT") != NULL)||(strstr(s, "OUTPUT") != NULL)||
       (strstr(s, "      ") != NULL))
    return 30;
}
int get_code_num(char *s) {
  int i, flag = 1;
  if(strstr(s, "BYTE") != NULL)
    return check_byte(s);
  else if(strstr(s, "WORD") != NULL)
    return 31;
  else if(strstr(s, "DIV") != NULL)
    return 24;
  else if(strstr(s, " SUB ") != NULL)
    return 21;
  else if(strstr(s, "MUL") != NULL)
    return 20;
  else if(strstr(s, "LDCH") != NULL)
    return 18;
  else if(strstr(s, "STCH") != NULL)
    return 17;
  else if(strstr(s, "WD") != NULL)
    return 16;
  else if(strstr(s, "ADD") != NULL)
    return 15;
  else if(strstr(s, "STX") != NULL)
    return 14;
  else if(strstr(s, "TIX") != NULL)
    return 13;
  else if(strstr(s, "JLT") != NULL)
    return 12;
  else if(strstr(s, " RD ") != NULL) //
    return 11;
  else if(strstr(s, "TD") != NULL)
    return 10;
  else if(strstr(s, "RSUB") != NULL)
    return 9;
  else if(strstr(s, "LDL") != NULL)
    return 8;
  else if(strstr(s, "STA") != NULL)
    return 7;
  else if(strstr(s, "J ") != NULL) //
    return 6;
  else if(strstr(s, "JEQ") != NULL)
    return 5;
  else if(strstr(s, "COMP") != NULL)
    return 4;
  else if(strstr(s, "STL") != NULL)
    return 3;
  else if(strstr(s, "JSUB ") != NULL)
    return 2;
  else if(strstr(s, "LDX") != NULL)
    return 1;
  else if(strstr(s, "LDA") != NULL)
	  //printf("-%s %s %s\n", s, code_map[i], code_base[i]);
    return 0;
  else
    return i = 99;
}
char *read_symtab2(char *s, char *fname) {
  //fname is SYMTAB file
  char str_buf[INPUT_STR];
  char *operand = malloc(sizeof(char)*15);
  char *addr = malloc(sizeof(char)*6);
  FILE *fp_r1 = fopen(fname, "r");
  int i, j, line_count;
  line_count = 0;
  //Get operand
  operand = copy_str(s, 24, strlen(s)-1);
  //printf("%s operand=%s len=%d", s, operand, strlen(operand));
  if (strlen(operand) == 0)
    addr = "0000";
  else {
	  while (fgets(str_buf, INPUT_STR, fp_r1)) {
      if (strstr(str_buf, operand) != NULL) {
        //printf("%s ", str_buf);
        addr = copy_str(str_buf,9,  13);
        //printf("-%s-", addr);
        break;
      }
	    line_count ++;
	  }
	  fclose(fp_r1);
  }
  return addr;
}
char *get_byte_str(char *s) {
  char *sub_str;
  int idx = 0;
  sub_str = strchr(s, '\'');
  for (int i = 0; i<strlen(sub_str); i++) {
    if (sub_str[i] != '\'') {
      sub_str[idx] = sub_str[i];
      idx++;
    }
  }
  sub_str[idx - 1] = '\0';
  return sub_str;
}
int get_word_str(char *s) {
  char *sub_str, *e_p;
  int idx = 0;
  int dec;
  sub_str = malloc(sizeof(char) * 2);
  for (int i = 24; i<=strlen(s); i++) {
    sub_str[idx] = s[i];
    idx++;
  }
  sub_str[idx-1] = '\0';
  dec = strtol(sub_str, &e_p, 10);
  //printf("dec_str=%s -%X-",sub_str,dec);
  return dec;
}
char *read_intfile(char *name, char *name2) {
  //name is INTFILE; name2 is SYMTAB file
  FILE *fp = fopen(name,"r");
  char str_buf[INPUT_STR];
  char *dev_str = malloc(sizeof(char) * 10000);
  char *sub_dev_str = malloc(sizeof(char) * 80);
  char *addr = malloc(sizeof(char) * 6);
  int code, line_count = 1;
  dev_str[0] = '\0';
  while (fgets(str_buf, INPUT_STR, fp)) {
      code = get_code_num(str_buf);
      //printf("LineNo=%2d ", line_count);
    if ((code != 99) && (line_count > 1)) {
      //addr = read_symtab(str_buf);    //return address
      if ((code == 17) || (code == 18)) { //STCH or LDCH
        //Get New Address ...
        //printf("%s%s", code_map[code], new_addr);
        sprintf(sub_dev_str, "%s%s", code_map[code], new_addr);
        strcat(dev_str, sub_dev_str);
        strcpy(obj[line_count], sub_dev_str); }
      else if (code == 19) {
        //printf("%s", code_map[20]); //EOF
        sprintf(sub_dev_str, "%s", code_map[25]); //"454F46"
        strcat(dev_str, sub_dev_str);
        strcpy(obj[line_count], sub_dev_str); }
      else if (code == 30) {//BYTE
        //printf("%s", get_byte_str(str_buf));
        sprintf(sub_dev_str, "%s", get_byte_str(str_buf)); 
        strcat(dev_str, sub_dev_str); 
        strcpy(obj[line_count], sub_dev_str);}
      else if (code == 31) {//WORD
        //printf("%06X", get_word_str(str_buf));
        sprintf(sub_dev_str, "%06X", get_word_str(str_buf));
        strcat(dev_str, sub_dev_str);
        strcpy(obj[line_count], sub_dev_str); }
      else {
        addr = read_symtab2(str_buf, name2); //return address
        //printf("%s%s", code_map[code], addr);
        sprintf(sub_dev_str, "%s%s", code_map[code], addr);
        strcat(dev_str, sub_dev_str);
        //printf("%s%s\n", code_map[code], addr);
        strcpy(obj[line_count], sub_dev_str);
      }
    }
    line_count++;
  } //while end
  fclose(fp);
  return dev_str;
}
int read_line_num(char *name) {
  FILE *fp = fopen(name,"r");
  char str_buf[INPUT_STR];
  int num = 1;
  while (fgets(str_buf, INPUT_STR, fp)) {
    num++;
  }
  fclose(fp);
  return num;
}
void init_obj_array(int col) {
  for (int i = 0; i < col; i++) {
	  obj[i] = (char*)malloc( sizeof(char) * 7);
    strcpy(obj[i], "\0");
  }
}
void print_obj_array(int col) {
  for (int i = 0; i < col; i++)
    printf("line[%2d]=%-6s len=%ld\n",i, obj[i], strlen(obj[i]));
}
int main(int argc, char *argv[]) {
  char str_buf[INPUT_STR];
  FILE *fp_intfile, *fp_symtab;
  char *obj_str = malloc(sizeof(char) * 10000);
  char *sub_str = malloc(sizeof(char) * 80);
  char *head = malloc(sizeof(char) * 19);
  char *s_address = malloc(sizeof(char) * 7);
  char *err_ch;
  int col, hex_a, last_hex_a;
  if (argc == 3) {
    fp_intfile = fopen(argv[1], "r");  
    fp_symtab = fopen(argv[2], "r");
    head = read_symtab(argv[2]);
    s_address = copy_str(head, 7,13);
    printf("%s\n", read_symtab(argv[2]));
    //printf("%s\n", read_symtab(argv[2]));
  }
  else {  //if no user input then default INTFILE & SYMTAB
    argv[1] = "INTFILE";
    argv[2] = "SYMTAB";
    fp_intfile = fopen(argv[1], "r");
    fp_symtab = fopen(argv[2], "r");
    head = read_symtab(argv[2]);
    s_address = copy_str(head, 7,13);
    printf("%s\n", read_symtab(argv[2]));
  }
  //printf("new_addr=%s\n",new_addr);
  //-----Get INTFILE objcode then trans to obj array (col * 7 )-----
  col = read_line_num(argv[1]);
  obj = (char**)malloc( sizeof(char*) * col );
  //-----init obj array-----
    init_obj_array(col);  
  //------------------------
  obj_str = read_intfile(argv[1], argv[2]);
    //printf("Line= %d\n", col);
    //printf("%s\n", obj_str);
    
  //-----print obj array-----
    //print_obj_array(col);
  //-------------------------
  int line = 1;
  int len_count = 0;
  int print_flag = 0;
  int set = 0;
  sub_str[0] = '\0';
  //-----Pass2 Read INTFILE-----
  while (fgets(str_buf, INPUT_STR, fp_intfile)) {
	hex_a = strtol(copy_str(str_buf,2,6), &err_ch, 16);  
    if (line == 1) { 
		line ++; 
		last_hex_a = hex_a;
		continue;
    }
    if (((line == 2)||(print_flag == 1)||(hex_a - last_hex_a > 3))&&
        (strlen(obj[line]) != 0)) {
      printf("T%s", copy_str(str_buf, 0, 6));
      print_flag = 0;
    }
    if (strlen(obj[line]) != 0) {
      strcat(sub_str, obj[line]);
      len_count += strlen(obj[line]) / 2;
      set += 1; // 6 bit = 1set
    }
    if (set == 10) {
      printf("%X%s\n", len_count, sub_str);
      len_count = 0;
      sub_str[0] = '\0';
      set = 0; //6 bit = 1set
      print_flag = 1;
    }  
    line ++;
    last_hex_a = hex_a;
  } //while end
  fclose(fp_intfile);
  printf("%X%s\n", len_count, sub_str);
  printf("E%s\n", s_address);
}
