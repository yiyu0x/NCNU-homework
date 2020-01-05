/*
記得接電
按鈕加減 顯示於7段顯示器
P0 => 按按鈕 (PB,SW &)
P1 => 七段顯示器

push bottom 0 1 2 3
switch 		4 5 6 7

*/
#include <8051.h>
#include <stdbool.h>
// p0 : 18 ~ 25

void delay(short time) {
	unsigned short d1;
	for (d1 = 0; d1 < time*100; d1 ++) {
	}
}
void main() {
	short table[] = {0x75, 0xb0};	//初始值 5 0
	bool index = 0;
	bool flag_plus = 1;
	bool flag_minus = 1;
	while (1) {
		
		index = !index;
		P1 = table[index];
		delay(50);

		if (P0_0 == 0 && flag_minus) {
			if (table[0] == 0x70 && table[1] == 0xb0) continue;
			flag_minus = 0;
			table[1] -= 1;
			if (table[1] == 0xaf) {
				table[1] = 0xb9;
				table[0]--;
			}
		}
		else if (P0_0 == 1) flag_minus = 1;
		//
		if (P0_1 == 0 && flag_plus) {
			if (table[0] == 0x79 && table[1] == 0xb9) continue;
			flag_plus = 0;
			table[1] += 1;
			if (table[1] == 0xba) {
				table[1] = 0xb0;
				table[0]++;
			}
		}
		else if (P0_1 == 1) flag_plus = 1;
	}
}