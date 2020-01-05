;--------------------------------------------------------
; File Created by SDCC : free open source ANSI-C Compiler
; Version 3.8.0 #10562 (MINGW64)
;--------------------------------------------------------
	.module main
	.optsdcc -mmcs51 --model-small
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _SPIN
	.globl _main
	.globl _timer_isr
	.globl _CY
	.globl _AC
	.globl _F0
	.globl _RS1
	.globl _RS0
	.globl _OV
	.globl _F1
	.globl _P
	.globl _PS
	.globl _PT1
	.globl _PX1
	.globl _PT0
	.globl _PX0
	.globl _RD
	.globl _WR
	.globl _T1
	.globl _T0
	.globl _INT1
	.globl _INT0
	.globl _TXD
	.globl _RXD
	.globl _P3_7
	.globl _P3_6
	.globl _P3_5
	.globl _P3_4
	.globl _P3_3
	.globl _P3_2
	.globl _P3_1
	.globl _P3_0
	.globl _EA
	.globl _ES
	.globl _ET1
	.globl _EX1
	.globl _ET0
	.globl _EX0
	.globl _P2_7
	.globl _P2_6
	.globl _P2_5
	.globl _P2_4
	.globl _P2_3
	.globl _P2_2
	.globl _P2_1
	.globl _P2_0
	.globl _SM0
	.globl _SM1
	.globl _SM2
	.globl _REN
	.globl _TB8
	.globl _RB8
	.globl _TI
	.globl _RI
	.globl _P1_7
	.globl _P1_6
	.globl _P1_5
	.globl _P1_4
	.globl _P1_3
	.globl _P1_2
	.globl _P1_1
	.globl _P1_0
	.globl _TF1
	.globl _TR1
	.globl _TF0
	.globl _TR0
	.globl _IE1
	.globl _IT1
	.globl _IE0
	.globl _IT0
	.globl _P0_7
	.globl _P0_6
	.globl _P0_5
	.globl _P0_4
	.globl _P0_3
	.globl _P0_2
	.globl _P0_1
	.globl _P0_0
	.globl _B
	.globl _ACC
	.globl _PSW
	.globl _IP
	.globl _P3
	.globl _IE
	.globl _P2
	.globl _SBUF
	.globl _SCON
	.globl _P1
	.globl _TH1
	.globl _TH0
	.globl _TL1
	.globl _TL0
	.globl _TMOD
	.globl _TCON
	.globl _PCON
	.globl _DPH
	.globl _DPL
	.globl _SP
	.globl _P0
	.globl _count3
	.globl _index
	.globl _count2
	.globl _tacc
	.globl _fmax
	.globl _f0
	.globl _speed
	.globl _step
	.globl _direct
	.globl _max
	.globl _count
;--------------------------------------------------------
; special function registers
;--------------------------------------------------------
	.area RSEG    (ABS,DATA)
	.org 0x0000
_P0	=	0x0080
_SP	=	0x0081
_DPL	=	0x0082
_DPH	=	0x0083
_PCON	=	0x0087
_TCON	=	0x0088
_TMOD	=	0x0089
_TL0	=	0x008a
_TL1	=	0x008b
_TH0	=	0x008c
_TH1	=	0x008d
_P1	=	0x0090
_SCON	=	0x0098
_SBUF	=	0x0099
_P2	=	0x00a0
_IE	=	0x00a8
_P3	=	0x00b0
_IP	=	0x00b8
_PSW	=	0x00d0
_ACC	=	0x00e0
_B	=	0x00f0
;--------------------------------------------------------
; special function bits
;--------------------------------------------------------
	.area RSEG    (ABS,DATA)
	.org 0x0000
_P0_0	=	0x0080
_P0_1	=	0x0081
_P0_2	=	0x0082
_P0_3	=	0x0083
_P0_4	=	0x0084
_P0_5	=	0x0085
_P0_6	=	0x0086
_P0_7	=	0x0087
_IT0	=	0x0088
_IE0	=	0x0089
_IT1	=	0x008a
_IE1	=	0x008b
_TR0	=	0x008c
_TF0	=	0x008d
_TR1	=	0x008e
_TF1	=	0x008f
_P1_0	=	0x0090
_P1_1	=	0x0091
_P1_2	=	0x0092
_P1_3	=	0x0093
_P1_4	=	0x0094
_P1_5	=	0x0095
_P1_6	=	0x0096
_P1_7	=	0x0097
_RI	=	0x0098
_TI	=	0x0099
_RB8	=	0x009a
_TB8	=	0x009b
_REN	=	0x009c
_SM2	=	0x009d
_SM1	=	0x009e
_SM0	=	0x009f
_P2_0	=	0x00a0
_P2_1	=	0x00a1
_P2_2	=	0x00a2
_P2_3	=	0x00a3
_P2_4	=	0x00a4
_P2_5	=	0x00a5
_P2_6	=	0x00a6
_P2_7	=	0x00a7
_EX0	=	0x00a8
_ET0	=	0x00a9
_EX1	=	0x00aa
_ET1	=	0x00ab
_ES	=	0x00ac
_EA	=	0x00af
_P3_0	=	0x00b0
_P3_1	=	0x00b1
_P3_2	=	0x00b2
_P3_3	=	0x00b3
_P3_4	=	0x00b4
_P3_5	=	0x00b5
_P3_6	=	0x00b6
_P3_7	=	0x00b7
_RXD	=	0x00b0
_TXD	=	0x00b1
_INT0	=	0x00b2
_INT1	=	0x00b3
_T0	=	0x00b4
_T1	=	0x00b5
_WR	=	0x00b6
_RD	=	0x00b7
_PX0	=	0x00b8
_PT0	=	0x00b9
_PX1	=	0x00ba
_PT1	=	0x00bb
_PS	=	0x00bc
_P	=	0x00d0
_F1	=	0x00d1
_OV	=	0x00d2
_RS0	=	0x00d3
_RS1	=	0x00d4
_F0	=	0x00d5
_AC	=	0x00d6
_CY	=	0x00d7
;--------------------------------------------------------
; overlayable register banks
;--------------------------------------------------------
	.area REG_BANK_0	(REL,OVR,DATA)
	.ds 8
	.area REG_BANK_1	(REL,OVR,DATA)
	.ds 8
;--------------------------------------------------------
; overlayable bit register bank
;--------------------------------------------------------
	.area BIT_BANK	(REL,OVR,DATA)
bits:
	.ds 1
	b0 = bits[0]
	b1 = bits[1]
	b2 = bits[2]
	b3 = bits[3]
	b4 = bits[4]
	b5 = bits[5]
	b6 = bits[6]
	b7 = bits[7]
;--------------------------------------------------------
; internal ram data
;--------------------------------------------------------
	.area DSEG    (DATA)
_count::
	.ds 2
_max::
	.ds 2
_direct::
	.ds 1
_step::
	.ds 1
_speed::
	.ds 2
_f0::
	.ds 2
_fmax::
	.ds 2
_tacc::
	.ds 2
_count2::
	.ds 12
_index::
	.ds 2
_count3::
	.ds 2
;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
;--------------------------------------------------------
; Stack segment in internal ram 
;--------------------------------------------------------
	.area	SSEG
__start__stack:
	.ds	1

;--------------------------------------------------------
; indirectly addressable internal ram data
;--------------------------------------------------------
	.area ISEG    (DATA)
;--------------------------------------------------------
; absolute internal ram data
;--------------------------------------------------------
	.area IABS    (ABS,DATA)
	.area IABS    (ABS,DATA)
;--------------------------------------------------------
; bit data
;--------------------------------------------------------
	.area BSEG    (BIT)
;--------------------------------------------------------
; paged external ram data
;--------------------------------------------------------
	.area PSEG    (PAG,XDATA)
;--------------------------------------------------------
; external ram data
;--------------------------------------------------------
	.area XSEG    (XDATA)
;--------------------------------------------------------
; absolute external ram data
;--------------------------------------------------------
	.area XABS    (ABS,XDATA)
;--------------------------------------------------------
; external initialized ram data
;--------------------------------------------------------
	.area XISEG   (XDATA)
	.area HOME    (CODE)
	.area GSINIT0 (CODE)
	.area GSINIT1 (CODE)
	.area GSINIT2 (CODE)
	.area GSINIT3 (CODE)
	.area GSINIT4 (CODE)
	.area GSINIT5 (CODE)
	.area GSINIT  (CODE)
	.area GSFINAL (CODE)
	.area CSEG    (CODE)
;--------------------------------------------------------
; interrupt vector 
;--------------------------------------------------------
	.area HOME    (CODE)
__interrupt_vect:
	ljmp	__sdcc_gsinit_startup
	reti
	.ds	7
	ljmp	_timer_isr
;--------------------------------------------------------
; global & static initialisations
;--------------------------------------------------------
	.area HOME    (CODE)
	.area GSINIT  (CODE)
	.area GSFINAL (CODE)
	.area GSINIT  (CODE)
	.globl __sdcc_gsinit_startup
	.globl __sdcc_program_startup
	.globl __start__stack
	.globl __mcs51_genXINIT
	.globl __mcs51_genXRAMCLEAR
	.globl __mcs51_genRAMCLEAR
;	main.c:5: int count=2000; // 一圈200步
	mov	_count,#0xd0
	mov	(_count + 1),#0x07
;	main.c:6: int max=50;
	mov	_max,#0x32
	mov	(_max + 1),#0x00
;	main.c:7: char direct=0; 
	mov	_direct,#0x00
;	main.c:8: unsigned char step=0x01;
	mov	_step,#0x01
;	main.c:9: unsigned int speed=(65536-65536);
	clr	a
	mov	_speed,a
	mov	(_speed + 1),a
;	main.c:14: int f0=65536-30000;
	mov	_f0,#0xd0
	mov	(_f0 + 1),#0x8a
;	main.c:15: int fmax=65536-7500;
	mov	_fmax,#0xb4
	mov	(_fmax + 1),#0xe2
;	main.c:17: int tacc=1;
	mov	_tacc,#0x01
;	1-genFromRTrack replaced	mov	(_tacc + 1),#0x00
	mov	(_tacc + 1),a
;	main.c:21: int count2[]={20.0, 60.0, 73.33333333333333, 84.24242424242424, 93.73882712012208, 100};
	mov	(_count2 + 0),#0x14
;	1-genFromRTrack replaced	mov	(_count2 + 1),#0x00
	mov	(_count2 + 1),a
	mov	((_count2 + 0x0002) + 0),#0x3c
;	1-genFromRTrack replaced	mov	((_count2 + 0x0002) + 1),#0x00
	mov	((_count2 + 0x0002) + 1),a
	mov	((_count2 + 0x0004) + 0),#0x49
;	1-genFromRTrack replaced	mov	((_count2 + 0x0004) + 1),#0x00
	mov	((_count2 + 0x0004) + 1),a
	mov	((_count2 + 0x0006) + 0),#0x54
;	1-genFromRTrack replaced	mov	((_count2 + 0x0006) + 1),#0x00
	mov	((_count2 + 0x0006) + 1),a
	mov	((_count2 + 0x0008) + 0),#0x5d
;	1-genFromRTrack replaced	mov	((_count2 + 0x0008) + 1),#0x00
	mov	((_count2 + 0x0008) + 1),a
	mov	((_count2 + 0x000a) + 0),#0x64
;	1-genFromRTrack replaced	mov	((_count2 + 0x000a) + 1),#0x00
	mov	((_count2 + 0x000a) + 1),a
;	main.c:22: int index=0;
	mov	_index,a
	mov	(_index + 1),a
;	main.c:23: int count3=0;
	mov	_count3,a
	mov	(_count3 + 1),a
	.area GSFINAL (CODE)
	ljmp	__sdcc_program_startup
;--------------------------------------------------------
; Home
;--------------------------------------------------------
	.area HOME    (CODE)
	.area HOME    (CODE)
__sdcc_program_startup:
	ljmp	_main
;	return from main will return to caller
;--------------------------------------------------------
; code
;--------------------------------------------------------
	.area CSEG    (CODE)
;------------------------------------------------------------
;Allocation info for local variables in function 'timer_isr'
;------------------------------------------------------------
;	main.c:25: void timer_isr (void) __interrupt (1) __using (1) {	//timer 0 interrupt 訊號		using register bank 1
;	-----------------------------------------
;	 function timer_isr
;	-----------------------------------------
_timer_isr:
	ar7 = 0x0f
	ar6 = 0x0e
	ar5 = 0x0d
	ar4 = 0x0c
	ar3 = 0x0b
	ar2 = 0x0a
	ar1 = 0x09
	ar0 = 0x08
	push	bits
	push	acc
	push	b
	push	dpl
	push	dph
	push	(0+7)
	push	(0+6)
	push	(0+5)
	push	(0+4)
	push	(0+3)
	push	(0+2)
	push	(0+1)
	push	(0+0)
	push	psw
	mov	psw,#0x08
;	main.c:31: TH0=f0/256;
	mov	__divsint_PARM_2,#0x00
	mov	(__divsint_PARM_2 + 1),#0x01
	mov	dpl,_f0
	mov	dph,(_f0 + 1)
	mov	psw,#0x00
	lcall	__divsint
	mov	psw,#0x08
	mov	r6,dpl
	mov	_TH0,r6
;	main.c:32: TL0=f0%16;   
	mov	__modsint_PARM_2,#0x10
	mov	(__modsint_PARM_2 + 1),#0x00
	mov	dpl,_f0
	mov	dph,(_f0 + 1)
	mov	psw,#0x00
	lcall	__modsint
	mov	psw,#0x08
	mov	r6,dpl
	mov	r7,dph
	mov	_TL0,r6
;	main.c:34: if(direct==0) { 
	mov	a,_direct
	jnz	00106$
;	main.c:35: step>>=1;
	mov	a,_step
	clr	c
	rrc	a
;	main.c:36: if(step==0x00) step=0x08;
	mov	_step,a
	jnz	00102$
	mov	_step,#0x08
00102$:
;	main.c:37: P0&=0xf0;
	anl	_P0,#0xf0
;	main.c:38: P0|=step;
	mov	a,_step
	orl	_P0,a
	sjmp	00107$
00106$:
;	main.c:41: step<<=1; 
	mov	a,_step
	mov	r7,a
	add	a,acc
	mov	_step,a
;	main.c:42: if(step==0x10)
	mov	a,#0x10
	cjne	a,_step,00104$
;	main.c:43: step=0x01;
	mov	_step,#0x01
00104$:
;	main.c:44: P0&=0xf0;
	anl	_P0,#0xf0
;	main.c:45: P0|=step;
	mov	a,_step
	orl	_P0,a
00107$:
;	main.c:47: count3++;
	inc	_count3
	clr	a
	cjne	a,_count3,00150$
	inc	(_count3 + 1)
00150$:
;	main.c:48: if(count3>=10){
	clr	c
	mov	a,_count3
	subb	a,#0x0a
	mov	a,(_count3 + 1)
	xrl	a,#0x80
	subb	a,#0x80
;	main.c:49: if(f0<fmax)
	jc	00111$
	mov	a,_f0
	subb	a,_fmax
	mov	a,(_f0 + 1)
	xrl	a,#0x80
	mov	b,(_fmax + 1)
	xrl	b,#0x80
	subb	a,b
	jnc	00111$
;	main.c:50: f0+=100;
	mov	a,#0x64
	add	a,_f0
	mov	_f0,a
	clr	a
	addc	a,(_f0 + 1)
	mov	(_f0 + 1),a
00111$:
;	main.c:52: if(--count<=0){
	dec	_count
	mov	a,#0xff
	cjne	a,_count,00153$
	dec	(_count + 1)
00153$:
	clr	c
	clr	a
	subb	a,_count
	mov	a,#(0x00 ^ 0x80)
	mov	b,(_count + 1)
	xrl	b,#0x80
	subb	a,b
	jc	00116$
;	main.c:53: if(direct==1)
	mov	a,#0x01
	cjne	a,_direct,00113$
;	main.c:54: TR0=0;
;	assignBit
	clr	_TR0
00113$:
;	main.c:55: direct=1;
	mov	_direct,#0x01
;	main.c:56: count=4000;
	mov	_count,#0xa0
	mov	(_count + 1),#0x0f
;	main.c:57: count3=0;
	clr	a
	mov	_count3,a
	mov	(_count3 + 1),a
;	main.c:58: f0=65536-30000;
	mov	_f0,#0xd0
	mov	(_f0 + 1),#0x8a
00116$:
;	main.c:60: }
	pop	psw
	pop	(0+0)
	pop	(0+1)
	pop	(0+2)
	pop	(0+3)
	pop	(0+4)
	pop	(0+5)
	pop	(0+6)
	pop	(0+7)
	pop	dph
	pop	dpl
	pop	b
	pop	acc
	pop	bits
	reti
;------------------------------------------------------------
;Allocation info for local variables in function 'main'
;------------------------------------------------------------
;	main.c:61: int main(){
;	-----------------------------------------
;	 function main
;	-----------------------------------------
_main:
	ar7 = 0x07
	ar6 = 0x06
	ar5 = 0x05
	ar4 = 0x04
	ar3 = 0x03
	ar2 = 0x02
	ar1 = 0x01
	ar0 = 0x00
;	main.c:62: IE=0x82;
	mov	_IE,#0x82
;	main.c:63: TMOD=0x01;
	mov	_TMOD,#0x01
;	main.c:64: TH0=f0/256;
	mov	__divsint_PARM_2,#0x00
	mov	(__divsint_PARM_2 + 1),#0x01
	mov	dpl,_f0
	mov	dph,(_f0 + 1)
	lcall	__divsint
	mov	r6,dpl
	mov	_TH0,r6
;	main.c:65: TL0=f0%16;
	mov	__modsint_PARM_2,#0x10
	mov	(__modsint_PARM_2 + 1),#0x00
	mov	dpl,_f0
	mov	dph,(_f0 + 1)
	lcall	__modsint
	mov	r6,dpl
	mov	_TL0,r6
;	main.c:66: TR0=1;
;	assignBit
	setb	_TR0
;	main.c:67: while (1) {
00102$:
;	main.c:69: }
	sjmp	00102$
	.area CSEG    (CODE)
	.area CONST   (CODE)
_SPIN:
	.byte #0x03,#0x00	;  3
	.byte #0x06,#0x00	;  6
	.byte #0x0c,#0x00	;  12
	.byte #0x09,#0x00	;  9
	.area XINIT   (CODE)
	.area CABS    (ABS,CODE)
