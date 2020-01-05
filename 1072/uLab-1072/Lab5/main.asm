;--------------------------------------------------------
; File Created by SDCC : free open source ANSI-C Compiler
; Version 3.8.0 #10562 (MINGW64)
;--------------------------------------------------------
	.module main
	.optsdcc -mmcs51 --model-small
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _music
	.globl _main
	.globl _init
	.globl _timer1
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
	.globl _table_index
	.globl _counter
	.globl _table
	.globl _isSound
	.globl _music_index
	.globl _timer1_count
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
	.area REG_BANK_2	(REL,OVR,DATA)
	.ds 8
;--------------------------------------------------------
; internal ram data
;--------------------------------------------------------
	.area DSEG    (DATA)
_timer1_count::
	.ds 2
_music_index::
	.ds 1
_isSound::
	.ds 2
_table::
	.ds 32
_counter::
	.ds 1
_table_index::
	.ds 1
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
	.ds	5
	reti
	.ds	7
	ljmp	_timer1
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
;	main.c:9: int table[16] = {262, 294, 330, 349, 392, 440, 494};
	mov	(_table + 0),#0x06
	mov	(_table + 1),#0x01
	mov	((_table + 0x0002) + 0),#0x26
	mov	((_table + 0x0002) + 1),#0x01
	mov	((_table + 0x0004) + 0),#0x4a
	mov	((_table + 0x0004) + 1),#0x01
	mov	((_table + 0x0006) + 0),#0x5d
	mov	((_table + 0x0006) + 1),#0x01
	mov	((_table + 0x0008) + 0),#0x88
	mov	((_table + 0x0008) + 1),#0x01
	mov	((_table + 0x000a) + 0),#0xb8
	mov	((_table + 0x000a) + 1),#0x01
	mov	((_table + 0x000c) + 0),#0xee
	mov	((_table + 0x000c) + 1),#0x01
;	main.c:18: char counter = 0;
	mov	_counter,#0x00
;	main.c:19: char table_index=0;
	mov	_table_index,#0x00
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
;	main.c:21: void timer_isr (void) __interrupt (1) __using (1) {
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
	push	dpl
	push	dph
	push	psw
	mov	psw,#0x08
;	main.c:23: TH0  = (PERIOD-table[music[music_index]-1]) >> 8;
	mov	a,_music_index
	mov	dptr,#_music
	movc	a,@a+dptr
	mov	r7,a
	dec	r7
	mov	a,r7
	add	a,r7
	add	a,#_table
	mov	r1,a
	mov	ar6,@r1
	inc	r1
	mov	ar7,@r1
	mov	ar2,r6
	mov	a,r7
	mov	r3,a
	rlc	a
	subb	a,acc
	mov	r4,a
	mov	r5,a
	clr	a
	clr	c
	subb	a,r2
	clr	a
	subb	a,r3
	mov	r3,a
	mov	a,#0x01
	subb	a,r4
	clr	a
	subb	a,r5
	mov	_TH0,r3
;	main.c:24: TL0  = (PERIOD-table[music[music_index]-1]) & 0xff;
	clr	c
	clr	a
	subb	a,r6
	mov	r6,a
	mov	_TL0,r6
;	main.c:30: counter++;
	inc	_counter
;	main.c:31: }
	pop	psw
	pop	dph
	pop	dpl
	pop	acc
	reti
;	eliminated unneeded push/pop b
;------------------------------------------------------------
;Allocation info for local variables in function 'timer1'
;------------------------------------------------------------
;	main.c:32: void timer1 (void) __interrupt (3) __using (2) {
;	-----------------------------------------
;	 function timer1
;	-----------------------------------------
_timer1:
	ar7 = 0x17
	ar6 = 0x16
	ar5 = 0x15
	ar4 = 0x14
	ar3 = 0x13
	ar2 = 0x12
	ar1 = 0x11
	ar0 = 0x10
	push	acc
	push	psw
;	main.c:33: TH1  = INIT_TIME >> 8;
	mov	_TH1,#0x0b
;	main.c:34: TL1  = INIT_TIME & 0xff;
	mov	_TL1,#0xdc
;	main.c:35: timer1_count++;
	inc	_timer1_count
	clr	a
	cjne	a,_timer1_count,00103$
	inc	(_timer1_count + 1)
00103$:
;	main.c:36: }
	pop	psw
	pop	acc
	reti
;	eliminated unneeded mov psw,# (no regs used in bank)
;	eliminated unneeded push/pop dpl
;	eliminated unneeded push/pop dph
;	eliminated unneeded push/pop b
;------------------------------------------------------------
;Allocation info for local variables in function 'init'
;------------------------------------------------------------
;tmp                       Allocated to registers r2 r3 r4 r5 
;i                         Allocated to registers r6 r7 
;i                         Allocated to registers r6 r7 
;------------------------------------------------------------
;	main.c:37: void init(){
;	-----------------------------------------
;	 function init
;	-----------------------------------------
_init:
	ar7 = 0x07
	ar6 = 0x06
	ar5 = 0x05
	ar4 = 0x04
	ar3 = 0x03
	ar2 = 0x02
	ar1 = 0x01
	ar0 = 0x00
;	main.c:38: music_index=0;
	mov	_music_index,#0x00
;	main.c:39: timer1_count=-1;
	mov	_timer1_count,#0xff
	mov	(_timer1_count + 1),#0xff
;	main.c:41: for(int i=7;i<16;i++){
	mov	r6,#0x07
	mov	r7,#0x00
00104$:
	clr	c
	mov	a,r6
	subb	a,#0x10
	mov	a,r7
	xrl	a,#0x80
	subb	a,#0x80
	jnc	00101$
;	main.c:42: table[i]=table[i-7]*2;
	mov	a,r6
	add	a,r6
	mov	r4,a
	mov	a,r7
	rlc	a
	mov	a,r4
	add	a,#_table
	mov	r1,a
	mov	ar5,r6
	mov	a,r5
	add	a,#0xf9
	add	a,acc
	add	a,#_table
	mov	r0,a
	mov	ar4,@r0
	inc	r0
	mov	ar5,@r0
	dec	r0
	mov	a,r4
	add	a,r4
	mov	r4,a
	mov	a,r5
	rlc	a
	mov	r5,a
	mov	@r1,ar4
	inc	r1
	mov	@r1,ar5
	dec	r1
;	main.c:41: for(int i=7;i<16;i++){
	inc	r6
	cjne	r6,#0x00,00104$
	inc	r7
	sjmp	00104$
00101$:
;	main.c:44: for(int i=0;i<16;i++){
	mov	r6,#0x00
	mov	r7,#0x00
00107$:
	clr	c
	mov	a,r6
	subb	a,#0x10
	mov	a,r7
	xrl	a,#0x80
	subb	a,#0x80
	jc	00131$
	ret
00131$:
;	main.c:45: tmp=1.0/table[i]*1000000;
	mov	a,r6
	add	a,r6
	mov	r4,a
	mov	a,r7
	rlc	a
	mov	a,r4
	add	a,#_table
	mov	r1,a
	mov	dpl,@r1
	inc	r1
	mov	dph,@r1
	dec	r1
	push	ar7
	push	ar6
	push	ar1
	lcall	___sint2fs
	mov	r2,dpl
	mov	r3,dph
	mov	r4,b
	mov	r5,a
	push	ar2
	push	ar3
	push	ar4
	push	ar5
	mov	dptr,#0x0000
	mov	b,#0x80
	mov	a,#0x3f
	lcall	___fsdiv
	mov	r2,dpl
	mov	r3,dph
	mov	r4,b
	mov	r5,a
	mov	a,sp
	add	a,#0xfc
	mov	sp,a
	push	ar2
	push	ar3
	push	ar4
	push	ar5
	mov	dptr,#0x2400
	mov	b,#0x74
	mov	a,#0x49
	lcall	___fsmul
	mov	r2,dpl
	mov	r3,dph
	mov	r4,b
	mov	r5,a
	mov	a,sp
	add	a,#0xfc
	mov	sp,a
;	main.c:46: table[i]=tmp;
	mov	dpl,r2
	mov	dph,r3
	mov	b,r4
	mov	a,r5
	lcall	___fs2sint
	mov	a,dpl
	mov	b,dph
	pop	ar1
	pop	ar6
	pop	ar7
	mov	@r1,a
	inc	r1
	mov	@r1,b
	dec	r1
;	main.c:44: for(int i=0;i<16;i++){
	inc	r6
	cjne	r6,#0x00,00132$
	inc	r7
00132$:
;	main.c:48: }
	ljmp	00107$
;------------------------------------------------------------
;Allocation info for local variables in function 'main'
;------------------------------------------------------------
;	main.c:49: int main(){
;	-----------------------------------------
;	 function main
;	-----------------------------------------
_main:
;	main.c:50: init();
	lcall	_init
;	main.c:51: TMOD = 0b00010001;
	mov	_TMOD,#0x11
;	main.c:52: IE   = 0x8A;
	mov	_IE,#0x8a
;	main.c:53: TR0  = 1;
;	assignBit
	setb	_TR0
;	main.c:54: TR1  = 1;
;	assignBit
	setb	_TR1
;	main.c:55: TH0  = PERIOD >> 8;
	mov	_TH0,#0x00
;	main.c:56: TL0  = PERIOD & 0xff;
	mov	_TL0,#0x00
;	main.c:57: P2_7=0;
;	assignBit
	clr	_P2_7
;	main.c:58: isSound=1;
	mov	_isSound,#0x01
	mov	(_isSound + 1),#0x00
;	main.c:59: while (1){
00110$:
;	main.c:60: EA = 0;
;	assignBit
	clr	_EA
;	main.c:61: if (counter == 1 ) {
	mov	a,#0x01
	cjne	a,_counter,00104$
;	main.c:62: counter = 0;
	mov	_counter,#0x00
;	main.c:63: if(music[music_index]!=16)
	mov	a,_music_index
	mov	dptr,#_music
	movc	a,@a+dptr
	mov	r7,a
	cjne	r7,#0x10,00136$
	sjmp	00104$
00136$:
;	main.c:64: P2_7=!P2_7;
	cpl	_P2_7
00104$:
;	main.c:66: if(timer1_count == 10){
	mov	a,#0x0a
	cjne	a,_timer1_count,00137$
	clr	a
	cjne	a,(_timer1_count + 1),00137$
	sjmp	00138$
00137$:
	sjmp	00108$
00138$:
;	main.c:67: music_index++;
	inc	_music_index
;	main.c:68: timer1_count=0;
	clr	a
	mov	_timer1_count,a
	mov	(_timer1_count + 1),a
;	main.c:69: if(music_index == 96)
	mov	a,#0x60
	cjne	a,_music_index,00108$
;	main.c:70: music_index = 0;
	mov	_music_index,#0x00
00108$:
;	main.c:72: EA = 1;
;	assignBit
	setb	_EA
;	main.c:74: return 0;
;	main.c:75: }
	sjmp	00110$
	.area CSEG    (CODE)
	.area CONST   (CODE)
_music:
	.db #0x0a	; 10
	.db #0x0a	; 10
	.db #0x0a	; 10
	.db #0x0a	; 10
	.db #0x09	; 9
	.db #0x08	; 8
	.db #0x08	; 8
	.db #0x07	; 7
	.db #0x06	; 6
	.db #0x06	; 6
	.db #0x08	; 8
	.db #0x0a	; 10
	.db #0x0d	; 13
	.db #0x0d	; 13
	.db #0x0d	; 13
	.db #0x0d	; 13
	.db #0x0c	; 12
	.db #0x0b	; 11
	.db #0x0b	; 11
	.db #0x0a	; 10
	.db #0x09	; 9
	.db #0x09	; 9
	.db #0x0a	; 10
	.db #0x0b	; 11
	.db #0x0a	; 10
	.db #0x0b	; 11
	.db #0x0a	; 10
	.db #0x0c	; 12
	.db #0x0b	; 11
	.db #0x0a	; 10
	.db #0x0a	; 10
	.db #0x09	; 9
	.db #0x08	; 8
	.db #0x08	; 8
	.db #0x07	; 7
	.db #0x06	; 6
	.db #0x07	; 7
	.db #0x07	; 7
	.db #0x07	; 7
	.db #0x07	; 7
	.db #0x08	; 8
	.db #0x07	; 7
	.db #0x06	; 6
	.db #0x10	; 16
	.db #0x10	; 16
	.db #0x06	; 6
	.db #0x10	; 16
	.db #0x10	; 16
	.db #0x0a	; 10
	.db #0x0a	; 10
	.db #0x0a	; 10
	.db #0x0a	; 10
	.db #0x09	; 9
	.db #0x08	; 8
	.db #0x08	; 8
	.db #0x07	; 7
	.db #0x07	; 7
	.db #0x07	; 7
	.db #0x07	; 7
	.db #0x07	; 7
	.db #0x0d	; 13
	.db #0x0d	; 13
	.db #0x0d	; 13
	.db #0x0d	; 13
	.db #0x0e	; 14
	.db #0x0d	; 13
	.db #0x0d	; 13
	.db #0x0c	; 12
	.db #0x0c	; 12
	.db #0x0c	; 12
	.db #0x0d	; 13
	.db #0x0e	; 14
	.db #0x0f	; 15
	.db #0x0f	; 15
	.db #0x0f	; 15
	.db #0x0f	; 15
	.db #0x0e	; 14
	.db #0x0e	; 14
	.db #0x0d	; 13
	.db #0x0d	; 13
	.db #0x0d	; 13
	.db #0x0d	; 13
	.db #0x0c	; 12
	.db #0x0b	; 11
	.db #0x0a	; 10
	.db #0x0a	; 10
	.db #0x0a	; 10
	.db #0x0a	; 10
	.db #0x0b	; 11
	.db #0x09	; 9
	.db #0x08	; 8
	.db #0x10	; 16
	.db #0x10	; 16
	.db #0x08	; 8
	.db #0x10	; 16
	.db #0x10	; 16
	.area XINIT   (CODE)
	.area CABS    (ABS,CODE)
