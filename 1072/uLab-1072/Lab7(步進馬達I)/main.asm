;--------------------------------------------------------
; File Created by SDCC : free open source ANSI-C Compiler
; Version 3.8.0 #10562 (MINGW64)
;--------------------------------------------------------
	.module main
	.optsdcc -mmcs51 --model-small
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _LED_Display_PARM_2
	.globl _SPIN
	.globl _main
	.globl _LED_Display
	.globl _keyPressed
	.globl _timer_isr
	.globl _delay
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
_main_table_65537_51:
	.ds 8
_main_num_65537_51:
	.ds 8
_main_row_65537_51:
	.ds 2
_main_cnt_65538_52:
	.ds 2
_main_previous_65538_52:
	.ds 2
_main_previous2_65538_52:
	.ds 2
;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
	.area	OSEG    (OVR,DATA)
	.area	OSEG    (OVR,DATA)
_keyPressed_row_65536_38:
	.ds 2
	.area	OSEG    (OVR,DATA)
_LED_Display_PARM_2:
	.ds 3
_LED_Display_table_65536_44:
	.ds 3
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
;	main.c:5: int count=50; // 一圈200步
	mov	_count,#0x32
	mov	(_count + 1),#0x00
;	main.c:6: int max=50;
	mov	_max,#0x32
	mov	(_max + 1),#0x00
;	main.c:7: char direct=0; 
	mov	_direct,#0x00
;	main.c:8: unsigned char step=0x01; 
	mov	_step,#0x01
;	main.c:9: unsigned int speed=(65536-30000);
	mov	_speed,#0xd0
	mov	(_speed + 1),#0x8a
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
;Allocation info for local variables in function 'delay'
;------------------------------------------------------------
;time                      Allocated to registers r6 r7 
;i                         Allocated to registers r4 r5 
;j                         Allocated to registers r2 r3 
;------------------------------------------------------------
;	main.c:10: void delay(unsigned int time)
;	-----------------------------------------
;	 function delay
;	-----------------------------------------
_delay:
	ar7 = 0x07
	ar6 = 0x06
	ar5 = 0x05
	ar4 = 0x04
	ar3 = 0x03
	ar2 = 0x02
	ar1 = 0x01
	ar0 = 0x00
	mov	r6,dpl
	mov	r7,dph
;	main.c:13: for(i=0;i<time;i++)    
	mov	r4,#0x00
	mov	r5,#0x00
00107$:
	clr	c
	mov	a,r4
	subb	a,r6
	mov	a,r5
	subb	a,r7
	jnc	00109$
;	main.c:14: for(j=0;j<1275;j++);
	mov	r2,#0xfb
	mov	r3,#0x04
00105$:
	mov	a,r2
	add	a,#0xff
	mov	r0,a
	mov	a,r3
	addc	a,#0xff
	mov	r1,a
	mov	ar2,r0
	mov	ar3,r1
	mov	a,r0
	orl	a,r1
	jnz	00105$
;	main.c:13: for(i=0;i<time;i++)    
	inc	r4
	cjne	r4,#0x00,00107$
	inc	r5
	sjmp	00107$
00109$:
;	main.c:15: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'timer_isr'
;------------------------------------------------------------
;	main.c:16: void timer_isr (void) __interrupt (1) __using (1) {	//timer 0 interrupt 訊號		using register bank 1
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
	push	acc
	push	b
	push	psw
	mov	psw,#0x08
;	main.c:17: TH0=speed/256; 
	mov	r6,(_speed + 1)
	mov	_TH0,r6
;	main.c:18: TL0=speed%16; 
	mov	a,#0x0f
	anl	a,_speed
	mov	r6,a
	mov	r7,#0x00
	mov	_TL0,r6
;	main.c:20: if(direct==0) { 
	mov	a,_direct
	jnz	00106$
;	main.c:21: step>>=1; 
	mov	a,_step
	clr	c
	rrc	a
;	main.c:22: if(step==0x00) step=0x08;
	mov	_step,a
	jnz	00102$
	mov	_step,#0x08
00102$:
;	main.c:23: P0&=0xf0; 
	anl	_P0,#0xf0
;	main.c:24: P0|=step; 
	mov	a,_step
	orl	_P0,a
	sjmp	00107$
00106$:
;	main.c:27: step<<=1; 
	mov	a,_step
	mov	r7,a
	add	a,acc
	mov	_step,a
;	main.c:28: if(step==0x10) 
	mov	a,#0x10
	cjne	a,_step,00104$
;	main.c:29: step=0x01;
	mov	_step,#0x01
00104$:
;	main.c:30: P0&=0xf0; 
	anl	_P0,#0xf0
;	main.c:31: P0|=step; 
	mov	a,_step
	orl	_P0,a
00107$:
;	main.c:33: if(--count<=0){
	dec	_count
	mov	a,#0xff
	cjne	a,_count,00132$
	dec	(_count + 1)
00132$:
	clr	c
	clr	a
	subb	a,_count
	mov	a,#(0x00 ^ 0x80)
	mov	b,(_count + 1)
	xrl	b,#0x80
	subb	a,b
	jc	00110$
;	main.c:34: TR0=0;
;	assignBit
	clr	_TR0
00110$:
;	main.c:36: }
	pop	psw
	pop	b
	pop	acc
	reti
;	eliminated unneeded push/pop dpl
;	eliminated unneeded push/pop dph
;------------------------------------------------------------
;Allocation info for local variables in function 'keyPressed'
;------------------------------------------------------------
;row                       Allocated with name '_keyPressed_row_65536_38'
;c                         Allocated to registers r4 r5 
;col                       Allocated to registers r2 r3 
;magic                     Allocated to registers r7 r6 
;------------------------------------------------------------
;	main.c:38: short keyPressed(short row) {
;	-----------------------------------------
;	 function keyPressed
;	-----------------------------------------
_keyPressed:
	ar7 = 0x07
	ar6 = 0x06
	ar5 = 0x05
	ar4 = 0x04
	ar3 = 0x03
	ar2 = 0x02
	ar1 = 0x01
	ar0 = 0x00
	mov	_keyPressed_row_65536_38,dpl
	mov	(_keyPressed_row_65536_38 + 1),dph
;	main.c:39: if((P2 & 0b11110000) != 0b11110000){	//if 按下按鈕
	mov	r4,_P2
	anl	ar4,#0xf0
	mov	r5,#0x00
	cjne	r4,#0xf0,00127$
	cjne	r5,#0x00,00127$
	sjmp	00105$
00127$:
;	main.c:40: for (short c = 1, col = 0; col < 4; c *= 2, col++) {
	mov	r4,#0x01
	mov	r5,#0x00
	mov	r2,#0x00
	mov	r3,#0x00
	mov	r0,#0x00
	mov	r1,#0x00
00107$:
	clr	c
	mov	a,r0
	subb	a,#0x04
	mov	a,r1
	xrl	a,#0x80
	subb	a,#0x80
	jnc	00105$
;	main.c:42: `			short magic = ((P2 >> 4) ^ 0b11111111) & 0b00001111;
	mov	a,_P2
	swap	a
	anl	a,#0x0f
	mov	r7,a
	xrl	ar7,#0xff
	anl	ar7,#0x0f
	mov	r6,#0x00
;	main.c:43: if (magic == c) {
	mov	a,r7
	cjne	a,ar4,00108$
	mov	a,r6
	cjne	a,ar5,00108$
;	main.c:44: return col * 4 + row;
	mov	a,r2
	add	a,r2
	mov	r6,a
	mov	a,r3
	rlc	a
	mov	r7,a
	mov	a,r6
	add	a,r6
	mov	r6,a
	mov	a,r7
	rlc	a
	mov	r7,a
	mov	a,_keyPressed_row_65536_38
	add	a,r6
	mov	dpl,a
	mov	a,(_keyPressed_row_65536_38 + 1)
	addc	a,r7
	mov	dph,a
	ret
00108$:
;	main.c:40: for (short c = 1, col = 0; col < 4; c *= 2, col++) {
	mov	a,r4
	add	a,r4
	mov	r4,a
	mov	a,r5
	rlc	a
	mov	r5,a
	inc	r0
	cjne	r0,#0x00,00131$
	inc	r1
00131$:
	mov	ar2,r0
	mov	ar3,r1
	sjmp	00107$
00105$:
;	main.c:48: return -1;	//沒按 return -1
	mov	dptr,#0xffff
;	main.c:49: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'LED_Display'
;------------------------------------------------------------
;num                       Allocated with name '_LED_Display_PARM_2'
;table                     Allocated with name '_LED_Display_table_65536_44'
;i                         Allocated to registers r3 r4 
;j                         Allocated to registers r6 r7 
;------------------------------------------------------------
;	main.c:50: void LED_Display(short table[], short num[]) {
;	-----------------------------------------
;	 function LED_Display
;	-----------------------------------------
_LED_Display:
	mov	_LED_Display_table_65536_44,dpl
	mov	(_LED_Display_table_65536_44 + 1),dph
	mov	(_LED_Display_table_65536_44 + 2),b
;	main.c:51: for(short i = 0; i < 4; i++) {
	mov	r3,#0x00
	mov	r4,#0x00
00107$:
	clr	c
	mov	a,r3
	subb	a,#0x04
	mov	a,r4
	xrl	a,#0x80
	subb	a,#0x80
	jnc	00109$
;	main.c:52: P1  = table[i] + num[i];
	mov	a,r3
	add	a,r3
	mov	r1,a
	mov	a,r4
	rlc	a
	mov	r2,a
	mov	a,r1
	add	a,_LED_Display_table_65536_44
	mov	r0,a
	mov	a,r2
	addc	a,(_LED_Display_table_65536_44 + 1)
	mov	r6,a
	mov	r7,(_LED_Display_table_65536_44 + 2)
	mov	dpl,r0
	mov	dph,r6
	mov	b,r7
	lcall	__gptrget
	mov	r0,a
	mov	a,r1
	add	a,_LED_Display_PARM_2
	mov	r1,a
	mov	a,r2
	addc	a,(_LED_Display_PARM_2 + 1)
	mov	r2,a
	mov	r7,(_LED_Display_PARM_2 + 2)
	mov	dpl,r1
	mov	dph,r2
	mov	b,r7
	lcall	__gptrget
	add	a,r0
	mov	_P1,a
;	main.c:53: for(int j = 0; j < 1000; j++){}
	mov	r6,#0x00
	mov	r7,#0x00
00104$:
	clr	c
	mov	a,r6
	subb	a,#0xe8
	mov	a,r7
	xrl	a,#0x80
	subb	a,#0x83
	jnc	00108$
	inc	r6
	cjne	r6,#0x00,00104$
	inc	r7
	sjmp	00104$
00108$:
;	main.c:51: for(short i = 0; i < 4; i++) {
	inc	r3
	cjne	r3,#0x00,00107$
	inc	r4
	sjmp	00107$
00109$:
;	main.c:55: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'main'
;------------------------------------------------------------
;table                     Allocated with name '_main_table_65537_51'
;num                       Allocated with name '_main_num_65537_51'
;row                       Allocated with name '_main_row_65537_51'
;cnt                       Allocated with name '_main_cnt_65538_52'
;previous                  Allocated with name '_main_previous_65538_52'
;previous2                 Allocated with name '_main_previous2_65538_52'
;key                       Allocated to registers r2 r3 
;------------------------------------------------------------
;	main.c:57: int main(){
;	-----------------------------------------
;	 function main
;	-----------------------------------------
_main:
;	main.c:58: IE=0x82;
	mov	_IE,#0x82
;	main.c:59: TMOD=0x01;
	mov	_TMOD,#0x01
;	main.c:60: TH0=speed/256;
	mov	r6,(_speed + 1)
	mov	_TH0,r6
;	main.c:61: TL0=speed%16;
	mov	a,#0x0f
	anl	a,_speed
	mov	r6,a
	mov	r7,#0x00
	mov	_TL0,r6
;	main.c:63: short table[4] = {0x70, 0xb0, 0xd0, 0xe0};
	mov	(_main_table_65537_51 + 0),#0x70
;	1-genFromRTrack replaced	mov	(_main_table_65537_51 + 1),#0x00
	mov	(_main_table_65537_51 + 1),r7
	mov	((_main_table_65537_51 + 0x0002) + 0),#0xb0
;	1-genFromRTrack replaced	mov	((_main_table_65537_51 + 0x0002) + 1),#0x00
	mov	((_main_table_65537_51 + 0x0002) + 1),r7
	mov	((_main_table_65537_51 + 0x0004) + 0),#0xd0
;	1-genFromRTrack replaced	mov	((_main_table_65537_51 + 0x0004) + 1),#0x00
	mov	((_main_table_65537_51 + 0x0004) + 1),r7
	mov	((_main_table_65537_51 + 0x0006) + 0),#0xe0
;	1-genFromRTrack replaced	mov	((_main_table_65537_51 + 0x0006) + 1),#0x00
	mov	((_main_table_65537_51 + 0x0006) + 1),r7
;	main.c:64: int num[4] = {0,0,0,0};
	clr	a
	mov	(_main_num_65537_51 + 0),a
	mov	(_main_num_65537_51 + 1),a
	mov	((_main_num_65537_51 + 0x0002) + 0),a
	mov	((_main_num_65537_51 + 0x0002) + 1),a
	mov	((_main_num_65537_51 + 0x0004) + 0),a
	mov	((_main_num_65537_51 + 0x0004) + 1),a
	mov	((_main_num_65537_51 + 0x0006) + 0),a
	mov	((_main_num_65537_51 + 0x0006) + 1),a
;	main.c:65: short row = 0;
	mov	_main_row_65537_51,a
	mov	(_main_row_65537_51 + 1),a
;	main.c:66: P2=0b11111110;
	mov	_P2,#0xfe
;	main.c:67: short cnt = 1;
	mov	_main_cnt_65538_52,#0x01
;	1-genFromRTrack replaced	mov	(_main_cnt_65538_52 + 1),#0x00
	mov	(_main_cnt_65538_52 + 1),a
;	main.c:69: short previous = -1;
	mov	_main_previous_65538_52,#0xff
	mov	(_main_previous_65538_52 + 1),#0xff
;	main.c:70: short previous2=-1;
	mov	_main_previous2_65538_52,#0xff
	mov	(_main_previous2_65538_52 + 1),#0xff
;	main.c:71: while (1) {
00115$:
;	main.c:72: P2    =cnt^0b11111111;
	mov	a,#0xff
	xrl	a,_main_cnt_65538_52
	mov	r2,a
	mov	_P2,r2
;	main.c:73: cnt *=2; //shift
	mov	a,_main_cnt_65538_52
	add	a,_main_cnt_65538_52
	mov	_main_cnt_65538_52,a
	mov	a,(_main_cnt_65538_52 + 1)
	rlc	a
	mov	(_main_cnt_65538_52 + 1),a
;	main.c:74: short key = keyPressed(row);
	mov	dpl,_main_row_65537_51
	mov	dph,(_main_row_65537_51 + 1)
	lcall	_keyPressed
	mov	r2,dpl
	mov	r3,dph
;	main.c:75: if (key != -1 && key != previous && key!=10 && key!=11) {	//有按且不等於上一按 => 處理debounce
	cjne	r2,#0xff,00155$
	cjne	r3,#0xff,00155$
	sjmp	00102$
00155$:
	mov	a,r2
	cjne	a,_main_previous_65538_52,00156$
	mov	a,r3
	cjne	a,(_main_previous_65538_52 + 1),00156$
	sjmp	00102$
00156$:
	cjne	r2,#0x0a,00157$
	cjne	r3,#0x00,00157$
	sjmp	00102$
00157$:
	cjne	r2,#0x0b,00158$
	cjne	r3,#0x00,00158$
	sjmp	00102$
00158$:
;	main.c:76: previous = key;
	mov	_main_previous_65538_52,r2
	mov	(_main_previous_65538_52 + 1),r3
;	main.c:77: previous2=key;
	mov	_main_previous2_65538_52,r2
	mov	(_main_previous2_65538_52 + 1),r3
;	main.c:78: num[0] =num[1];
	mov	r6,((_main_num_65537_51 + 0x0002) + 0)
	mov	r7,((_main_num_65537_51 + 0x0002) + 1)
	mov	(_main_num_65537_51 + 0),r6
	mov	(_main_num_65537_51 + 1),r7
;	main.c:79: num[1] =num[2];
	mov	r6,((_main_num_65537_51 + 0x0004) + 0)
	mov	r7,((_main_num_65537_51 + 0x0004) + 1)
	mov	((_main_num_65537_51 + 0x0002) + 0),r6
	mov	((_main_num_65537_51 + 0x0002) + 1),r7
;	main.c:80: num[2] =num[3];			
	mov	r6,((_main_num_65537_51 + 0x0006) + 0)
	mov	r7,((_main_num_65537_51 + 0x0006) + 1)
	mov	((_main_num_65537_51 + 0x0004) + 0),r6
	mov	((_main_num_65537_51 + 0x0004) + 1),r7
;	main.c:81: num[3] = key;	//往前推
	mov	((_main_num_65537_51 + 0x0006) + 0),r2
	mov	((_main_num_65537_51 + 0x0006) + 1),r3
00102$:
;	main.c:84: if((key==10 || key==11)&& previous2!=key){	//debounce!
	cjne	r2,#0x0a,00159$
	cjne	r3,#0x00,00159$
	sjmp	00111$
00159$:
	cjne	r2,#0x0b,00160$
	cjne	r3,#0x00,00160$
	sjmp	00161$
00160$:
	ljmp	00109$
00161$:
00111$:
	mov	a,r2
	cjne	a,_main_previous2_65538_52,00162$
	mov	a,r3
	cjne	a,(_main_previous2_65538_52 + 1),00162$
	ljmp	00109$
00162$:
;	main.c:85: previous2= key;
	mov	_main_previous2_65538_52,r2
	mov	(_main_previous2_65538_52 + 1),r3
;	main.c:86: count=(num[1]*100+num[2]*10+num[3])/360.0*200.0;
	mov	__mulint_PARM_2,((_main_num_65537_51 + 0x0002) + 0)
	mov	(__mulint_PARM_2 + 1),((_main_num_65537_51 + 0x0002) + 1)
	mov	dptr,#0x0064
	push	ar3
	push	ar2
	lcall	__mulint
	mov	r6,dpl
	mov	r7,dph
	pop	ar2
	pop	ar3
	mov	__mulint_PARM_2,((_main_num_65537_51 + 0x0004) + 0)
	mov	(__mulint_PARM_2 + 1),((_main_num_65537_51 + 0x0004) + 1)
	mov	dptr,#0x000a
	push	ar7
	push	ar6
	push	ar3
	push	ar2
	lcall	__mulint
	mov	r4,dpl
	mov	r5,dph
	pop	ar2
	pop	ar3
	pop	ar6
	pop	ar7
	mov	a,r4
	add	a,r6
	mov	r6,a
	mov	a,r5
	addc	a,r7
	mov	r7,a
	mov	a,(_main_num_65537_51 + 0x0006)
	add	a,r6
	mov	dpl,a
	mov	a,((_main_num_65537_51 + 0x0006) + 1)
	addc	a,r7
	mov	dph,a
	push	ar3
	push	ar2
	lcall	___sint2fs
	mov	r4,dpl
	mov	r5,dph
	mov	r6,b
	mov	r7,a
	clr	a
	push	acc
	push	acc
	mov	a,#0xb4
	push	acc
	mov	a,#0x43
	push	acc
	mov	dpl,r4
	mov	dph,r5
	mov	b,r6
	mov	a,r7
	lcall	___fsdiv
	mov	r4,dpl
	mov	r5,dph
	mov	r6,b
	mov	r7,a
	mov	a,sp
	add	a,#0xfc
	mov	sp,a
	push	ar4
	push	ar5
	push	ar6
	push	ar7
	mov	dptr,#0x0000
	mov	b,#0x48
	mov	a,#0x43
	lcall	___fsmul
	mov	r4,dpl
	mov	r5,dph
	mov	r6,b
	mov	r7,a
	mov	a,sp
	add	a,#0xfc
	mov	sp,a
	mov	dpl,r4
	mov	dph,r5
	mov	b,r6
	mov	a,r7
	lcall	___fs2sint
	mov	_count,dpl
	mov	(_count + 1),dph
	pop	ar2
	pop	ar3
;	main.c:87: num[0]=0,num[1]=0,num[2]=0,num[3]=0;
	clr	a
	mov	(_main_num_65537_51 + 0),a
	mov	(_main_num_65537_51 + 1),a
	mov	((_main_num_65537_51 + 0x0002) + 0),a
	mov	((_main_num_65537_51 + 0x0002) + 1),a
	mov	((_main_num_65537_51 + 0x0004) + 0),a
	mov	((_main_num_65537_51 + 0x0004) + 1),a
	mov	((_main_num_65537_51 + 0x0006) + 0),a
	mov	((_main_num_65537_51 + 0x0006) + 1),a
;	main.c:88: direct=0;
;	1-genFromRTrack replaced	mov	_direct,#0x00
	mov	_direct,a
;	main.c:89: if(key==11)
	cjne	r2,#0x0b,00107$
	cjne	r3,#0x00,00107$
;	main.c:90: direct=1;
	mov	_direct,#0x01
00107$:
;	main.c:91: TR0=1;
;	assignBit
	setb	_TR0
00109$:
;	main.c:93: row++;
	inc	_main_row_65537_51
	clr	a
	cjne	a,_main_row_65537_51,00165$
	inc	(_main_row_65537_51 + 1)
00165$:
;	main.c:94: if (cnt == 0x10) {	//用cnt從上往下掃 
	mov	a,#0x10
	cjne	a,_main_cnt_65538_52,00166$
	clr	a
	cjne	a,(_main_cnt_65538_52 + 1),00166$
	sjmp	00167$
00166$:
	sjmp	00113$
00167$:
;	main.c:95: cnt = 1;
	mov	_main_cnt_65538_52,#0x01
;	main.c:96: row = 0;
	clr	a
	mov	(_main_cnt_65538_52 + 1),a
	mov	_main_row_65537_51,a
	mov	(_main_row_65537_51 + 1),a
00113$:
;	main.c:98: LED_Display(table,num);
	mov	_LED_Display_PARM_2,#_main_num_65537_51
	mov	(_LED_Display_PARM_2 + 1),#0x00
	mov	(_LED_Display_PARM_2 + 2),#0x40
	mov	dptr,#_main_table_65537_51
	mov	b,#0x40
	lcall	_LED_Display
;	main.c:100: }
	ljmp	00115$
	.area CSEG    (CODE)
	.area CONST   (CODE)
_SPIN:
	.byte #0x03,#0x00	;  3
	.byte #0x06,#0x00	;  6
	.byte #0x0c,#0x00	;  12
	.byte #0x09,#0x00	;  9
	.area XINIT   (CODE)
	.area CABS    (ABS,CODE)
