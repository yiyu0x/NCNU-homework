;--------------------------------------------------------
; File Created by SDCC : free open source ANSI-C Compiler
; Version 3.8.0 #10562 (MINGW64)
;--------------------------------------------------------
	.module main
	.optsdcc -mmcs51 --model-small
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _main
	.globl _display
	.globl _delay
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
	.globl _cc
	.globl _dc
	.globl _t
	.globl _counter
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
_counter::
	.ds 2
_t::
	.ds 2
_dc::
	.ds 2
_cc::
	.ds 2
;--------------------------------------------------------
; overlayable items in internal ram 
;--------------------------------------------------------
	.area	OSEG    (OVR,DATA)
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
;	main.c:4: unsigned int counter = 0;
	clr	a
	mov	_counter,a
	mov	(_counter + 1),a
;	main.c:5: int t  = 0;
	mov	_t,a
	mov	(_t + 1),a
;	main.c:6: int dc = 0x70; // 十位
	mov	_dc,#0x70
;	1-genFromRTrack replaced	mov	(_dc + 1),#0x00
	mov	(_dc + 1),a
;	main.c:7: int cc = 0xb0; // 個位
	mov	_cc,#0xb0
;	1-genFromRTrack replaced	mov	(_cc + 1),#0x00
	mov	(_cc + 1),a
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
;	main.c:8: void timer_isr (void) __interrupt (1) __using (1) {
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
	push	psw
;	main.c:9: TH0  = PERIOD >> 8;
	mov	_TH0,#0x3c
;	main.c:10: TL0  = PERIOD & 0xff;
	mov	_TL0,#0xb0
;	main.c:11: counter++;
	inc	_counter
	clr	a
	cjne	a,_counter,00103$
	inc	(_counter + 1)
00103$:
;	main.c:12: }
	pop	psw
	pop	acc
	reti
;	eliminated unneeded mov psw,# (no regs used in bank)
;	eliminated unneeded push/pop dpl
;	eliminated unneeded push/pop dph
;	eliminated unneeded push/pop b
;------------------------------------------------------------
;Allocation info for local variables in function 'delay'
;------------------------------------------------------------
;i                         Allocated to registers r6 r7 
;------------------------------------------------------------
;	main.c:14: void delay() {
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
;	main.c:15: for(int i = 0; i < 1500; i++);
	mov	r6,#0x00
	mov	r7,#0x00
00103$:
	clr	c
	mov	a,r6
	subb	a,#0xdc
	mov	a,r7
	xrl	a,#0x80
	subb	a,#0x85
	jnc	00105$
	inc	r6
	cjne	r6,#0x00,00103$
	inc	r7
	sjmp	00103$
00105$:
;	main.c:16: }
	ret
;------------------------------------------------------------
;Allocation info for local variables in function 'display'
;------------------------------------------------------------
;	main.c:17: void display() {
;	-----------------------------------------
;	 function display
;	-----------------------------------------
_display:
;	main.c:18: if(t) P0 = dc;
	mov	a,_t
	orl	a,(_t + 1)
	jz	00102$
	mov	_P0,_dc
	sjmp	00103$
00102$:
;	main.c:19: else  P0 = cc;
	mov	_P0,_cc
00103$:
;	main.c:20: if (t == 0) t = 1;
	mov	a,_t
	orl	a,(_t + 1)
	jnz	00105$
	mov	_t,#0x01
	mov	(_t + 1),a
	sjmp	00106$
00105$:
;	main.c:21: else t = 0;			
	clr	a
	mov	_t,a
	mov	(_t + 1),a
00106$:
;	main.c:22: delay();
;	main.c:23: }
	ljmp	_delay
;------------------------------------------------------------
;Allocation info for local variables in function 'main'
;------------------------------------------------------------
;	main.c:25: int main(){
;	-----------------------------------------
;	 function main
;	-----------------------------------------
_main:
;	main.c:26: P0   = 0x30;
	mov	_P0,#0x30
;	main.c:27: TMOD = 0b00000001;
	mov	_TMOD,#0x01
;	main.c:28: IE   = 0x82;
	mov	_IE,#0x82
;	main.c:29: TR0  = 1;
;	assignBit
	setb	_TR0
;	main.c:30: TH0  = PERIOD >> 8;
	mov	_TH0,#0x3c
;	main.c:31: TL0  = PERIOD & 0xff;
	mov	_TL0,#0xb0
;	main.c:32: while (1){
00109$:
;	main.c:33: EA = 0;
;	assignBit
	clr	_EA
;	main.c:34: if (counter == 10) {
	mov	a,#0x0a
	cjne	a,_counter,00133$
	clr	a
	cjne	a,(_counter + 1),00133$
	sjmp	00134$
00133$:
	sjmp	00107$
00134$:
;	main.c:35: counter = 0;
	clr	a
	mov	_counter,a
	mov	(_counter + 1),a
;	main.c:36: cc++;
	inc	_cc
;	genFromRTrack removed	clr	a
	cjne	a,_cc,00135$
	inc	(_cc + 1)
00135$:
;	main.c:37: if(dc == 0x79 && cc == 0xba){
	mov	a,#0x79
	cjne	a,_dc,00136$
	clr	a
	cjne	a,(_dc + 1),00136$
	sjmp	00137$
00136$:
	sjmp	00102$
00137$:
	mov	a,#0xba
	cjne	a,_cc,00138$
	clr	a
	cjne	a,(_cc + 1),00138$
	sjmp	00139$
00138$:
	sjmp	00102$
00139$:
;	main.c:38: dc = 0x70;
	mov	_dc,#0x70
	mov	(_dc + 1),#0x00
;	main.c:39: cc = 0xb0;
	mov	_cc,#0xb0
	mov	(_cc + 1),#0x00
00102$:
;	main.c:41: if(cc == 0xba){
	mov	a,#0xba
	cjne	a,_cc,00140$
	clr	a
	cjne	a,(_cc + 1),00140$
	sjmp	00141$
00140$:
	sjmp	00107$
00141$:
;	main.c:42: cc = 0xb0;
	mov	_cc,#0xb0
	mov	(_cc + 1),#0x00
;	main.c:43: dc++;
	inc	_dc
	clr	a
	cjne	a,_dc,00142$
	inc	(_dc + 1)
00142$:
00107$:
;	main.c:46: EA = 1;
;	assignBit
	setb	_EA
;	main.c:47: display();
	lcall	_display
;	main.c:49: return 0;
;	main.c:50: }
	sjmp	00109$
	.area CSEG    (CODE)
	.area CONST   (CODE)
	.area XINIT   (CODE)
	.area CABS    (ABS,CODE)
