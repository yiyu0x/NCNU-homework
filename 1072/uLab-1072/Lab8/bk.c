#include <8051.h>
#include <stdlib.h>
#define PERIOD 15536
const short SPIN[] = {0x03, 0x06, 0x0C, 0x09};
int count=50; // 一圈200步
int max=50;
char direct=0; 
unsigned char step=0x01;
unsigned int speed=(65536-8000);
const double interrupt_table[]={0.05, 0.016666666666666663, 0.013636363636363641, 0.0118705035971223, 0.010667938043629935};
const int step2[]={20.0, 60.0, 73.33333333333333, 84.24242424242424, 93.73882712012208, 100};
int index=0;
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
		index++;
	}
}
int main(){
	IE=0x82;
	TMOD=0x01;
	TH0=speed/256;
	TL0=speed%16;

	for(int i=0;i<5;i++){
		interrupt_table[i]*=100000;
		interrupt_table[i]=65536-interrupt_table[i];
	}
	while (1) {
	}
}