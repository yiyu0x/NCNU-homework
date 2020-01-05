/*
	8*8LED 用P2

*/

#include <8051.h>

const int t[8]={
0b01111111,
0b00111111,
0b00011111,
0b00001111,
0b00000111,
0b00000011,
0b00000001,
0b00000000
};
const int a[8]={
	0b11100111,
	0b11011011,
	0b10111101,
	0b10000001,
	0b10111101,
	0b10111101,
	0b10111101,
	0b11111111
};
int counter;	//	掃a[0] ~ a[7]
int tmp;		//	P0補數暫存
int multi;		//	掃10次位移一次
int index;		//	位移
void delay() {
	unsigned d1;
	for (d1 = 0; d1 < 800; d1 ++) {
	}
}
void display(){
	P0=tmp^0xff;
	P2=a[((counter--)+index)&7];
	delay();
	tmp<<=1;
	if(tmp==0){
		tmp=0x01;
		counter=7;
		multi++;
		if(multi==10){
			multi=0;
			index++;
			if(index==8)
				index=0;
		}
	}
}
int main() {
	counter=7;
	tmp=1;
	index=0;
	P1=0xff;
	while(1){
		display();
	//	以下是測試用code
	//	P0=0b10101010;
	//	P0=0b01010101;
	//	P0=0xff;		//橫列row => 0 light
	//	P2=0x00;		//左邊直行 => 0 
	//	P2=0x00;		//右邊直行 => 0 light
	}
}