//LED 跑馬燈
#include <8051.h>
/*
0 是 亮
1 是 暗

	P1 = D2 ~ D9
	P2 = D10 ~ D17
	P0 = D18 ~ D25

*/
void main()
{
	while(1){
		P0=0x01;
	}
}