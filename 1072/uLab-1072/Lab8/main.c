#include <8051.h>
#include <stdlib.h>
#define PERIOD 15536
const short SPIN[] = {0x03, 0x06, 0x0C, 0x09};
int count=4000; // 一圈200步
//int max=50;
char direct=0; 
unsigned char step=0x01;
unsigned int speed=(65536-65536);
//fast => 65536 - 7700
//65536-7500

//int f0=65536-10000;
int f0=65536-30000;
int fmax=65536-7500;
//65536-7500
int tacc=1;

//int interrupt_table[]={60536.0, 63869.333333333336, 64172.36363636363, 64348.94964028777, 64469.20619563701};

int count2[]={20.0, 60.0, 73.33333333333333, 84.24242424242424, 93.73882712012208, 100};
int index=0;
int count3=0;

void timer_isr (void) __interrupt (1) __using (1) {	//timer 0 interrupt 訊號		using register bank 1
//	TH0=interrupt_table[index]/256;
//	TL0=interrupt_table[index]%16; 
//	TH0=speed/256;
//	TL0=speed%16;

	TH0=f0/256;
	TL0=f0%16;   

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
	count3++;
	if(count3>=10){
		if(f0<fmax)
			f0+=100;
	}
	if(--count<=0){
		if(direct==1)
			TR0=0;
		direct=1;
		count=4000;
		count3=0;
		f0=65536-30000;
	}
}
int main(){
	IE=0x82;
	TMOD=0x01;
	TH0=f0/256;
	TL0=f0%16;
	TR0=1;
	while (1) {
	}
}