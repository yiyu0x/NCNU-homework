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
                                     11 	.globl _music
                                     12 	.globl _main
                                     13 	.globl _init
                                     14 	.globl _timer1
                                     15 	.globl _timer_isr
                                     16 	.globl _CY
                                     17 	.globl _AC
                                     18 	.globl _F0
                                     19 	.globl _RS1
                                     20 	.globl _RS0
                                     21 	.globl _OV
                                     22 	.globl _F1
                                     23 	.globl _P
                                     24 	.globl _PS
                                     25 	.globl _PT1
                                     26 	.globl _PX1
                                     27 	.globl _PT0
                                     28 	.globl _PX0
                                     29 	.globl _RD
                                     30 	.globl _WR
                                     31 	.globl _T1
                                     32 	.globl _T0
                                     33 	.globl _INT1
                                     34 	.globl _INT0
                                     35 	.globl _TXD
                                     36 	.globl _RXD
                                     37 	.globl _P3_7
                                     38 	.globl _P3_6
                                     39 	.globl _P3_5
                                     40 	.globl _P3_4
                                     41 	.globl _P3_3
                                     42 	.globl _P3_2
                                     43 	.globl _P3_1
                                     44 	.globl _P3_0
                                     45 	.globl _EA
                                     46 	.globl _ES
                                     47 	.globl _ET1
                                     48 	.globl _EX1
                                     49 	.globl _ET0
                                     50 	.globl _EX0
                                     51 	.globl _P2_7
                                     52 	.globl _P2_6
                                     53 	.globl _P2_5
                                     54 	.globl _P2_4
                                     55 	.globl _P2_3
                                     56 	.globl _P2_2
                                     57 	.globl _P2_1
                                     58 	.globl _P2_0
                                     59 	.globl _SM0
                                     60 	.globl _SM1
                                     61 	.globl _SM2
                                     62 	.globl _REN
                                     63 	.globl _TB8
                                     64 	.globl _RB8
                                     65 	.globl _TI
                                     66 	.globl _RI
                                     67 	.globl _P1_7
                                     68 	.globl _P1_6
                                     69 	.globl _P1_5
                                     70 	.globl _P1_4
                                     71 	.globl _P1_3
                                     72 	.globl _P1_2
                                     73 	.globl _P1_1
                                     74 	.globl _P1_0
                                     75 	.globl _TF1
                                     76 	.globl _TR1
                                     77 	.globl _TF0
                                     78 	.globl _TR0
                                     79 	.globl _IE1
                                     80 	.globl _IT1
                                     81 	.globl _IE0
                                     82 	.globl _IT0
                                     83 	.globl _P0_7
                                     84 	.globl _P0_6
                                     85 	.globl _P0_5
                                     86 	.globl _P0_4
                                     87 	.globl _P0_3
                                     88 	.globl _P0_2
                                     89 	.globl _P0_1
                                     90 	.globl _P0_0
                                     91 	.globl _B
                                     92 	.globl _ACC
                                     93 	.globl _PSW
                                     94 	.globl _IP
                                     95 	.globl _P3
                                     96 	.globl _IE
                                     97 	.globl _P2
                                     98 	.globl _SBUF
                                     99 	.globl _SCON
                                    100 	.globl _P1
                                    101 	.globl _TH1
                                    102 	.globl _TH0
                                    103 	.globl _TL1
                                    104 	.globl _TL0
                                    105 	.globl _TMOD
                                    106 	.globl _TCON
                                    107 	.globl _PCON
                                    108 	.globl _DPH
                                    109 	.globl _DPL
                                    110 	.globl _SP
                                    111 	.globl _P0
                                    112 	.globl _table_index
                                    113 	.globl _counter
                                    114 	.globl _table
                                    115 	.globl _isSound
                                    116 	.globl _music_index
                                    117 	.globl _timer1_count
                                    118 ;--------------------------------------------------------
                                    119 ; special function registers
                                    120 ;--------------------------------------------------------
                                    121 	.area RSEG    (ABS,DATA)
      000000                        122 	.org 0x0000
                           000080   123 _P0	=	0x0080
                           000081   124 _SP	=	0x0081
                           000082   125 _DPL	=	0x0082
                           000083   126 _DPH	=	0x0083
                           000087   127 _PCON	=	0x0087
                           000088   128 _TCON	=	0x0088
                           000089   129 _TMOD	=	0x0089
                           00008A   130 _TL0	=	0x008a
                           00008B   131 _TL1	=	0x008b
                           00008C   132 _TH0	=	0x008c
                           00008D   133 _TH1	=	0x008d
                           000090   134 _P1	=	0x0090
                           000098   135 _SCON	=	0x0098
                           000099   136 _SBUF	=	0x0099
                           0000A0   137 _P2	=	0x00a0
                           0000A8   138 _IE	=	0x00a8
                           0000B0   139 _P3	=	0x00b0
                           0000B8   140 _IP	=	0x00b8
                           0000D0   141 _PSW	=	0x00d0
                           0000E0   142 _ACC	=	0x00e0
                           0000F0   143 _B	=	0x00f0
                                    144 ;--------------------------------------------------------
                                    145 ; special function bits
                                    146 ;--------------------------------------------------------
                                    147 	.area RSEG    (ABS,DATA)
      000000                        148 	.org 0x0000
                           000080   149 _P0_0	=	0x0080
                           000081   150 _P0_1	=	0x0081
                           000082   151 _P0_2	=	0x0082
                           000083   152 _P0_3	=	0x0083
                           000084   153 _P0_4	=	0x0084
                           000085   154 _P0_5	=	0x0085
                           000086   155 _P0_6	=	0x0086
                           000087   156 _P0_7	=	0x0087
                           000088   157 _IT0	=	0x0088
                           000089   158 _IE0	=	0x0089
                           00008A   159 _IT1	=	0x008a
                           00008B   160 _IE1	=	0x008b
                           00008C   161 _TR0	=	0x008c
                           00008D   162 _TF0	=	0x008d
                           00008E   163 _TR1	=	0x008e
                           00008F   164 _TF1	=	0x008f
                           000090   165 _P1_0	=	0x0090
                           000091   166 _P1_1	=	0x0091
                           000092   167 _P1_2	=	0x0092
                           000093   168 _P1_3	=	0x0093
                           000094   169 _P1_4	=	0x0094
                           000095   170 _P1_5	=	0x0095
                           000096   171 _P1_6	=	0x0096
                           000097   172 _P1_7	=	0x0097
                           000098   173 _RI	=	0x0098
                           000099   174 _TI	=	0x0099
                           00009A   175 _RB8	=	0x009a
                           00009B   176 _TB8	=	0x009b
                           00009C   177 _REN	=	0x009c
                           00009D   178 _SM2	=	0x009d
                           00009E   179 _SM1	=	0x009e
                           00009F   180 _SM0	=	0x009f
                           0000A0   181 _P2_0	=	0x00a0
                           0000A1   182 _P2_1	=	0x00a1
                           0000A2   183 _P2_2	=	0x00a2
                           0000A3   184 _P2_3	=	0x00a3
                           0000A4   185 _P2_4	=	0x00a4
                           0000A5   186 _P2_5	=	0x00a5
                           0000A6   187 _P2_6	=	0x00a6
                           0000A7   188 _P2_7	=	0x00a7
                           0000A8   189 _EX0	=	0x00a8
                           0000A9   190 _ET0	=	0x00a9
                           0000AA   191 _EX1	=	0x00aa
                           0000AB   192 _ET1	=	0x00ab
                           0000AC   193 _ES	=	0x00ac
                           0000AF   194 _EA	=	0x00af
                           0000B0   195 _P3_0	=	0x00b0
                           0000B1   196 _P3_1	=	0x00b1
                           0000B2   197 _P3_2	=	0x00b2
                           0000B3   198 _P3_3	=	0x00b3
                           0000B4   199 _P3_4	=	0x00b4
                           0000B5   200 _P3_5	=	0x00b5
                           0000B6   201 _P3_6	=	0x00b6
                           0000B7   202 _P3_7	=	0x00b7
                           0000B0   203 _RXD	=	0x00b0
                           0000B1   204 _TXD	=	0x00b1
                           0000B2   205 _INT0	=	0x00b2
                           0000B3   206 _INT1	=	0x00b3
                           0000B4   207 _T0	=	0x00b4
                           0000B5   208 _T1	=	0x00b5
                           0000B6   209 _WR	=	0x00b6
                           0000B7   210 _RD	=	0x00b7
                           0000B8   211 _PX0	=	0x00b8
                           0000B9   212 _PT0	=	0x00b9
                           0000BA   213 _PX1	=	0x00ba
                           0000BB   214 _PT1	=	0x00bb
                           0000BC   215 _PS	=	0x00bc
                           0000D0   216 _P	=	0x00d0
                           0000D1   217 _F1	=	0x00d1
                           0000D2   218 _OV	=	0x00d2
                           0000D3   219 _RS0	=	0x00d3
                           0000D4   220 _RS1	=	0x00d4
                           0000D5   221 _F0	=	0x00d5
                           0000D6   222 _AC	=	0x00d6
                           0000D7   223 _CY	=	0x00d7
                                    224 ;--------------------------------------------------------
                                    225 ; overlayable register banks
                                    226 ;--------------------------------------------------------
                                    227 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                        228 	.ds 8
                                    229 	.area REG_BANK_1	(REL,OVR,DATA)
      000008                        230 	.ds 8
                                    231 	.area REG_BANK_2	(REL,OVR,DATA)
      000010                        232 	.ds 8
                                    233 ;--------------------------------------------------------
                                    234 ; internal ram data
                                    235 ;--------------------------------------------------------
                                    236 	.area DSEG    (DATA)
      000018                        237 _timer1_count::
      000018                        238 	.ds 2
      00001A                        239 _music_index::
      00001A                        240 	.ds 1
      00001B                        241 _isSound::
      00001B                        242 	.ds 2
      00001D                        243 _table::
      00001D                        244 	.ds 32
      00003D                        245 _counter::
      00003D                        246 	.ds 1
      00003E                        247 _table_index::
      00003E                        248 	.ds 1
                                    249 ;--------------------------------------------------------
                                    250 ; overlayable items in internal ram 
                                    251 ;--------------------------------------------------------
                                    252 ;--------------------------------------------------------
                                    253 ; Stack segment in internal ram 
                                    254 ;--------------------------------------------------------
                                    255 	.area	SSEG
      00003F                        256 __start__stack:
      00003F                        257 	.ds	1
                                    258 
                                    259 ;--------------------------------------------------------
                                    260 ; indirectly addressable internal ram data
                                    261 ;--------------------------------------------------------
                                    262 	.area ISEG    (DATA)
                                    263 ;--------------------------------------------------------
                                    264 ; absolute internal ram data
                                    265 ;--------------------------------------------------------
                                    266 	.area IABS    (ABS,DATA)
                                    267 	.area IABS    (ABS,DATA)
                                    268 ;--------------------------------------------------------
                                    269 ; bit data
                                    270 ;--------------------------------------------------------
                                    271 	.area BSEG    (BIT)
                                    272 ;--------------------------------------------------------
                                    273 ; paged external ram data
                                    274 ;--------------------------------------------------------
                                    275 	.area PSEG    (PAG,XDATA)
                                    276 ;--------------------------------------------------------
                                    277 ; external ram data
                                    278 ;--------------------------------------------------------
                                    279 	.area XSEG    (XDATA)
                                    280 ;--------------------------------------------------------
                                    281 ; absolute external ram data
                                    282 ;--------------------------------------------------------
                                    283 	.area XABS    (ABS,XDATA)
                                    284 ;--------------------------------------------------------
                                    285 ; external initialized ram data
                                    286 ;--------------------------------------------------------
                                    287 	.area XISEG   (XDATA)
                                    288 	.area HOME    (CODE)
                                    289 	.area GSINIT0 (CODE)
                                    290 	.area GSINIT1 (CODE)
                                    291 	.area GSINIT2 (CODE)
                                    292 	.area GSINIT3 (CODE)
                                    293 	.area GSINIT4 (CODE)
                                    294 	.area GSINIT5 (CODE)
                                    295 	.area GSINIT  (CODE)
                                    296 	.area GSFINAL (CODE)
                                    297 	.area CSEG    (CODE)
                                    298 ;--------------------------------------------------------
                                    299 ; interrupt vector 
                                    300 ;--------------------------------------------------------
                                    301 	.area HOME    (CODE)
      000000                        302 __interrupt_vect:
      000000 02 00 21         [24]  303 	ljmp	__sdcc_gsinit_startup
      000003 32               [24]  304 	reti
      000004                        305 	.ds	7
      00000B 02 00 AD         [24]  306 	ljmp	_timer_isr
      00000E                        307 	.ds	5
      000013 32               [24]  308 	reti
      000014                        309 	.ds	7
      00001B 02 00 F1         [24]  310 	ljmp	_timer1
                                    311 ;--------------------------------------------------------
                                    312 ; global & static initialisations
                                    313 ;--------------------------------------------------------
                                    314 	.area HOME    (CODE)
                                    315 	.area GSINIT  (CODE)
                                    316 	.area GSFINAL (CODE)
                                    317 	.area GSINIT  (CODE)
                                    318 	.globl __sdcc_gsinit_startup
                                    319 	.globl __sdcc_program_startup
                                    320 	.globl __start__stack
                                    321 	.globl __mcs51_genXINIT
                                    322 	.globl __mcs51_genXRAMCLEAR
                                    323 	.globl __mcs51_genRAMCLEAR
                                    324 ;	main.c:9: int table[16] = {262, 294, 330, 349, 392, 440, 494};
      00007A 75 1D 06         [24]  325 	mov	(_table + 0),#0x06
      00007D 75 1E 01         [24]  326 	mov	(_table + 1),#0x01
      000080 75 1F 26         [24]  327 	mov	((_table + 0x0002) + 0),#0x26
      000083 75 20 01         [24]  328 	mov	((_table + 0x0002) + 1),#0x01
      000086 75 21 4A         [24]  329 	mov	((_table + 0x0004) + 0),#0x4a
      000089 75 22 01         [24]  330 	mov	((_table + 0x0004) + 1),#0x01
      00008C 75 23 5D         [24]  331 	mov	((_table + 0x0006) + 0),#0x5d
      00008F 75 24 01         [24]  332 	mov	((_table + 0x0006) + 1),#0x01
      000092 75 25 88         [24]  333 	mov	((_table + 0x0008) + 0),#0x88
      000095 75 26 01         [24]  334 	mov	((_table + 0x0008) + 1),#0x01
      000098 75 27 B8         [24]  335 	mov	((_table + 0x000a) + 0),#0xb8
      00009B 75 28 01         [24]  336 	mov	((_table + 0x000a) + 1),#0x01
      00009E 75 29 EE         [24]  337 	mov	((_table + 0x000c) + 0),#0xee
      0000A1 75 2A 01         [24]  338 	mov	((_table + 0x000c) + 1),#0x01
                                    339 ;	main.c:18: char counter = 0;
      0000A4 75 3D 00         [24]  340 	mov	_counter,#0x00
                                    341 ;	main.c:19: char table_index=0;
      0000A7 75 3E 00         [24]  342 	mov	_table_index,#0x00
                                    343 	.area GSFINAL (CODE)
      0000AA 02 00 1E         [24]  344 	ljmp	__sdcc_program_startup
                                    345 ;--------------------------------------------------------
                                    346 ; Home
                                    347 ;--------------------------------------------------------
                                    348 	.area HOME    (CODE)
                                    349 	.area HOME    (CODE)
      00001E                        350 __sdcc_program_startup:
      00001E 02 01 DD         [24]  351 	ljmp	_main
                                    352 ;	return from main will return to caller
                                    353 ;--------------------------------------------------------
                                    354 ; code
                                    355 ;--------------------------------------------------------
                                    356 	.area CSEG    (CODE)
                                    357 ;------------------------------------------------------------
                                    358 ;Allocation info for local variables in function 'timer_isr'
                                    359 ;------------------------------------------------------------
                                    360 ;	main.c:21: void timer_isr (void) __interrupt (1) __using (1) {
                                    361 ;	-----------------------------------------
                                    362 ;	 function timer_isr
                                    363 ;	-----------------------------------------
      0000AD                        364 _timer_isr:
                           00000F   365 	ar7 = 0x0f
                           00000E   366 	ar6 = 0x0e
                           00000D   367 	ar5 = 0x0d
                           00000C   368 	ar4 = 0x0c
                           00000B   369 	ar3 = 0x0b
                           00000A   370 	ar2 = 0x0a
                           000009   371 	ar1 = 0x09
                           000008   372 	ar0 = 0x08
      0000AD C0 E0            [24]  373 	push	acc
      0000AF C0 82            [24]  374 	push	dpl
      0000B1 C0 83            [24]  375 	push	dph
      0000B3 C0 D0            [24]  376 	push	psw
      0000B5 75 D0 08         [24]  377 	mov	psw,#0x08
                                    378 ;	main.c:23: TH0  = (PERIOD-table[music[music_index]-1]) >> 8;
      0000B8 E5 1A            [12]  379 	mov	a,_music_index
      0000BA 90 05 68         [24]  380 	mov	dptr,#_music
      0000BD 93               [24]  381 	movc	a,@a+dptr
      0000BE FF               [12]  382 	mov	r7,a
      0000BF 1F               [12]  383 	dec	r7
      0000C0 EF               [12]  384 	mov	a,r7
      0000C1 2F               [12]  385 	add	a,r7
      0000C2 24 1D            [12]  386 	add	a,#_table
      0000C4 F9               [12]  387 	mov	r1,a
      0000C5 87 0E            [24]  388 	mov	ar6,@r1
      0000C7 09               [12]  389 	inc	r1
      0000C8 87 0F            [24]  390 	mov	ar7,@r1
      0000CA 8E 0A            [24]  391 	mov	ar2,r6
      0000CC EF               [12]  392 	mov	a,r7
      0000CD FB               [12]  393 	mov	r3,a
      0000CE 33               [12]  394 	rlc	a
      0000CF 95 E0            [12]  395 	subb	a,acc
      0000D1 FC               [12]  396 	mov	r4,a
      0000D2 FD               [12]  397 	mov	r5,a
      0000D3 E4               [12]  398 	clr	a
      0000D4 C3               [12]  399 	clr	c
      0000D5 9A               [12]  400 	subb	a,r2
      0000D6 E4               [12]  401 	clr	a
      0000D7 9B               [12]  402 	subb	a,r3
      0000D8 FB               [12]  403 	mov	r3,a
      0000D9 74 01            [12]  404 	mov	a,#0x01
      0000DB 9C               [12]  405 	subb	a,r4
      0000DC E4               [12]  406 	clr	a
      0000DD 9D               [12]  407 	subb	a,r5
      0000DE 8B 8C            [24]  408 	mov	_TH0,r3
                                    409 ;	main.c:24: TL0  = (PERIOD-table[music[music_index]-1]) & 0xff;
      0000E0 C3               [12]  410 	clr	c
      0000E1 E4               [12]  411 	clr	a
      0000E2 9E               [12]  412 	subb	a,r6
      0000E3 FE               [12]  413 	mov	r6,a
      0000E4 8E 8A            [24]  414 	mov	_TL0,r6
                                    415 ;	main.c:30: counter++;
      0000E6 05 3D            [12]  416 	inc	_counter
                                    417 ;	main.c:31: }
      0000E8 D0 D0            [24]  418 	pop	psw
      0000EA D0 83            [24]  419 	pop	dph
      0000EC D0 82            [24]  420 	pop	dpl
      0000EE D0 E0            [24]  421 	pop	acc
      0000F0 32               [24]  422 	reti
                                    423 ;	eliminated unneeded push/pop b
                                    424 ;------------------------------------------------------------
                                    425 ;Allocation info for local variables in function 'timer1'
                                    426 ;------------------------------------------------------------
                                    427 ;	main.c:32: void timer1 (void) __interrupt (3) __using (2) {
                                    428 ;	-----------------------------------------
                                    429 ;	 function timer1
                                    430 ;	-----------------------------------------
      0000F1                        431 _timer1:
                           000017   432 	ar7 = 0x17
                           000016   433 	ar6 = 0x16
                           000015   434 	ar5 = 0x15
                           000014   435 	ar4 = 0x14
                           000013   436 	ar3 = 0x13
                           000012   437 	ar2 = 0x12
                           000011   438 	ar1 = 0x11
                           000010   439 	ar0 = 0x10
      0000F1 C0 E0            [24]  440 	push	acc
      0000F3 C0 D0            [24]  441 	push	psw
                                    442 ;	main.c:33: TH1  = INIT_TIME >> 8;
      0000F5 75 8D 0B         [24]  443 	mov	_TH1,#0x0b
                                    444 ;	main.c:34: TL1  = INIT_TIME & 0xff;
      0000F8 75 8B DC         [24]  445 	mov	_TL1,#0xdc
                                    446 ;	main.c:35: timer1_count++;
      0000FB 05 18            [12]  447 	inc	_timer1_count
      0000FD E4               [12]  448 	clr	a
      0000FE B5 18 02         [24]  449 	cjne	a,_timer1_count,00103$
      000101 05 19            [12]  450 	inc	(_timer1_count + 1)
      000103                        451 00103$:
                                    452 ;	main.c:36: }
      000103 D0 D0            [24]  453 	pop	psw
      000105 D0 E0            [24]  454 	pop	acc
      000107 32               [24]  455 	reti
                                    456 ;	eliminated unneeded mov psw,# (no regs used in bank)
                                    457 ;	eliminated unneeded push/pop dpl
                                    458 ;	eliminated unneeded push/pop dph
                                    459 ;	eliminated unneeded push/pop b
                                    460 ;------------------------------------------------------------
                                    461 ;Allocation info for local variables in function 'init'
                                    462 ;------------------------------------------------------------
                                    463 ;tmp                       Allocated to registers r2 r3 r4 r5 
                                    464 ;i                         Allocated to registers r6 r7 
                                    465 ;i                         Allocated to registers r6 r7 
                                    466 ;------------------------------------------------------------
                                    467 ;	main.c:37: void init(){
                                    468 ;	-----------------------------------------
                                    469 ;	 function init
                                    470 ;	-----------------------------------------
      000108                        471 _init:
                           000007   472 	ar7 = 0x07
                           000006   473 	ar6 = 0x06
                           000005   474 	ar5 = 0x05
                           000004   475 	ar4 = 0x04
                           000003   476 	ar3 = 0x03
                           000002   477 	ar2 = 0x02
                           000001   478 	ar1 = 0x01
                           000000   479 	ar0 = 0x00
                                    480 ;	main.c:38: music_index=0;
      000108 75 1A 00         [24]  481 	mov	_music_index,#0x00
                                    482 ;	main.c:39: timer1_count=-1;
      00010B 75 18 FF         [24]  483 	mov	_timer1_count,#0xff
      00010E 75 19 FF         [24]  484 	mov	(_timer1_count + 1),#0xff
                                    485 ;	main.c:41: for(int i=7;i<16;i++){
      000111 7E 07            [12]  486 	mov	r6,#0x07
      000113 7F 00            [12]  487 	mov	r7,#0x00
      000115                        488 00104$:
      000115 C3               [12]  489 	clr	c
      000116 EE               [12]  490 	mov	a,r6
      000117 94 10            [12]  491 	subb	a,#0x10
      000119 EF               [12]  492 	mov	a,r7
      00011A 64 80            [12]  493 	xrl	a,#0x80
      00011C 94 80            [12]  494 	subb	a,#0x80
      00011E 50 2C            [24]  495 	jnc	00101$
                                    496 ;	main.c:42: table[i]=table[i-7]*2;
      000120 EE               [12]  497 	mov	a,r6
      000121 2E               [12]  498 	add	a,r6
      000122 FC               [12]  499 	mov	r4,a
      000123 EF               [12]  500 	mov	a,r7
      000124 33               [12]  501 	rlc	a
      000125 EC               [12]  502 	mov	a,r4
      000126 24 1D            [12]  503 	add	a,#_table
      000128 F9               [12]  504 	mov	r1,a
      000129 8E 05            [24]  505 	mov	ar5,r6
      00012B ED               [12]  506 	mov	a,r5
      00012C 24 F9            [12]  507 	add	a,#0xf9
      00012E 25 E0            [12]  508 	add	a,acc
      000130 24 1D            [12]  509 	add	a,#_table
      000132 F8               [12]  510 	mov	r0,a
      000133 86 04            [24]  511 	mov	ar4,@r0
      000135 08               [12]  512 	inc	r0
      000136 86 05            [24]  513 	mov	ar5,@r0
      000138 18               [12]  514 	dec	r0
      000139 EC               [12]  515 	mov	a,r4
      00013A 2C               [12]  516 	add	a,r4
      00013B FC               [12]  517 	mov	r4,a
      00013C ED               [12]  518 	mov	a,r5
      00013D 33               [12]  519 	rlc	a
      00013E FD               [12]  520 	mov	r5,a
      00013F A7 04            [24]  521 	mov	@r1,ar4
      000141 09               [12]  522 	inc	r1
      000142 A7 05            [24]  523 	mov	@r1,ar5
      000144 19               [12]  524 	dec	r1
                                    525 ;	main.c:41: for(int i=7;i<16;i++){
      000145 0E               [12]  526 	inc	r6
      000146 BE 00 CC         [24]  527 	cjne	r6,#0x00,00104$
      000149 0F               [12]  528 	inc	r7
      00014A 80 C9            [24]  529 	sjmp	00104$
      00014C                        530 00101$:
                                    531 ;	main.c:44: for(int i=0;i<16;i++){
      00014C 7E 00            [12]  532 	mov	r6,#0x00
      00014E 7F 00            [12]  533 	mov	r7,#0x00
      000150                        534 00107$:
      000150 C3               [12]  535 	clr	c
      000151 EE               [12]  536 	mov	a,r6
      000152 94 10            [12]  537 	subb	a,#0x10
      000154 EF               [12]  538 	mov	a,r7
      000155 64 80            [12]  539 	xrl	a,#0x80
      000157 94 80            [12]  540 	subb	a,#0x80
      000159 40 01            [24]  541 	jc	00131$
      00015B 22               [24]  542 	ret
      00015C                        543 00131$:
                                    544 ;	main.c:45: tmp=1.0/table[i]*1000000;
      00015C EE               [12]  545 	mov	a,r6
      00015D 2E               [12]  546 	add	a,r6
      00015E FC               [12]  547 	mov	r4,a
      00015F EF               [12]  548 	mov	a,r7
      000160 33               [12]  549 	rlc	a
      000161 EC               [12]  550 	mov	a,r4
      000162 24 1D            [12]  551 	add	a,#_table
      000164 F9               [12]  552 	mov	r1,a
      000165 87 82            [24]  553 	mov	dpl,@r1
      000167 09               [12]  554 	inc	r1
      000168 87 83            [24]  555 	mov	dph,@r1
      00016A 19               [12]  556 	dec	r1
      00016B C0 07            [24]  557 	push	ar7
      00016D C0 06            [24]  558 	push	ar6
      00016F C0 01            [24]  559 	push	ar1
      000171 12 03 34         [24]  560 	lcall	___sint2fs
      000174 AA 82            [24]  561 	mov	r2,dpl
      000176 AB 83            [24]  562 	mov	r3,dph
      000178 AC F0            [24]  563 	mov	r4,b
      00017A FD               [12]  564 	mov	r5,a
      00017B C0 02            [24]  565 	push	ar2
      00017D C0 03            [24]  566 	push	ar3
      00017F C0 04            [24]  567 	push	ar4
      000181 C0 05            [24]  568 	push	ar5
      000183 90 00 00         [24]  569 	mov	dptr,#0x0000
      000186 75 F0 80         [24]  570 	mov	b,#0x80
      000189 74 3F            [12]  571 	mov	a,#0x3f
      00018B 12 03 C4         [24]  572 	lcall	___fsdiv
      00018E AA 82            [24]  573 	mov	r2,dpl
      000190 AB 83            [24]  574 	mov	r3,dph
      000192 AC F0            [24]  575 	mov	r4,b
      000194 FD               [12]  576 	mov	r5,a
      000195 E5 81            [12]  577 	mov	a,sp
      000197 24 FC            [12]  578 	add	a,#0xfc
      000199 F5 81            [12]  579 	mov	sp,a
      00019B C0 02            [24]  580 	push	ar2
      00019D C0 03            [24]  581 	push	ar3
      00019F C0 04            [24]  582 	push	ar4
      0001A1 C0 05            [24]  583 	push	ar5
      0001A3 90 24 00         [24]  584 	mov	dptr,#0x2400
      0001A6 75 F0 74         [24]  585 	mov	b,#0x74
      0001A9 74 49            [12]  586 	mov	a,#0x49
      0001AB 12 02 30         [24]  587 	lcall	___fsmul
      0001AE AA 82            [24]  588 	mov	r2,dpl
      0001B0 AB 83            [24]  589 	mov	r3,dph
      0001B2 AC F0            [24]  590 	mov	r4,b
      0001B4 FD               [12]  591 	mov	r5,a
      0001B5 E5 81            [12]  592 	mov	a,sp
      0001B7 24 FC            [12]  593 	add	a,#0xfc
      0001B9 F5 81            [12]  594 	mov	sp,a
                                    595 ;	main.c:46: table[i]=tmp;
      0001BB 8A 82            [24]  596 	mov	dpl,r2
      0001BD 8B 83            [24]  597 	mov	dph,r3
      0001BF 8C F0            [24]  598 	mov	b,r4
      0001C1 ED               [12]  599 	mov	a,r5
      0001C2 12 03 41         [24]  600 	lcall	___fs2sint
      0001C5 E5 82            [12]  601 	mov	a,dpl
      0001C7 85 83 F0         [24]  602 	mov	b,dph
      0001CA D0 01            [24]  603 	pop	ar1
      0001CC D0 06            [24]  604 	pop	ar6
      0001CE D0 07            [24]  605 	pop	ar7
      0001D0 F7               [12]  606 	mov	@r1,a
      0001D1 09               [12]  607 	inc	r1
      0001D2 A7 F0            [24]  608 	mov	@r1,b
      0001D4 19               [12]  609 	dec	r1
                                    610 ;	main.c:44: for(int i=0;i<16;i++){
      0001D5 0E               [12]  611 	inc	r6
      0001D6 BE 00 01         [24]  612 	cjne	r6,#0x00,00132$
      0001D9 0F               [12]  613 	inc	r7
      0001DA                        614 00132$:
                                    615 ;	main.c:48: }
      0001DA 02 01 50         [24]  616 	ljmp	00107$
                                    617 ;------------------------------------------------------------
                                    618 ;Allocation info for local variables in function 'main'
                                    619 ;------------------------------------------------------------
                                    620 ;	main.c:49: int main(){
                                    621 ;	-----------------------------------------
                                    622 ;	 function main
                                    623 ;	-----------------------------------------
      0001DD                        624 _main:
                                    625 ;	main.c:50: init();
      0001DD 12 01 08         [24]  626 	lcall	_init
                                    627 ;	main.c:51: TMOD = 0b00010001;
      0001E0 75 89 11         [24]  628 	mov	_TMOD,#0x11
                                    629 ;	main.c:52: IE   = 0x8A;
      0001E3 75 A8 8A         [24]  630 	mov	_IE,#0x8a
                                    631 ;	main.c:53: TR0  = 1;
                                    632 ;	assignBit
      0001E6 D2 8C            [12]  633 	setb	_TR0
                                    634 ;	main.c:54: TR1  = 1;
                                    635 ;	assignBit
      0001E8 D2 8E            [12]  636 	setb	_TR1
                                    637 ;	main.c:55: TH0  = PERIOD >> 8;
      0001EA 75 8C 00         [24]  638 	mov	_TH0,#0x00
                                    639 ;	main.c:56: TL0  = PERIOD & 0xff;
      0001ED 75 8A 00         [24]  640 	mov	_TL0,#0x00
                                    641 ;	main.c:57: P2_7=0;
                                    642 ;	assignBit
      0001F0 C2 A7            [12]  643 	clr	_P2_7
                                    644 ;	main.c:58: isSound=1;
      0001F2 75 1B 01         [24]  645 	mov	_isSound,#0x01
      0001F5 75 1C 00         [24]  646 	mov	(_isSound + 1),#0x00
                                    647 ;	main.c:59: while (1){
      0001F8                        648 00110$:
                                    649 ;	main.c:60: EA = 0;
                                    650 ;	assignBit
      0001F8 C2 AF            [12]  651 	clr	_EA
                                    652 ;	main.c:61: if (counter == 1 ) {
      0001FA 74 01            [12]  653 	mov	a,#0x01
      0001FC B5 3D 11         [24]  654 	cjne	a,_counter,00104$
                                    655 ;	main.c:62: counter = 0;
      0001FF 75 3D 00         [24]  656 	mov	_counter,#0x00
                                    657 ;	main.c:63: if(music[music_index]!=16)
      000202 E5 1A            [12]  658 	mov	a,_music_index
      000204 90 05 68         [24]  659 	mov	dptr,#_music
      000207 93               [24]  660 	movc	a,@a+dptr
      000208 FF               [12]  661 	mov	r7,a
      000209 BF 10 02         [24]  662 	cjne	r7,#0x10,00136$
      00020C 80 02            [24]  663 	sjmp	00104$
      00020E                        664 00136$:
                                    665 ;	main.c:64: P2_7=!P2_7;
      00020E B2 A7            [12]  666 	cpl	_P2_7
      000210                        667 00104$:
                                    668 ;	main.c:66: if(timer1_count == 10){
      000210 74 0A            [12]  669 	mov	a,#0x0a
      000212 B5 18 06         [24]  670 	cjne	a,_timer1_count,00137$
      000215 E4               [12]  671 	clr	a
      000216 B5 19 02         [24]  672 	cjne	a,(_timer1_count + 1),00137$
      000219 80 02            [24]  673 	sjmp	00138$
      00021B                        674 00137$:
      00021B 80 0F            [24]  675 	sjmp	00108$
      00021D                        676 00138$:
                                    677 ;	main.c:67: music_index++;
      00021D 05 1A            [12]  678 	inc	_music_index
                                    679 ;	main.c:68: timer1_count=0;
      00021F E4               [12]  680 	clr	a
      000220 F5 18            [12]  681 	mov	_timer1_count,a
      000222 F5 19            [12]  682 	mov	(_timer1_count + 1),a
                                    683 ;	main.c:69: if(music_index == 96)
      000224 74 60            [12]  684 	mov	a,#0x60
      000226 B5 1A 03         [24]  685 	cjne	a,_music_index,00108$
                                    686 ;	main.c:70: music_index = 0;
      000229 75 1A 00         [24]  687 	mov	_music_index,#0x00
      00022C                        688 00108$:
                                    689 ;	main.c:72: EA = 1;
                                    690 ;	assignBit
      00022C D2 AF            [12]  691 	setb	_EA
                                    692 ;	main.c:74: return 0;
                                    693 ;	main.c:75: }
      00022E 80 C8            [24]  694 	sjmp	00110$
                                    695 	.area CSEG    (CODE)
                                    696 	.area CONST   (CODE)
      000568                        697 _music:
      000568 0A                     698 	.db #0x0a	; 10
      000569 0A                     699 	.db #0x0a	; 10
      00056A 0A                     700 	.db #0x0a	; 10
      00056B 0A                     701 	.db #0x0a	; 10
      00056C 09                     702 	.db #0x09	; 9
      00056D 08                     703 	.db #0x08	; 8
      00056E 08                     704 	.db #0x08	; 8
      00056F 07                     705 	.db #0x07	; 7
      000570 06                     706 	.db #0x06	; 6
      000571 06                     707 	.db #0x06	; 6
      000572 08                     708 	.db #0x08	; 8
      000573 0A                     709 	.db #0x0a	; 10
      000574 0D                     710 	.db #0x0d	; 13
      000575 0D                     711 	.db #0x0d	; 13
      000576 0D                     712 	.db #0x0d	; 13
      000577 0D                     713 	.db #0x0d	; 13
      000578 0C                     714 	.db #0x0c	; 12
      000579 0B                     715 	.db #0x0b	; 11
      00057A 0B                     716 	.db #0x0b	; 11
      00057B 0A                     717 	.db #0x0a	; 10
      00057C 09                     718 	.db #0x09	; 9
      00057D 09                     719 	.db #0x09	; 9
      00057E 0A                     720 	.db #0x0a	; 10
      00057F 0B                     721 	.db #0x0b	; 11
      000580 0A                     722 	.db #0x0a	; 10
      000581 0B                     723 	.db #0x0b	; 11
      000582 0A                     724 	.db #0x0a	; 10
      000583 0C                     725 	.db #0x0c	; 12
      000584 0B                     726 	.db #0x0b	; 11
      000585 0A                     727 	.db #0x0a	; 10
      000586 0A                     728 	.db #0x0a	; 10
      000587 09                     729 	.db #0x09	; 9
      000588 08                     730 	.db #0x08	; 8
      000589 08                     731 	.db #0x08	; 8
      00058A 07                     732 	.db #0x07	; 7
      00058B 06                     733 	.db #0x06	; 6
      00058C 07                     734 	.db #0x07	; 7
      00058D 07                     735 	.db #0x07	; 7
      00058E 07                     736 	.db #0x07	; 7
      00058F 07                     737 	.db #0x07	; 7
      000590 08                     738 	.db #0x08	; 8
      000591 07                     739 	.db #0x07	; 7
      000592 06                     740 	.db #0x06	; 6
      000593 10                     741 	.db #0x10	; 16
      000594 10                     742 	.db #0x10	; 16
      000595 06                     743 	.db #0x06	; 6
      000596 10                     744 	.db #0x10	; 16
      000597 10                     745 	.db #0x10	; 16
      000598 0A                     746 	.db #0x0a	; 10
      000599 0A                     747 	.db #0x0a	; 10
      00059A 0A                     748 	.db #0x0a	; 10
      00059B 0A                     749 	.db #0x0a	; 10
      00059C 09                     750 	.db #0x09	; 9
      00059D 08                     751 	.db #0x08	; 8
      00059E 08                     752 	.db #0x08	; 8
      00059F 07                     753 	.db #0x07	; 7
      0005A0 07                     754 	.db #0x07	; 7
      0005A1 07                     755 	.db #0x07	; 7
      0005A2 07                     756 	.db #0x07	; 7
      0005A3 07                     757 	.db #0x07	; 7
      0005A4 0D                     758 	.db #0x0d	; 13
      0005A5 0D                     759 	.db #0x0d	; 13
      0005A6 0D                     760 	.db #0x0d	; 13
      0005A7 0D                     761 	.db #0x0d	; 13
      0005A8 0E                     762 	.db #0x0e	; 14
      0005A9 0D                     763 	.db #0x0d	; 13
      0005AA 0D                     764 	.db #0x0d	; 13
      0005AB 0C                     765 	.db #0x0c	; 12
      0005AC 0C                     766 	.db #0x0c	; 12
      0005AD 0C                     767 	.db #0x0c	; 12
      0005AE 0D                     768 	.db #0x0d	; 13
      0005AF 0E                     769 	.db #0x0e	; 14
      0005B0 0F                     770 	.db #0x0f	; 15
      0005B1 0F                     771 	.db #0x0f	; 15
      0005B2 0F                     772 	.db #0x0f	; 15
      0005B3 0F                     773 	.db #0x0f	; 15
      0005B4 0E                     774 	.db #0x0e	; 14
      0005B5 0E                     775 	.db #0x0e	; 14
      0005B6 0D                     776 	.db #0x0d	; 13
      0005B7 0D                     777 	.db #0x0d	; 13
      0005B8 0D                     778 	.db #0x0d	; 13
      0005B9 0D                     779 	.db #0x0d	; 13
      0005BA 0C                     780 	.db #0x0c	; 12
      0005BB 0B                     781 	.db #0x0b	; 11
      0005BC 0A                     782 	.db #0x0a	; 10
      0005BD 0A                     783 	.db #0x0a	; 10
      0005BE 0A                     784 	.db #0x0a	; 10
      0005BF 0A                     785 	.db #0x0a	; 10
      0005C0 0B                     786 	.db #0x0b	; 11
      0005C1 09                     787 	.db #0x09	; 9
      0005C2 08                     788 	.db #0x08	; 8
      0005C3 10                     789 	.db #0x10	; 16
      0005C4 10                     790 	.db #0x10	; 16
      0005C5 08                     791 	.db #0x08	; 8
      0005C6 10                     792 	.db #0x10	; 16
      0005C7 10                     793 	.db #0x10	; 16
                                    794 	.area XINIT   (CODE)
                                    795 	.area CABS    (ABS,CODE)
