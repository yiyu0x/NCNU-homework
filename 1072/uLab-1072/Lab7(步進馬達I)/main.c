#include <8051.h>
#include <stdlib.h>
#define PERIOD 15536
const short SPIN[] = {0x03, 0x06, 0x0C, 0x09};
int count=50; // 一圈200步
int max=50;
char direct=0; 
unsigned char step=0x01; 
unsigned int speed=(65536-30000);
void delay(unsigned int time)
{
        unsigned i,j ;
        for(i=0;i<time;i++)    
        for(j=0;j<1275;j++);
}
void timer_isr (void) __interrupt (1) __using (1) {	//timer 0 interrupt 訊號		using register bank 1
	TH0=speed/256; 
	TL0=speed%16; 

	if(direct==0) { 
		step>>=1; 
		if(step==0x00) step=0x08;
		P0&=0xf0; 
		P0|=step; 
	}
	else { 
		step<<=1; 
		if(step==0x10) 
		step=0x01;
		P0&=0xf0; 
		P0|=step; 
	}
	if(--count<=0){
		TR0=0;
	}
}

short keyPressed(short row) {
	if((P2 & 0b11110000) != 0b11110000){	//if 按下按鈕
		for (short c = 1, col = 0; col < 4; c *= 2, col++) {
			//前四位=>後四位 並且遮蔽前四位	偵測哪一個column被按下去
`			short magic = ((P2 >> 4) ^ 0b11111111) & 0b00001111;
			if (magic == c) {
				return col * 4 + row;
			}
		}
	}
	return -1;	//沒按 return -1
}
void LED_Display(short table[], short num[]) {
	for(short i = 0; i < 4; i++) {
		P1  = table[i] + num[i];
		for(int j = 0; j < 1000; j++){}
	}
}

int main(){
	IE=0x82;
	TMOD=0x01;
	TH0=speed/256;
	TL0=speed%16;

	short table[4] = {0x70, 0xb0, 0xd0, 0xe0};
	int num[4] = {0,0,0,0};
	short row = 0;
	P2=0b11111110;
	short cnt = 1;

	short previous = -1;
	short previous2=-1;
	while (1) {
		P2    =cnt^0b11111111;
		cnt *=2; //shift
		short key = keyPressed(row);
		if (key != -1 && key != previous && key!=10 && key!=11) {	//有按且不等於上一按 => 處理debounce
			previous = key;
			previous2=key;
			num[0] =num[1];
			num[1] =num[2];
			num[2] =num[3];			
			num[3] = key;	//往前推
		}
		
		if((key==10 || key==11)&& previous2!=key){	//debounce!
			previous2= key;
			count=(num[1]*100+num[2]*10+num[3])/360.0*200.0;
			num[0]=0,num[1]=0,num[2]=0,num[3]=0;
			direct=0;
			if(key==11)
				direct=1;
			TR0=1;
		}
		row++;
		if (cnt == 0x10) {	//用cnt從上往下掃 
			cnt = 1;
			row = 0;
		}
		LED_Display(table,num);
	}
}