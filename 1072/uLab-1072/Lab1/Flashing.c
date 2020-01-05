//LED 跑馬燈
#include <8051.h>
/*
0 是 亮
1 是 暗

	P1 = D2 ~ D9
	P2 = D10 ~ D17
	P0 = D18 ~ D25

*/
void timer() {
	unsigned d1, d2;
	for (d1 = 0; d1 < 1024; d1 ++) {
		for (d2 = 0; d2 < 100; d2 ++) {
		}
	}
}
void main()
{
	unsigned led;
	led = 16; // 12 O'clock
	int CASE = 0;

	while (1) {
		if (CASE == 0) {
			led >>= 1;
			P1 = ~led;
			if (led == 0) {
				CASE = 1;
				led = 256;
				P1 = 255; // turn all off
			}
		}
		if (CASE == 1) {
			led >>= 1;
			P0 = ~led;
			if (led == 0) {
				CASE = 2;
				led = 256;
				P0 = 255; // turn all off
			}
		}
		if (CASE == 2) {
			led >>= 1;
			P2 = ~led;
			if (led == 0) {
				CASE = 0;
				led = 256;
				P2 = 255;
				continue; // turn all off
			}
		}
		timer();
	}
}