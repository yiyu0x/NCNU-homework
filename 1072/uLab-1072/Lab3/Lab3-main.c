/*
P2 => Keyboard
P1 => 7段顯示器
				0	
				1	
				2	
				3
4	5	6	7

*/
#include <8051.h>
#include <stdbool.h>
#include "LED_Display.h"
#include "Keypad4x4.h"
int main() {
	short table[4] = {0x70, 0xb0, 0xd0, 0xe0};
	short num[4] = {15, 15, 15, 15};
	short row = 0;
	P2=0b11111110;
	short count = 1;
	short number = 0;
	short previous = -1;
	while (1) {
		P2    =count^0b11111111;
		count *=2; //shift
		short key = keyPressed(row);
		if (key != -1 && key != previous) {	//有按且不等於上一按 => 處理debounce
			previous = key;
			num[0] =num[1];
			num[1] =num[2];
			num[2] =num[3];			
			num[3] = key;	//往前推
		}
		row++;
		if (count == 0x10) {	//用count從上往下掃 
			count = 1;
			row   = 0;
		}
		LED_Display(table,num);
	}
}
	