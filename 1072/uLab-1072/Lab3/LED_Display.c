#include "LED_Display.h"
#include <8051.h>
void LED_Display(short table[], short num[]) {
	for(short i = 0; i < 4; i++) {
		P1  = table[i] + num[i];
		for(int j = 0; j < 10000; j++){}
	}
}
