;--------------------------------------------------------
; File Created by SDCC : free open source ANSI-C Compiler
; Version 3.8.0 #10562 (MINGW64)
;--------------------------------------------------------
	.module Lab3_main
	.optsdcc -mmcs51 --model-small
	
;--------------------------------------------------------
; Public variables in this module
;--------------------------------------------------------
	.globl _main
	.globl _keyPressed
	.globl _LED_Display
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
;--------------------------------------------------------
; internal ram data
;--------------------------------------------------------
	.area DSEG    (DATA)
_main_table_65536_3:
	.ds 8
_main_num_65536_3:
	.ds 8
_main_row_65536_3:
	.ds 2
_main_previous_65537_4:
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
;Allocation info for local variables in function 'main'
;------------------------------------------------------------
;table                     Allocated with name '_main_table_65536_3'
;num                       Allocated with name '_main_num_65536_3'
;row                       Allocated with name '_main_row_65536_3'
;count                     Allocated to registers r4 r5 
;number                    Allocated to registers 
;previous                  Allocated with name '_main_previous_65537_4'
;key                       Allocated to registers r2 r3 
;------------------------------------------------------------
;	Lab3-main.c:5: int main() {
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
;	Lab3-main.c:6: short table[4] = {0x70, 0xb0, 0xd0, 0xe0};
	mov	(_main_table_65536_3 + 0),#0x70
	mov	(_main_table_65536_3 + 1),#0x00
	mov	((_main_table_65536_3 + 0x0002) + 0),#0xb0
	mov	((_main_table_65536_3 + 0x0002) + 1),#0x00
	mov	((_main_table_65536_3 + 0x0004) + 0),#0xd0
	mov	((_main_table_65536_3 + 0x0004) + 1),#0x00
	mov	((_main_table_65536_3 + 0x0006) + 0),#0xe0
	mov	((_main_table_65536_3 + 0x0006) + 1),#0x00
;	Lab3-main.c:7: short num[4] = {15, 15, 15, 15};
	mov	(_main_num_65536_3 + 0),#0x0f
	mov	(_main_num_65536_3 + 1),#0x00
	mov	((_main_num_65536_3 + 0x0002) + 0),#0x0f
	mov	((_main_num_65536_3 + 0x0002) + 1),#0x00
	mov	((_main_num_65536_3 + 0x0004) + 0),#0x0f
	mov	((_main_num_65536_3 + 0x0004) + 1),#0x00
	mov	((_main_num_65536_3 + 0x0006) + 0),#0x0f
;	Lab3-main.c:8: short row = 0;
	clr	a
	mov	((_main_num_65536_3 + 0x0006) + 1),a
	mov	_main_row_65536_3,a
	mov	(_main_row_65536_3 + 1),a
;	Lab3-main.c:9: P2=0b11111110;
	mov	_P2,#0xfe
;	Lab3-main.c:10: short count = 1;
	mov	r4,#0x01
	mov	r5,#0x00
;	Lab3-main.c:12: short previous = -1;
	mov	_main_previous_65537_4,#0xff
	mov	(_main_previous_65537_4 + 1),#0xff
;	Lab3-main.c:13: while (1) {
00107$:
;	Lab3-main.c:14: P2    =count^0b11111111;
	mov	a,#0xff
	xrl	a,r4
	mov	r2,a
	mov	ar3,r5
	mov	_P2,r2
;	Lab3-main.c:15: count *=2;
	mov	a,r4
	add	a,r4
	mov	r4,a
	mov	a,r5
	rlc	a
	mov	r5,a
;	Lab3-main.c:16: short key = keyPressed(row);
	mov	dpl,_main_row_65536_3
	mov	dph,(_main_row_65536_3 + 1)
	push	ar5
	push	ar4
	lcall	_keyPressed
	mov	r2,dpl
	mov	r3,dph
	pop	ar4
	pop	ar5
;	Lab3-main.c:17: if (key != -1 && key != previous) {
	cjne	r2,#0xff,00127$
	cjne	r3,#0xff,00127$
	sjmp	00102$
00127$:
	mov	a,r2
	cjne	a,_main_previous_65537_4,00128$
	mov	a,r3
	cjne	a,(_main_previous_65537_4 + 1),00128$
	sjmp	00102$
00128$:
;	Lab3-main.c:18: previous = key;
	mov	_main_previous_65537_4,r2
	mov	(_main_previous_65537_4 + 1),r3
;	Lab3-main.c:19: num[0] =num[1];
	mov	r6,((_main_num_65536_3 + 0x0002) + 0)
	mov	r7,((_main_num_65536_3 + 0x0002) + 1)
	mov	(_main_num_65536_3 + 0),r6
	mov	(_main_num_65536_3 + 1),r7
;	Lab3-main.c:20: num[1] =num[2];
	mov	r6,((_main_num_65536_3 + 0x0004) + 0)
	mov	r7,((_main_num_65536_3 + 0x0004) + 1)
	mov	((_main_num_65536_3 + 0x0002) + 0),r6
	mov	((_main_num_65536_3 + 0x0002) + 1),r7
;	Lab3-main.c:21: num[2] =num[3];			
	mov	r6,((_main_num_65536_3 + 0x0006) + 0)
	mov	r7,((_main_num_65536_3 + 0x0006) + 1)
	mov	((_main_num_65536_3 + 0x0004) + 0),r6
	mov	((_main_num_65536_3 + 0x0004) + 1),r7
;	Lab3-main.c:22: num[3] = key;
	mov	((_main_num_65536_3 + 0x0006) + 0),r2
	mov	((_main_num_65536_3 + 0x0006) + 1),r3
00102$:
;	Lab3-main.c:24: row++;
	inc	_main_row_65536_3
	clr	a
	cjne	a,_main_row_65536_3,00129$
	inc	(_main_row_65536_3 + 1)
00129$:
;	Lab3-main.c:25: if (count == 0x10) {
	cjne	r4,#0x10,00105$
	cjne	r5,#0x00,00105$
;	Lab3-main.c:26: count = 1;
	mov	r4,#0x01
;	Lab3-main.c:27: row   = 0;
	clr	a
	mov	r5,a
	mov	_main_row_65536_3,a
	mov	(_main_row_65536_3 + 1),a
00105$:
;	Lab3-main.c:29: LED_Display(table,num);
	mov	_LED_Display_PARM_2,#_main_num_65536_3
	mov	(_LED_Display_PARM_2 + 1),#0x00
	mov	(_LED_Display_PARM_2 + 2),#0x40
	mov	dptr,#_main_table_65536_3
	mov	b,#0x40
	push	ar5
	push	ar4
	lcall	_LED_Display
	pop	ar4
	pop	ar5
;	Lab3-main.c:31: }
	ljmp	00107$
	.area CSEG    (CODE)
	.area CONST   (CODE)
	.area XINIT   (CODE)
	.area CABS    (ABS,CODE)
