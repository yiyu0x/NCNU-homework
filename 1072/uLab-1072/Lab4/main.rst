                                      1 ;--------------------------------------------------------
                                      2 ; File Created by SDCC : free open source ANSI-C Compiler
                                      3 ; Version 3.8.0 #10562 (MINGW64)
                                      4 ;--------------------------------------------------------
                                      5 	.module main
                                      6 	.optsdcc -mmcs51 --model-small
                                      7 	
                                      8 ;--------------------------------------------------------
                                      9 ; Public variables in this module
                                     10 ;--------------------------------------------------------
                                     11 	.globl _main
                                     12 	.globl _display
                                     13 	.globl _delay
                                     14 	.globl _timer_isr
                                     15 	.globl _CY
                                     16 	.globl _AC
                                     17 	.globl _F0
                                     18 	.globl _RS1
                                     19 	.globl _RS0
                                     20 	.globl _OV
                                     21 	.globl _F1
                                     22 	.globl _P
                                     23 	.globl _PS
                                     24 	.globl _PT1
                                     25 	.globl _PX1
                                     26 	.globl _PT0
                                     27 	.globl _PX0
                                     28 	.globl _RD
                                     29 	.globl _WR
                                     30 	.globl _T1
                                     31 	.globl _T0
                                     32 	.globl _INT1
                                     33 	.globl _INT0
                                     34 	.globl _TXD
                                     35 	.globl _RXD
                                     36 	.globl _P3_7
                                     37 	.globl _P3_6
                                     38 	.globl _P3_5
                                     39 	.globl _P3_4
                                     40 	.globl _P3_3
                                     41 	.globl _P3_2
                                     42 	.globl _P3_1
                                     43 	.globl _P3_0
                                     44 	.globl _EA
                                     45 	.globl _ES
                                     46 	.globl _ET1
                                     47 	.globl _EX1
                                     48 	.globl _ET0
                                     49 	.globl _EX0
                                     50 	.globl _P2_7
                                     51 	.globl _P2_6
                                     52 	.globl _P2_5
                                     53 	.globl _P2_4
                                     54 	.globl _P2_3
                                     55 	.globl _P2_2
                                     56 	.globl _P2_1
                                     57 	.globl _P2_0
                                     58 	.globl _SM0
                                     59 	.globl _SM1
                                     60 	.globl _SM2
                                     61 	.globl _REN
                                     62 	.globl _TB8
                                     63 	.globl _RB8
                                     64 	.globl _TI
                                     65 	.globl _RI
                                     66 	.globl _P1_7
                                     67 	.globl _P1_6
                                     68 	.globl _P1_5
                                     69 	.globl _P1_4
                                     70 	.globl _P1_3
                                     71 	.globl _P1_2
                                     72 	.globl _P1_1
                                     73 	.globl _P1_0
                                     74 	.globl _TF1
                                     75 	.globl _TR1
                                     76 	.globl _TF0
                                     77 	.globl _TR0
                                     78 	.globl _IE1
                                     79 	.globl _IT1
                                     80 	.globl _IE0
                                     81 	.globl _IT0
                                     82 	.globl _P0_7
                                     83 	.globl _P0_6
                                     84 	.globl _P0_5
                                     85 	.globl _P0_4
                                     86 	.globl _P0_3
                                     87 	.globl _P0_2
                                     88 	.globl _P0_1
                                     89 	.globl _P0_0
                                     90 	.globl _B
                                     91 	.globl _ACC
                                     92 	.globl _PSW
                                     93 	.globl _IP
                                     94 	.globl _P3
                                     95 	.globl _IE
                                     96 	.globl _P2
                                     97 	.globl _SBUF
                                     98 	.globl _SCON
                                     99 	.globl _P1
                                    100 	.globl _TH1
                                    101 	.globl _TH0
                                    102 	.globl _TL1
                                    103 	.globl _TL0
                                    104 	.globl _TMOD
                                    105 	.globl _TCON
                                    106 	.globl _PCON
                                    107 	.globl _DPH
                                    108 	.globl _DPL
                                    109 	.globl _SP
                                    110 	.globl _P0
                                    111 	.globl _cc
                                    112 	.globl _dc
                                    113 	.globl _t
                                    114 	.globl _counter
                                    115 ;--------------------------------------------------------
                                    116 ; special function registers
                                    117 ;--------------------------------------------------------
                                    118 	.area RSEG    (ABS,DATA)
      000000                        119 	.org 0x0000
                           000080   120 _P0	=	0x0080
                           000081   121 _SP	=	0x0081
                           000082   122 _DPL	=	0x0082
                           000083   123 _DPH	=	0x0083
                           000087   124 _PCON	=	0x0087
                           000088   125 _TCON	=	0x0088
                           000089   126 _TMOD	=	0x0089
                           00008A   127 _TL0	=	0x008a
                           00008B   128 _TL1	=	0x008b
                           00008C   129 _TH0	=	0x008c
                           00008D   130 _TH1	=	0x008d
                           000090   131 _P1	=	0x0090
                           000098   132 _SCON	=	0x0098
                           000099   133 _SBUF	=	0x0099
                           0000A0   134 _P2	=	0x00a0
                           0000A8   135 _IE	=	0x00a8
                           0000B0   136 _P3	=	0x00b0
                           0000B8   137 _IP	=	0x00b8
                           0000D0   138 _PSW	=	0x00d0
                           0000E0   139 _ACC	=	0x00e0
                           0000F0   140 _B	=	0x00f0
                                    141 ;--------------------------------------------------------
                                    142 ; special function bits
                                    143 ;--------------------------------------------------------
                                    144 	.area RSEG    (ABS,DATA)
      000000                        145 	.org 0x0000
                           000080   146 _P0_0	=	0x0080
                           000081   147 _P0_1	=	0x0081
                           000082   148 _P0_2	=	0x0082
                           000083   149 _P0_3	=	0x0083
                           000084   150 _P0_4	=	0x0084
                           000085   151 _P0_5	=	0x0085
                           000086   152 _P0_6	=	0x0086
                           000087   153 _P0_7	=	0x0087
                           000088   154 _IT0	=	0x0088
                           000089   155 _IE0	=	0x0089
                           00008A   156 _IT1	=	0x008a
                           00008B   157 _IE1	=	0x008b
                           00008C   158 _TR0	=	0x008c
                           00008D   159 _TF0	=	0x008d
                           00008E   160 _TR1	=	0x008e
                           00008F   161 _TF1	=	0x008f
                           000090   162 _P1_0	=	0x0090
                           000091   163 _P1_1	=	0x0091
                           000092   164 _P1_2	=	0x0092
                           000093   165 _P1_3	=	0x0093
                           000094   166 _P1_4	=	0x0094
                           000095   167 _P1_5	=	0x0095
                           000096   168 _P1_6	=	0x0096
                           000097   169 _P1_7	=	0x0097
                           000098   170 _RI	=	0x0098
                           000099   171 _TI	=	0x0099
                           00009A   172 _RB8	=	0x009a
                           00009B   173 _TB8	=	0x009b
                           00009C   174 _REN	=	0x009c
                           00009D   175 _SM2	=	0x009d
                           00009E   176 _SM1	=	0x009e
                           00009F   177 _SM0	=	0x009f
                           0000A0   178 _P2_0	=	0x00a0
                           0000A1   179 _P2_1	=	0x00a1
                           0000A2   180 _P2_2	=	0x00a2
                           0000A3   181 _P2_3	=	0x00a3
                           0000A4   182 _P2_4	=	0x00a4
                           0000A5   183 _P2_5	=	0x00a5
                           0000A6   184 _P2_6	=	0x00a6
                           0000A7   185 _P2_7	=	0x00a7
                           0000A8   186 _EX0	=	0x00a8
                           0000A9   187 _ET0	=	0x00a9
                           0000AA   188 _EX1	=	0x00aa
                           0000AB   189 _ET1	=	0x00ab
                           0000AC   190 _ES	=	0x00ac
                           0000AF   191 _EA	=	0x00af
                           0000B0   192 _P3_0	=	0x00b0
                           0000B1   193 _P3_1	=	0x00b1
                           0000B2   194 _P3_2	=	0x00b2
                           0000B3   195 _P3_3	=	0x00b3
                           0000B4   196 _P3_4	=	0x00b4
                           0000B5   197 _P3_5	=	0x00b5
                           0000B6   198 _P3_6	=	0x00b6
                           0000B7   199 _P3_7	=	0x00b7
                           0000B0   200 _RXD	=	0x00b0
                           0000B1   201 _TXD	=	0x00b1
                           0000B2   202 _INT0	=	0x00b2
                           0000B3   203 _INT1	=	0x00b3
                           0000B4   204 _T0	=	0x00b4
                           0000B5   205 _T1	=	0x00b5
                           0000B6   206 _WR	=	0x00b6
                           0000B7   207 _RD	=	0x00b7
                           0000B8   208 _PX0	=	0x00b8
                           0000B9   209 _PT0	=	0x00b9
                           0000BA   210 _PX1	=	0x00ba
                           0000BB   211 _PT1	=	0x00bb
                           0000BC   212 _PS	=	0x00bc
                           0000D0   213 _P	=	0x00d0
                           0000D1   214 _F1	=	0x00d1
                           0000D2   215 _OV	=	0x00d2
                           0000D3   216 _RS0	=	0x00d3
                           0000D4   217 _RS1	=	0x00d4
                           0000D5   218 _F0	=	0x00d5
                           0000D6   219 _AC	=	0x00d6
                           0000D7   220 _CY	=	0x00d7
                                    221 ;--------------------------------------------------------
                                    222 ; overlayable register banks
                                    223 ;--------------------------------------------------------
                                    224 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                        225 	.ds 8
                                    226 	.area REG_BANK_1	(REL,OVR,DATA)
      000008                        227 	.ds 8
                                    228 ;--------------------------------------------------------
                                    229 ; internal ram data
                                    230 ;--------------------------------------------------------
                                    231 	.area DSEG    (DATA)
      000010                        232 _counter::
      000010                        233 	.ds 2
      000012                        234 _t::
      000012                        235 	.ds 2
      000014                        236 _dc::
      000014                        237 	.ds 2
      000016                        238 _cc::
      000016                        239 	.ds 2
                                    240 ;--------------------------------------------------------
                                    241 ; overlayable items in internal ram 
                                    242 ;--------------------------------------------------------
                                    243 	.area	OSEG    (OVR,DATA)
                                    244 ;--------------------------------------------------------
                                    245 ; Stack segment in internal ram 
                                    246 ;--------------------------------------------------------
                                    247 	.area	SSEG
      000018                        248 __start__stack:
      000018                        249 	.ds	1
                                    250 
                                    251 ;--------------------------------------------------------
                                    252 ; indirectly addressable internal ram data
                                    253 ;--------------------------------------------------------
                                    254 	.area ISEG    (DATA)
                                    255 ;--------------------------------------------------------
                                    256 ; absolute internal ram data
                                    257 ;--------------------------------------------------------
                                    258 	.area IABS    (ABS,DATA)
                                    259 	.area IABS    (ABS,DATA)
                                    260 ;--------------------------------------------------------
                                    261 ; bit data
                                    262 ;--------------------------------------------------------
                                    263 	.area BSEG    (BIT)
                                    264 ;--------------------------------------------------------
                                    265 ; paged external ram data
                                    266 ;--------------------------------------------------------
                                    267 	.area PSEG    (PAG,XDATA)
                                    268 ;--------------------------------------------------------
                                    269 ; external ram data
                                    270 ;--------------------------------------------------------
                                    271 	.area XSEG    (XDATA)
                                    272 ;--------------------------------------------------------
                                    273 ; absolute external ram data
                                    274 ;--------------------------------------------------------
                                    275 	.area XABS    (ABS,XDATA)
                                    276 ;--------------------------------------------------------
                                    277 ; external initialized ram data
                                    278 ;--------------------------------------------------------
                                    279 	.area XISEG   (XDATA)
                                    280 	.area HOME    (CODE)
                                    281 	.area GSINIT0 (CODE)
                                    282 	.area GSINIT1 (CODE)
                                    283 	.area GSINIT2 (CODE)
                                    284 	.area GSINIT3 (CODE)
                                    285 	.area GSINIT4 (CODE)
                                    286 	.area GSINIT5 (CODE)
                                    287 	.area GSINIT  (CODE)
                                    288 	.area GSFINAL (CODE)
                                    289 	.area CSEG    (CODE)
                                    290 ;--------------------------------------------------------
                                    291 ; interrupt vector 
                                    292 ;--------------------------------------------------------
                                    293 	.area HOME    (CODE)
      000000                        294 __interrupt_vect:
      000000 02 00 11         [24]  295 	ljmp	__sdcc_gsinit_startup
      000003 32               [24]  296 	reti
      000004                        297 	.ds	7
      00000B 02 00 80         [24]  298 	ljmp	_timer_isr
                                    299 ;--------------------------------------------------------
                                    300 ; global & static initialisations
                                    301 ;--------------------------------------------------------
                                    302 	.area HOME    (CODE)
                                    303 	.area GSINIT  (CODE)
                                    304 	.area GSFINAL (CODE)
                                    305 	.area GSINIT  (CODE)
                                    306 	.globl __sdcc_gsinit_startup
                                    307 	.globl __sdcc_program_startup
                                    308 	.globl __start__stack
                                    309 	.globl __mcs51_genXINIT
                                    310 	.globl __mcs51_genXRAMCLEAR
                                    311 	.globl __mcs51_genRAMCLEAR
                                    312 ;	main.c:4: unsigned int counter = 0;
      00006A E4               [12]  313 	clr	a
      00006B F5 10            [12]  314 	mov	_counter,a
      00006D F5 11            [12]  315 	mov	(_counter + 1),a
                                    316 ;	main.c:5: int t  = 0;
      00006F F5 12            [12]  317 	mov	_t,a
      000071 F5 13            [12]  318 	mov	(_t + 1),a
                                    319 ;	main.c:6: int dc = 0x70; // 十位
      000073 75 14 70         [24]  320 	mov	_dc,#0x70
                                    321 ;	1-genFromRTrack replaced	mov	(_dc + 1),#0x00
      000076 F5 15            [12]  322 	mov	(_dc + 1),a
                                    323 ;	main.c:7: int cc = 0xb0; // 個位
      000078 75 16 B0         [24]  324 	mov	_cc,#0xb0
                                    325 ;	1-genFromRTrack replaced	mov	(_cc + 1),#0x00
      00007B F5 17            [12]  326 	mov	(_cc + 1),a
                                    327 	.area GSFINAL (CODE)
      00007D 02 00 0E         [24]  328 	ljmp	__sdcc_program_startup
                                    329 ;--------------------------------------------------------
                                    330 ; Home
                                    331 ;--------------------------------------------------------
                                    332 	.area HOME    (CODE)
                                    333 	.area HOME    (CODE)
      00000E                        334 __sdcc_program_startup:
      00000E 02 00 D1         [24]  335 	ljmp	_main
                                    336 ;	return from main will return to caller
                                    337 ;--------------------------------------------------------
                                    338 ; code
                                    339 ;--------------------------------------------------------
                                    340 	.area CSEG    (CODE)
                                    341 ;------------------------------------------------------------
                                    342 ;Allocation info for local variables in function 'timer_isr'
                                    343 ;------------------------------------------------------------
                                    344 ;	main.c:8: void timer_isr (void) __interrupt (1) __using (1) {
                                    345 ;	-----------------------------------------
                                    346 ;	 function timer_isr
                                    347 ;	-----------------------------------------
      000080                        348 _timer_isr:
                           00000F   349 	ar7 = 0x0f
                           00000E   350 	ar6 = 0x0e
                           00000D   351 	ar5 = 0x0d
                           00000C   352 	ar4 = 0x0c
                           00000B   353 	ar3 = 0x0b
                           00000A   354 	ar2 = 0x0a
                           000009   355 	ar1 = 0x09
                           000008   356 	ar0 = 0x08
      000080 C0 E0            [24]  357 	push	acc
      000082 C0 D0            [24]  358 	push	psw
                                    359 ;	main.c:9: TH0  = PERIOD >> 8;
      000084 75 8C 3C         [24]  360 	mov	_TH0,#0x3c
                                    361 ;	main.c:10: TL0  = PERIOD & 0xff;
      000087 75 8A B0         [24]  362 	mov	_TL0,#0xb0
                                    363 ;	main.c:11: counter++;
      00008A 05 10            [12]  364 	inc	_counter
      00008C E4               [12]  365 	clr	a
      00008D B5 10 02         [24]  366 	cjne	a,_counter,00103$
      000090 05 11            [12]  367 	inc	(_counter + 1)
      000092                        368 00103$:
                                    369 ;	main.c:12: }
      000092 D0 D0            [24]  370 	pop	psw
      000094 D0 E0            [24]  371 	pop	acc
      000096 32               [24]  372 	reti
                                    373 ;	eliminated unneeded mov psw,# (no regs used in bank)
                                    374 ;	eliminated unneeded push/pop dpl
                                    375 ;	eliminated unneeded push/pop dph
                                    376 ;	eliminated unneeded push/pop b
                                    377 ;------------------------------------------------------------
                                    378 ;Allocation info for local variables in function 'delay'
                                    379 ;------------------------------------------------------------
                                    380 ;i                         Allocated to registers r6 r7 
                                    381 ;------------------------------------------------------------
                                    382 ;	main.c:14: void delay() {
                                    383 ;	-----------------------------------------
                                    384 ;	 function delay
                                    385 ;	-----------------------------------------
      000097                        386 _delay:
                           000007   387 	ar7 = 0x07
                           000006   388 	ar6 = 0x06
                           000005   389 	ar5 = 0x05
                           000004   390 	ar4 = 0x04
                           000003   391 	ar3 = 0x03
                           000002   392 	ar2 = 0x02
                           000001   393 	ar1 = 0x01
                           000000   394 	ar0 = 0x00
                                    395 ;	main.c:15: for(int i = 0; i < 1500; i++);
      000097 7E 00            [12]  396 	mov	r6,#0x00
      000099 7F 00            [12]  397 	mov	r7,#0x00
      00009B                        398 00103$:
      00009B C3               [12]  399 	clr	c
      00009C EE               [12]  400 	mov	a,r6
      00009D 94 DC            [12]  401 	subb	a,#0xdc
      00009F EF               [12]  402 	mov	a,r7
      0000A0 64 80            [12]  403 	xrl	a,#0x80
      0000A2 94 85            [12]  404 	subb	a,#0x85
      0000A4 50 07            [24]  405 	jnc	00105$
      0000A6 0E               [12]  406 	inc	r6
      0000A7 BE 00 F1         [24]  407 	cjne	r6,#0x00,00103$
      0000AA 0F               [12]  408 	inc	r7
      0000AB 80 EE            [24]  409 	sjmp	00103$
      0000AD                        410 00105$:
                                    411 ;	main.c:16: }
      0000AD 22               [24]  412 	ret
                                    413 ;------------------------------------------------------------
                                    414 ;Allocation info for local variables in function 'display'
                                    415 ;------------------------------------------------------------
                                    416 ;	main.c:17: void display() {
                                    417 ;	-----------------------------------------
                                    418 ;	 function display
                                    419 ;	-----------------------------------------
      0000AE                        420 _display:
                                    421 ;	main.c:18: if(t) P0 = dc;
      0000AE E5 12            [12]  422 	mov	a,_t
      0000B0 45 13            [12]  423 	orl	a,(_t + 1)
      0000B2 60 05            [24]  424 	jz	00102$
      0000B4 85 14 80         [24]  425 	mov	_P0,_dc
      0000B7 80 03            [24]  426 	sjmp	00103$
      0000B9                        427 00102$:
                                    428 ;	main.c:19: else  P0 = cc;
      0000B9 85 16 80         [24]  429 	mov	_P0,_cc
      0000BC                        430 00103$:
                                    431 ;	main.c:20: if (t == 0) t = 1;
      0000BC E5 12            [12]  432 	mov	a,_t
      0000BE 45 13            [12]  433 	orl	a,(_t + 1)
      0000C0 70 07            [24]  434 	jnz	00105$
      0000C2 75 12 01         [24]  435 	mov	_t,#0x01
      0000C5 F5 13            [12]  436 	mov	(_t + 1),a
      0000C7 80 05            [24]  437 	sjmp	00106$
      0000C9                        438 00105$:
                                    439 ;	main.c:21: else t = 0;			
      0000C9 E4               [12]  440 	clr	a
      0000CA F5 12            [12]  441 	mov	_t,a
      0000CC F5 13            [12]  442 	mov	(_t + 1),a
      0000CE                        443 00106$:
                                    444 ;	main.c:22: delay();
                                    445 ;	main.c:23: }
      0000CE 02 00 97         [24]  446 	ljmp	_delay
                                    447 ;------------------------------------------------------------
                                    448 ;Allocation info for local variables in function 'main'
                                    449 ;------------------------------------------------------------
                                    450 ;	main.c:25: int main(){
                                    451 ;	-----------------------------------------
                                    452 ;	 function main
                                    453 ;	-----------------------------------------
      0000D1                        454 _main:
                                    455 ;	main.c:26: P0   = 0x30;
      0000D1 75 80 30         [24]  456 	mov	_P0,#0x30
                                    457 ;	main.c:27: TMOD = 0b00000001;
      0000D4 75 89 01         [24]  458 	mov	_TMOD,#0x01
                                    459 ;	main.c:28: IE   = 0x82;
      0000D7 75 A8 82         [24]  460 	mov	_IE,#0x82
                                    461 ;	main.c:29: TR0  = 1;
                                    462 ;	assignBit
      0000DA D2 8C            [12]  463 	setb	_TR0
                                    464 ;	main.c:30: TH0  = PERIOD >> 8;
      0000DC 75 8C 3C         [24]  465 	mov	_TH0,#0x3c
                                    466 ;	main.c:31: TL0  = PERIOD & 0xff;
      0000DF 75 8A B0         [24]  467 	mov	_TL0,#0xb0
                                    468 ;	main.c:32: while (1){
      0000E2                        469 00109$:
                                    470 ;	main.c:33: EA = 0;
                                    471 ;	assignBit
      0000E2 C2 AF            [12]  472 	clr	_EA
                                    473 ;	main.c:34: if (counter == 10) {
      0000E4 74 0A            [12]  474 	mov	a,#0x0a
      0000E6 B5 10 06         [24]  475 	cjne	a,_counter,00133$
      0000E9 E4               [12]  476 	clr	a
      0000EA B5 11 02         [24]  477 	cjne	a,(_counter + 1),00133$
      0000ED 80 02            [24]  478 	sjmp	00134$
      0000EF                        479 00133$:
      0000EF 80 4D            [24]  480 	sjmp	00107$
      0000F1                        481 00134$:
                                    482 ;	main.c:35: counter = 0;
      0000F1 E4               [12]  483 	clr	a
      0000F2 F5 10            [12]  484 	mov	_counter,a
      0000F4 F5 11            [12]  485 	mov	(_counter + 1),a
                                    486 ;	main.c:36: cc++;
      0000F6 05 16            [12]  487 	inc	_cc
                                    488 ;	genFromRTrack removed	clr	a
      0000F8 B5 16 02         [24]  489 	cjne	a,_cc,00135$
      0000FB 05 17            [12]  490 	inc	(_cc + 1)
      0000FD                        491 00135$:
                                    492 ;	main.c:37: if(dc == 0x79 && cc == 0xba){
      0000FD 74 79            [12]  493 	mov	a,#0x79
      0000FF B5 14 06         [24]  494 	cjne	a,_dc,00136$
      000102 E4               [12]  495 	clr	a
      000103 B5 15 02         [24]  496 	cjne	a,(_dc + 1),00136$
      000106 80 02            [24]  497 	sjmp	00137$
      000108                        498 00136$:
      000108 80 19            [24]  499 	sjmp	00102$
      00010A                        500 00137$:
      00010A 74 BA            [12]  501 	mov	a,#0xba
      00010C B5 16 06         [24]  502 	cjne	a,_cc,00138$
      00010F E4               [12]  503 	clr	a
      000110 B5 17 02         [24]  504 	cjne	a,(_cc + 1),00138$
      000113 80 02            [24]  505 	sjmp	00139$
      000115                        506 00138$:
      000115 80 0C            [24]  507 	sjmp	00102$
      000117                        508 00139$:
                                    509 ;	main.c:38: dc = 0x70;
      000117 75 14 70         [24]  510 	mov	_dc,#0x70
      00011A 75 15 00         [24]  511 	mov	(_dc + 1),#0x00
                                    512 ;	main.c:39: cc = 0xb0;
      00011D 75 16 B0         [24]  513 	mov	_cc,#0xb0
      000120 75 17 00         [24]  514 	mov	(_cc + 1),#0x00
      000123                        515 00102$:
                                    516 ;	main.c:41: if(cc == 0xba){
      000123 74 BA            [12]  517 	mov	a,#0xba
      000125 B5 16 06         [24]  518 	cjne	a,_cc,00140$
      000128 E4               [12]  519 	clr	a
      000129 B5 17 02         [24]  520 	cjne	a,(_cc + 1),00140$
      00012C 80 02            [24]  521 	sjmp	00141$
      00012E                        522 00140$:
      00012E 80 0E            [24]  523 	sjmp	00107$
      000130                        524 00141$:
                                    525 ;	main.c:42: cc = 0xb0;
      000130 75 16 B0         [24]  526 	mov	_cc,#0xb0
      000133 75 17 00         [24]  527 	mov	(_cc + 1),#0x00
                                    528 ;	main.c:43: dc++;
      000136 05 14            [12]  529 	inc	_dc
      000138 E4               [12]  530 	clr	a
      000139 B5 14 02         [24]  531 	cjne	a,_dc,00142$
      00013C 05 15            [12]  532 	inc	(_dc + 1)
      00013E                        533 00142$:
      00013E                        534 00107$:
                                    535 ;	main.c:46: EA = 1;
                                    536 ;	assignBit
      00013E D2 AF            [12]  537 	setb	_EA
                                    538 ;	main.c:47: display();
      000140 12 00 AE         [24]  539 	lcall	_display
                                    540 ;	main.c:49: return 0;
                                    541 ;	main.c:50: }
      000143 80 9D            [24]  542 	sjmp	00109$
                                    543 	.area CSEG    (CODE)
                                    544 	.area CONST   (CODE)
                                    545 	.area XINIT   (CODE)
                                    546 	.area CABS    (ABS,CODE)
