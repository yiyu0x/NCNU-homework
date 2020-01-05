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
                                     11 	.globl _SPIN
                                     12 	.globl _main
                                     13 	.globl _timer_isr
                                     14 	.globl _CY
                                     15 	.globl _AC
                                     16 	.globl _F0
                                     17 	.globl _RS1
                                     18 	.globl _RS0
                                     19 	.globl _OV
                                     20 	.globl _F1
                                     21 	.globl _P
                                     22 	.globl _PS
                                     23 	.globl _PT1
                                     24 	.globl _PX1
                                     25 	.globl _PT0
                                     26 	.globl _PX0
                                     27 	.globl _RD
                                     28 	.globl _WR
                                     29 	.globl _T1
                                     30 	.globl _T0
                                     31 	.globl _INT1
                                     32 	.globl _INT0
                                     33 	.globl _TXD
                                     34 	.globl _RXD
                                     35 	.globl _P3_7
                                     36 	.globl _P3_6
                                     37 	.globl _P3_5
                                     38 	.globl _P3_4
                                     39 	.globl _P3_3
                                     40 	.globl _P3_2
                                     41 	.globl _P3_1
                                     42 	.globl _P3_0
                                     43 	.globl _EA
                                     44 	.globl _ES
                                     45 	.globl _ET1
                                     46 	.globl _EX1
                                     47 	.globl _ET0
                                     48 	.globl _EX0
                                     49 	.globl _P2_7
                                     50 	.globl _P2_6
                                     51 	.globl _P2_5
                                     52 	.globl _P2_4
                                     53 	.globl _P2_3
                                     54 	.globl _P2_2
                                     55 	.globl _P2_1
                                     56 	.globl _P2_0
                                     57 	.globl _SM0
                                     58 	.globl _SM1
                                     59 	.globl _SM2
                                     60 	.globl _REN
                                     61 	.globl _TB8
                                     62 	.globl _RB8
                                     63 	.globl _TI
                                     64 	.globl _RI
                                     65 	.globl _P1_7
                                     66 	.globl _P1_6
                                     67 	.globl _P1_5
                                     68 	.globl _P1_4
                                     69 	.globl _P1_3
                                     70 	.globl _P1_2
                                     71 	.globl _P1_1
                                     72 	.globl _P1_0
                                     73 	.globl _TF1
                                     74 	.globl _TR1
                                     75 	.globl _TF0
                                     76 	.globl _TR0
                                     77 	.globl _IE1
                                     78 	.globl _IT1
                                     79 	.globl _IE0
                                     80 	.globl _IT0
                                     81 	.globl _P0_7
                                     82 	.globl _P0_6
                                     83 	.globl _P0_5
                                     84 	.globl _P0_4
                                     85 	.globl _P0_3
                                     86 	.globl _P0_2
                                     87 	.globl _P0_1
                                     88 	.globl _P0_0
                                     89 	.globl _B
                                     90 	.globl _ACC
                                     91 	.globl _PSW
                                     92 	.globl _IP
                                     93 	.globl _P3
                                     94 	.globl _IE
                                     95 	.globl _P2
                                     96 	.globl _SBUF
                                     97 	.globl _SCON
                                     98 	.globl _P1
                                     99 	.globl _TH1
                                    100 	.globl _TH0
                                    101 	.globl _TL1
                                    102 	.globl _TL0
                                    103 	.globl _TMOD
                                    104 	.globl _TCON
                                    105 	.globl _PCON
                                    106 	.globl _DPH
                                    107 	.globl _DPL
                                    108 	.globl _SP
                                    109 	.globl _P0
                                    110 	.globl _count3
                                    111 	.globl _index
                                    112 	.globl _count2
                                    113 	.globl _tacc
                                    114 	.globl _fmax
                                    115 	.globl _f0
                                    116 	.globl _speed
                                    117 	.globl _step
                                    118 	.globl _direct
                                    119 	.globl _max
                                    120 	.globl _count
                                    121 ;--------------------------------------------------------
                                    122 ; special function registers
                                    123 ;--------------------------------------------------------
                                    124 	.area RSEG    (ABS,DATA)
      000000                        125 	.org 0x0000
                           000080   126 _P0	=	0x0080
                           000081   127 _SP	=	0x0081
                           000082   128 _DPL	=	0x0082
                           000083   129 _DPH	=	0x0083
                           000087   130 _PCON	=	0x0087
                           000088   131 _TCON	=	0x0088
                           000089   132 _TMOD	=	0x0089
                           00008A   133 _TL0	=	0x008a
                           00008B   134 _TL1	=	0x008b
                           00008C   135 _TH0	=	0x008c
                           00008D   136 _TH1	=	0x008d
                           000090   137 _P1	=	0x0090
                           000098   138 _SCON	=	0x0098
                           000099   139 _SBUF	=	0x0099
                           0000A0   140 _P2	=	0x00a0
                           0000A8   141 _IE	=	0x00a8
                           0000B0   142 _P3	=	0x00b0
                           0000B8   143 _IP	=	0x00b8
                           0000D0   144 _PSW	=	0x00d0
                           0000E0   145 _ACC	=	0x00e0
                           0000F0   146 _B	=	0x00f0
                                    147 ;--------------------------------------------------------
                                    148 ; special function bits
                                    149 ;--------------------------------------------------------
                                    150 	.area RSEG    (ABS,DATA)
      000000                        151 	.org 0x0000
                           000080   152 _P0_0	=	0x0080
                           000081   153 _P0_1	=	0x0081
                           000082   154 _P0_2	=	0x0082
                           000083   155 _P0_3	=	0x0083
                           000084   156 _P0_4	=	0x0084
                           000085   157 _P0_5	=	0x0085
                           000086   158 _P0_6	=	0x0086
                           000087   159 _P0_7	=	0x0087
                           000088   160 _IT0	=	0x0088
                           000089   161 _IE0	=	0x0089
                           00008A   162 _IT1	=	0x008a
                           00008B   163 _IE1	=	0x008b
                           00008C   164 _TR0	=	0x008c
                           00008D   165 _TF0	=	0x008d
                           00008E   166 _TR1	=	0x008e
                           00008F   167 _TF1	=	0x008f
                           000090   168 _P1_0	=	0x0090
                           000091   169 _P1_1	=	0x0091
                           000092   170 _P1_2	=	0x0092
                           000093   171 _P1_3	=	0x0093
                           000094   172 _P1_4	=	0x0094
                           000095   173 _P1_5	=	0x0095
                           000096   174 _P1_6	=	0x0096
                           000097   175 _P1_7	=	0x0097
                           000098   176 _RI	=	0x0098
                           000099   177 _TI	=	0x0099
                           00009A   178 _RB8	=	0x009a
                           00009B   179 _TB8	=	0x009b
                           00009C   180 _REN	=	0x009c
                           00009D   181 _SM2	=	0x009d
                           00009E   182 _SM1	=	0x009e
                           00009F   183 _SM0	=	0x009f
                           0000A0   184 _P2_0	=	0x00a0
                           0000A1   185 _P2_1	=	0x00a1
                           0000A2   186 _P2_2	=	0x00a2
                           0000A3   187 _P2_3	=	0x00a3
                           0000A4   188 _P2_4	=	0x00a4
                           0000A5   189 _P2_5	=	0x00a5
                           0000A6   190 _P2_6	=	0x00a6
                           0000A7   191 _P2_7	=	0x00a7
                           0000A8   192 _EX0	=	0x00a8
                           0000A9   193 _ET0	=	0x00a9
                           0000AA   194 _EX1	=	0x00aa
                           0000AB   195 _ET1	=	0x00ab
                           0000AC   196 _ES	=	0x00ac
                           0000AF   197 _EA	=	0x00af
                           0000B0   198 _P3_0	=	0x00b0
                           0000B1   199 _P3_1	=	0x00b1
                           0000B2   200 _P3_2	=	0x00b2
                           0000B3   201 _P3_3	=	0x00b3
                           0000B4   202 _P3_4	=	0x00b4
                           0000B5   203 _P3_5	=	0x00b5
                           0000B6   204 _P3_6	=	0x00b6
                           0000B7   205 _P3_7	=	0x00b7
                           0000B0   206 _RXD	=	0x00b0
                           0000B1   207 _TXD	=	0x00b1
                           0000B2   208 _INT0	=	0x00b2
                           0000B3   209 _INT1	=	0x00b3
                           0000B4   210 _T0	=	0x00b4
                           0000B5   211 _T1	=	0x00b5
                           0000B6   212 _WR	=	0x00b6
                           0000B7   213 _RD	=	0x00b7
                           0000B8   214 _PX0	=	0x00b8
                           0000B9   215 _PT0	=	0x00b9
                           0000BA   216 _PX1	=	0x00ba
                           0000BB   217 _PT1	=	0x00bb
                           0000BC   218 _PS	=	0x00bc
                           0000D0   219 _P	=	0x00d0
                           0000D1   220 _F1	=	0x00d1
                           0000D2   221 _OV	=	0x00d2
                           0000D3   222 _RS0	=	0x00d3
                           0000D4   223 _RS1	=	0x00d4
                           0000D5   224 _F0	=	0x00d5
                           0000D6   225 _AC	=	0x00d6
                           0000D7   226 _CY	=	0x00d7
                                    227 ;--------------------------------------------------------
                                    228 ; overlayable register banks
                                    229 ;--------------------------------------------------------
                                    230 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                        231 	.ds 8
                                    232 	.area REG_BANK_1	(REL,OVR,DATA)
      000008                        233 	.ds 8
                                    234 ;--------------------------------------------------------
                                    235 ; overlayable bit register bank
                                    236 ;--------------------------------------------------------
                                    237 	.area BIT_BANK	(REL,OVR,DATA)
      000020                        238 bits:
      000020                        239 	.ds 1
                           008000   240 	b0 = bits[0]
                           008100   241 	b1 = bits[1]
                           008200   242 	b2 = bits[2]
                           008300   243 	b3 = bits[3]
                           008400   244 	b4 = bits[4]
                           008500   245 	b5 = bits[5]
                           008600   246 	b6 = bits[6]
                           008700   247 	b7 = bits[7]
                                    248 ;--------------------------------------------------------
                                    249 ; internal ram data
                                    250 ;--------------------------------------------------------
                                    251 	.area DSEG    (DATA)
      000021                        252 _count::
      000021                        253 	.ds 2
      000023                        254 _max::
      000023                        255 	.ds 2
      000025                        256 _direct::
      000025                        257 	.ds 1
      000026                        258 _step::
      000026                        259 	.ds 1
      000027                        260 _speed::
      000027                        261 	.ds 2
      000029                        262 _f0::
      000029                        263 	.ds 2
      00002B                        264 _fmax::
      00002B                        265 	.ds 2
      00002D                        266 _tacc::
      00002D                        267 	.ds 2
      00002F                        268 _count2::
      00002F                        269 	.ds 12
      00003B                        270 _index::
      00003B                        271 	.ds 2
      00003D                        272 _count3::
      00003D                        273 	.ds 2
                                    274 ;--------------------------------------------------------
                                    275 ; overlayable items in internal ram 
                                    276 ;--------------------------------------------------------
                                    277 ;--------------------------------------------------------
                                    278 ; Stack segment in internal ram 
                                    279 ;--------------------------------------------------------
                                    280 	.area	SSEG
      00003F                        281 __start__stack:
      00003F                        282 	.ds	1
                                    283 
                                    284 ;--------------------------------------------------------
                                    285 ; indirectly addressable internal ram data
                                    286 ;--------------------------------------------------------
                                    287 	.area ISEG    (DATA)
                                    288 ;--------------------------------------------------------
                                    289 ; absolute internal ram data
                                    290 ;--------------------------------------------------------
                                    291 	.area IABS    (ABS,DATA)
                                    292 	.area IABS    (ABS,DATA)
                                    293 ;--------------------------------------------------------
                                    294 ; bit data
                                    295 ;--------------------------------------------------------
                                    296 	.area BSEG    (BIT)
                                    297 ;--------------------------------------------------------
                                    298 ; paged external ram data
                                    299 ;--------------------------------------------------------
                                    300 	.area PSEG    (PAG,XDATA)
                                    301 ;--------------------------------------------------------
                                    302 ; external ram data
                                    303 ;--------------------------------------------------------
                                    304 	.area XSEG    (XDATA)
                                    305 ;--------------------------------------------------------
                                    306 ; absolute external ram data
                                    307 ;--------------------------------------------------------
                                    308 	.area XABS    (ABS,XDATA)
                                    309 ;--------------------------------------------------------
                                    310 ; external initialized ram data
                                    311 ;--------------------------------------------------------
                                    312 	.area XISEG   (XDATA)
                                    313 	.area HOME    (CODE)
                                    314 	.area GSINIT0 (CODE)
                                    315 	.area GSINIT1 (CODE)
                                    316 	.area GSINIT2 (CODE)
                                    317 	.area GSINIT3 (CODE)
                                    318 	.area GSINIT4 (CODE)
                                    319 	.area GSINIT5 (CODE)
                                    320 	.area GSINIT  (CODE)
                                    321 	.area GSFINAL (CODE)
                                    322 	.area CSEG    (CODE)
                                    323 ;--------------------------------------------------------
                                    324 ; interrupt vector 
                                    325 ;--------------------------------------------------------
                                    326 	.area HOME    (CODE)
      000000                        327 __interrupt_vect:
      000000 02 00 11         [24]  328 	ljmp	__sdcc_gsinit_startup
      000003 32               [24]  329 	reti
      000004                        330 	.ds	7
      00000B 02 00 BB         [24]  331 	ljmp	_timer_isr
                                    332 ;--------------------------------------------------------
                                    333 ; global & static initialisations
                                    334 ;--------------------------------------------------------
                                    335 	.area HOME    (CODE)
                                    336 	.area GSINIT  (CODE)
                                    337 	.area GSFINAL (CODE)
                                    338 	.area GSINIT  (CODE)
                                    339 	.globl __sdcc_gsinit_startup
                                    340 	.globl __sdcc_program_startup
                                    341 	.globl __start__stack
                                    342 	.globl __mcs51_genXINIT
                                    343 	.globl __mcs51_genXRAMCLEAR
                                    344 	.globl __mcs51_genRAMCLEAR
                                    345 ;	main.c:5: int count=2000; // 一圈200步
      00006A 75 21 D0         [24]  346 	mov	_count,#0xd0
      00006D 75 22 07         [24]  347 	mov	(_count + 1),#0x07
                                    348 ;	main.c:6: int max=50;
      000070 75 23 32         [24]  349 	mov	_max,#0x32
      000073 75 24 00         [24]  350 	mov	(_max + 1),#0x00
                                    351 ;	main.c:7: char direct=0; 
      000076 75 25 00         [24]  352 	mov	_direct,#0x00
                                    353 ;	main.c:8: unsigned char step=0x01;
      000079 75 26 01         [24]  354 	mov	_step,#0x01
                                    355 ;	main.c:9: unsigned int speed=(65536-65536);
      00007C E4               [12]  356 	clr	a
      00007D F5 27            [12]  357 	mov	_speed,a
      00007F F5 28            [12]  358 	mov	(_speed + 1),a
                                    359 ;	main.c:14: int f0=65536-30000;
      000081 75 29 D0         [24]  360 	mov	_f0,#0xd0
      000084 75 2A 8A         [24]  361 	mov	(_f0 + 1),#0x8a
                                    362 ;	main.c:15: int fmax=65536-7500;
      000087 75 2B B4         [24]  363 	mov	_fmax,#0xb4
      00008A 75 2C E2         [24]  364 	mov	(_fmax + 1),#0xe2
                                    365 ;	main.c:17: int tacc=1;
      00008D 75 2D 01         [24]  366 	mov	_tacc,#0x01
                                    367 ;	1-genFromRTrack replaced	mov	(_tacc + 1),#0x00
      000090 F5 2E            [12]  368 	mov	(_tacc + 1),a
                                    369 ;	main.c:21: int count2[]={20.0, 60.0, 73.33333333333333, 84.24242424242424, 93.73882712012208, 100};
      000092 75 2F 14         [24]  370 	mov	(_count2 + 0),#0x14
                                    371 ;	1-genFromRTrack replaced	mov	(_count2 + 1),#0x00
      000095 F5 30            [12]  372 	mov	(_count2 + 1),a
      000097 75 31 3C         [24]  373 	mov	((_count2 + 0x0002) + 0),#0x3c
                                    374 ;	1-genFromRTrack replaced	mov	((_count2 + 0x0002) + 1),#0x00
      00009A F5 32            [12]  375 	mov	((_count2 + 0x0002) + 1),a
      00009C 75 33 49         [24]  376 	mov	((_count2 + 0x0004) + 0),#0x49
                                    377 ;	1-genFromRTrack replaced	mov	((_count2 + 0x0004) + 1),#0x00
      00009F F5 34            [12]  378 	mov	((_count2 + 0x0004) + 1),a
      0000A1 75 35 54         [24]  379 	mov	((_count2 + 0x0006) + 0),#0x54
                                    380 ;	1-genFromRTrack replaced	mov	((_count2 + 0x0006) + 1),#0x00
      0000A4 F5 36            [12]  381 	mov	((_count2 + 0x0006) + 1),a
      0000A6 75 37 5D         [24]  382 	mov	((_count2 + 0x0008) + 0),#0x5d
                                    383 ;	1-genFromRTrack replaced	mov	((_count2 + 0x0008) + 1),#0x00
      0000A9 F5 38            [12]  384 	mov	((_count2 + 0x0008) + 1),a
      0000AB 75 39 64         [24]  385 	mov	((_count2 + 0x000a) + 0),#0x64
                                    386 ;	1-genFromRTrack replaced	mov	((_count2 + 0x000a) + 1),#0x00
      0000AE F5 3A            [12]  387 	mov	((_count2 + 0x000a) + 1),a
                                    388 ;	main.c:22: int index=0;
      0000B0 F5 3B            [12]  389 	mov	_index,a
      0000B2 F5 3C            [12]  390 	mov	(_index + 1),a
                                    391 ;	main.c:23: int count3=0;
      0000B4 F5 3D            [12]  392 	mov	_count3,a
      0000B6 F5 3E            [12]  393 	mov	(_count3 + 1),a
                                    394 	.area GSFINAL (CODE)
      0000B8 02 00 0E         [24]  395 	ljmp	__sdcc_program_startup
                                    396 ;--------------------------------------------------------
                                    397 ; Home
                                    398 ;--------------------------------------------------------
                                    399 	.area HOME    (CODE)
                                    400 	.area HOME    (CODE)
      00000E                        401 __sdcc_program_startup:
      00000E 02 01 BF         [24]  402 	ljmp	_main
                                    403 ;	return from main will return to caller
                                    404 ;--------------------------------------------------------
                                    405 ; code
                                    406 ;--------------------------------------------------------
                                    407 	.area CSEG    (CODE)
                                    408 ;------------------------------------------------------------
                                    409 ;Allocation info for local variables in function 'timer_isr'
                                    410 ;------------------------------------------------------------
                                    411 ;	main.c:25: void timer_isr (void) __interrupt (1) __using (1) {	//timer 0 interrupt 訊號		using register bank 1
                                    412 ;	-----------------------------------------
                                    413 ;	 function timer_isr
                                    414 ;	-----------------------------------------
      0000BB                        415 _timer_isr:
                           00000F   416 	ar7 = 0x0f
                           00000E   417 	ar6 = 0x0e
                           00000D   418 	ar5 = 0x0d
                           00000C   419 	ar4 = 0x0c
                           00000B   420 	ar3 = 0x0b
                           00000A   421 	ar2 = 0x0a
                           000009   422 	ar1 = 0x09
                           000008   423 	ar0 = 0x08
      0000BB C0 20            [24]  424 	push	bits
      0000BD C0 E0            [24]  425 	push	acc
      0000BF C0 F0            [24]  426 	push	b
      0000C1 C0 82            [24]  427 	push	dpl
      0000C3 C0 83            [24]  428 	push	dph
      0000C5 C0 07            [24]  429 	push	(0+7)
      0000C7 C0 06            [24]  430 	push	(0+6)
      0000C9 C0 05            [24]  431 	push	(0+5)
      0000CB C0 04            [24]  432 	push	(0+4)
      0000CD C0 03            [24]  433 	push	(0+3)
      0000CF C0 02            [24]  434 	push	(0+2)
      0000D1 C0 01            [24]  435 	push	(0+1)
      0000D3 C0 00            [24]  436 	push	(0+0)
      0000D5 C0 D0            [24]  437 	push	psw
      0000D7 75 D0 08         [24]  438 	mov	psw,#0x08
                                    439 ;	main.c:31: TH0=f0/256;
      0000DA 75 10 00         [24]  440 	mov	__divsint_PARM_2,#0x00
      0000DD 75 11 01         [24]  441 	mov	(__divsint_PARM_2 + 1),#0x01
      0000E0 85 29 82         [24]  442 	mov	dpl,_f0
      0000E3 85 2A 83         [24]  443 	mov	dph,(_f0 + 1)
      0000E6 75 D0 00         [24]  444 	mov	psw,#0x00
      0000E9 12 02 9B         [24]  445 	lcall	__divsint
      0000EC 75 D0 08         [24]  446 	mov	psw,#0x08
      0000EF AE 82            [24]  447 	mov	r6,dpl
      0000F1 8E 8C            [24]  448 	mov	_TH0,r6
                                    449 ;	main.c:32: TL0=f0%16;   
      0000F3 75 10 10         [24]  450 	mov	__modsint_PARM_2,#0x10
      0000F6 75 11 00         [24]  451 	mov	(__modsint_PARM_2 + 1),#0x00
      0000F9 85 29 82         [24]  452 	mov	dpl,_f0
      0000FC 85 2A 83         [24]  453 	mov	dph,(_f0 + 1)
      0000FF 75 D0 00         [24]  454 	mov	psw,#0x00
      000102 12 02 65         [24]  455 	lcall	__modsint
      000105 75 D0 08         [24]  456 	mov	psw,#0x08
      000108 AE 82            [24]  457 	mov	r6,dpl
      00010A AF 83            [24]  458 	mov	r7,dph
      00010C 8E 8A            [24]  459 	mov	_TL0,r6
                                    460 ;	main.c:34: if(direct==0) { 
      00010E E5 25            [12]  461 	mov	a,_direct
      000110 70 14            [24]  462 	jnz	00106$
                                    463 ;	main.c:35: step>>=1;
      000112 E5 26            [12]  464 	mov	a,_step
      000114 C3               [12]  465 	clr	c
      000115 13               [12]  466 	rrc	a
                                    467 ;	main.c:36: if(step==0x00) step=0x08;
      000116 F5 26            [12]  468 	mov	_step,a
      000118 70 03            [24]  469 	jnz	00102$
      00011A 75 26 08         [24]  470 	mov	_step,#0x08
      00011D                        471 00102$:
                                    472 ;	main.c:37: P0&=0xf0;
      00011D 53 80 F0         [24]  473 	anl	_P0,#0xf0
                                    474 ;	main.c:38: P0|=step;
      000120 E5 26            [12]  475 	mov	a,_step
      000122 42 80            [12]  476 	orl	_P0,a
      000124 80 16            [24]  477 	sjmp	00107$
      000126                        478 00106$:
                                    479 ;	main.c:41: step<<=1; 
      000126 E5 26            [12]  480 	mov	a,_step
      000128 FF               [12]  481 	mov	r7,a
      000129 25 E0            [12]  482 	add	a,acc
      00012B F5 26            [12]  483 	mov	_step,a
                                    484 ;	main.c:42: if(step==0x10)
      00012D 74 10            [12]  485 	mov	a,#0x10
      00012F B5 26 03         [24]  486 	cjne	a,_step,00104$
                                    487 ;	main.c:43: step=0x01;
      000132 75 26 01         [24]  488 	mov	_step,#0x01
      000135                        489 00104$:
                                    490 ;	main.c:44: P0&=0xf0;
      000135 53 80 F0         [24]  491 	anl	_P0,#0xf0
                                    492 ;	main.c:45: P0|=step;
      000138 E5 26            [12]  493 	mov	a,_step
      00013A 42 80            [12]  494 	orl	_P0,a
      00013C                        495 00107$:
                                    496 ;	main.c:47: count3++;
      00013C 05 3D            [12]  497 	inc	_count3
      00013E E4               [12]  498 	clr	a
      00013F B5 3D 02         [24]  499 	cjne	a,_count3,00150$
      000142 05 3E            [12]  500 	inc	(_count3 + 1)
      000144                        501 00150$:
                                    502 ;	main.c:48: if(count3>=10){
      000144 C3               [12]  503 	clr	c
      000145 E5 3D            [12]  504 	mov	a,_count3
      000147 94 0A            [12]  505 	subb	a,#0x0a
      000149 E5 3E            [12]  506 	mov	a,(_count3 + 1)
      00014B 64 80            [12]  507 	xrl	a,#0x80
      00014D 94 80            [12]  508 	subb	a,#0x80
                                    509 ;	main.c:49: if(f0<fmax)
      00014F 40 1D            [24]  510 	jc	00111$
      000151 E5 29            [12]  511 	mov	a,_f0
      000153 95 2B            [12]  512 	subb	a,_fmax
      000155 E5 2A            [12]  513 	mov	a,(_f0 + 1)
      000157 64 80            [12]  514 	xrl	a,#0x80
      000159 85 2C F0         [24]  515 	mov	b,(_fmax + 1)
      00015C 63 F0 80         [24]  516 	xrl	b,#0x80
      00015F 95 F0            [12]  517 	subb	a,b
      000161 50 0B            [24]  518 	jnc	00111$
                                    519 ;	main.c:50: f0+=100;
      000163 74 64            [12]  520 	mov	a,#0x64
      000165 25 29            [12]  521 	add	a,_f0
      000167 F5 29            [12]  522 	mov	_f0,a
      000169 E4               [12]  523 	clr	a
      00016A 35 2A            [12]  524 	addc	a,(_f0 + 1)
      00016C F5 2A            [12]  525 	mov	(_f0 + 1),a
      00016E                        526 00111$:
                                    527 ;	main.c:52: if(--count<=0){
      00016E 15 21            [12]  528 	dec	_count
      000170 74 FF            [12]  529 	mov	a,#0xff
      000172 B5 21 02         [24]  530 	cjne	a,_count,00153$
      000175 15 22            [12]  531 	dec	(_count + 1)
      000177                        532 00153$:
      000177 C3               [12]  533 	clr	c
      000178 E4               [12]  534 	clr	a
      000179 95 21            [12]  535 	subb	a,_count
      00017B 74 80            [12]  536 	mov	a,#(0x00 ^ 0x80)
      00017D 85 22 F0         [24]  537 	mov	b,(_count + 1)
      000180 63 F0 80         [24]  538 	xrl	b,#0x80
      000183 95 F0            [12]  539 	subb	a,b
      000185 40 1B            [24]  540 	jc	00116$
                                    541 ;	main.c:53: if(direct==1)
      000187 74 01            [12]  542 	mov	a,#0x01
      000189 B5 25 02         [24]  543 	cjne	a,_direct,00113$
                                    544 ;	main.c:54: TR0=0;
                                    545 ;	assignBit
      00018C C2 8C            [12]  546 	clr	_TR0
      00018E                        547 00113$:
                                    548 ;	main.c:55: direct=1;
      00018E 75 25 01         [24]  549 	mov	_direct,#0x01
                                    550 ;	main.c:56: count=4000;
      000191 75 21 A0         [24]  551 	mov	_count,#0xa0
      000194 75 22 0F         [24]  552 	mov	(_count + 1),#0x0f
                                    553 ;	main.c:57: count3=0;
      000197 E4               [12]  554 	clr	a
      000198 F5 3D            [12]  555 	mov	_count3,a
      00019A F5 3E            [12]  556 	mov	(_count3 + 1),a
                                    557 ;	main.c:58: f0=65536-30000;
      00019C 75 29 D0         [24]  558 	mov	_f0,#0xd0
      00019F 75 2A 8A         [24]  559 	mov	(_f0 + 1),#0x8a
      0001A2                        560 00116$:
                                    561 ;	main.c:60: }
      0001A2 D0 D0            [24]  562 	pop	psw
      0001A4 D0 00            [24]  563 	pop	(0+0)
      0001A6 D0 01            [24]  564 	pop	(0+1)
      0001A8 D0 02            [24]  565 	pop	(0+2)
      0001AA D0 03            [24]  566 	pop	(0+3)
      0001AC D0 04            [24]  567 	pop	(0+4)
      0001AE D0 05            [24]  568 	pop	(0+5)
      0001B0 D0 06            [24]  569 	pop	(0+6)
      0001B2 D0 07            [24]  570 	pop	(0+7)
      0001B4 D0 83            [24]  571 	pop	dph
      0001B6 D0 82            [24]  572 	pop	dpl
      0001B8 D0 F0            [24]  573 	pop	b
      0001BA D0 E0            [24]  574 	pop	acc
      0001BC D0 20            [24]  575 	pop	bits
      0001BE 32               [24]  576 	reti
                                    577 ;------------------------------------------------------------
                                    578 ;Allocation info for local variables in function 'main'
                                    579 ;------------------------------------------------------------
                                    580 ;	main.c:61: int main(){
                                    581 ;	-----------------------------------------
                                    582 ;	 function main
                                    583 ;	-----------------------------------------
      0001BF                        584 _main:
                           000007   585 	ar7 = 0x07
                           000006   586 	ar6 = 0x06
                           000005   587 	ar5 = 0x05
                           000004   588 	ar4 = 0x04
                           000003   589 	ar3 = 0x03
                           000002   590 	ar2 = 0x02
                           000001   591 	ar1 = 0x01
                           000000   592 	ar0 = 0x00
                                    593 ;	main.c:62: IE=0x82;
      0001BF 75 A8 82         [24]  594 	mov	_IE,#0x82
                                    595 ;	main.c:63: TMOD=0x01;
      0001C2 75 89 01         [24]  596 	mov	_TMOD,#0x01
                                    597 ;	main.c:64: TH0=f0/256;
      0001C5 75 10 00         [24]  598 	mov	__divsint_PARM_2,#0x00
      0001C8 75 11 01         [24]  599 	mov	(__divsint_PARM_2 + 1),#0x01
      0001CB 85 29 82         [24]  600 	mov	dpl,_f0
      0001CE 85 2A 83         [24]  601 	mov	dph,(_f0 + 1)
      0001D1 12 02 9B         [24]  602 	lcall	__divsint
      0001D4 AE 82            [24]  603 	mov	r6,dpl
      0001D6 8E 8C            [24]  604 	mov	_TH0,r6
                                    605 ;	main.c:65: TL0=f0%16;
      0001D8 75 10 10         [24]  606 	mov	__modsint_PARM_2,#0x10
      0001DB 75 11 00         [24]  607 	mov	(__modsint_PARM_2 + 1),#0x00
      0001DE 85 29 82         [24]  608 	mov	dpl,_f0
      0001E1 85 2A 83         [24]  609 	mov	dph,(_f0 + 1)
      0001E4 12 02 65         [24]  610 	lcall	__modsint
      0001E7 AE 82            [24]  611 	mov	r6,dpl
      0001E9 8E 8A            [24]  612 	mov	_TL0,r6
                                    613 ;	main.c:66: TR0=1;
                                    614 ;	assignBit
      0001EB D2 8C            [12]  615 	setb	_TR0
                                    616 ;	main.c:67: while (1) {
      0001ED                        617 00102$:
                                    618 ;	main.c:69: }
      0001ED 80 FE            [24]  619 	sjmp	00102$
                                    620 	.area CSEG    (CODE)
                                    621 	.area CONST   (CODE)
      0002D7                        622 _SPIN:
      0002D7 03 00                  623 	.byte #0x03,#0x00	;  3
      0002D9 06 00                  624 	.byte #0x06,#0x00	;  6
      0002DB 0C 00                  625 	.byte #0x0c,#0x00	;  12
      0002DD 09 00                  626 	.byte #0x09,#0x00	;  9
                                    627 	.area XINIT   (CODE)
                                    628 	.area CABS    (ABS,CODE)
