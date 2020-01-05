                                      1 ;--------------------------------------------------------
                                      2 ; File Created by SDCC : free open source ANSI-C Compiler
                                      3 ; Version 3.8.0 #10562 (MINGW64)
                                      4 ;--------------------------------------------------------
                                      5 	.module Lab3_main
                                      6 	.optsdcc -mmcs51 --model-small
                                      7 	
                                      8 ;--------------------------------------------------------
                                      9 ; Public variables in this module
                                     10 ;--------------------------------------------------------
                                     11 	.globl _main
                                     12 	.globl _keyPressed
                                     13 	.globl _LED_Display
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
                                    110 ;--------------------------------------------------------
                                    111 ; special function registers
                                    112 ;--------------------------------------------------------
                                    113 	.area RSEG    (ABS,DATA)
      000000                        114 	.org 0x0000
                           000080   115 _P0	=	0x0080
                           000081   116 _SP	=	0x0081
                           000082   117 _DPL	=	0x0082
                           000083   118 _DPH	=	0x0083
                           000087   119 _PCON	=	0x0087
                           000088   120 _TCON	=	0x0088
                           000089   121 _TMOD	=	0x0089
                           00008A   122 _TL0	=	0x008a
                           00008B   123 _TL1	=	0x008b
                           00008C   124 _TH0	=	0x008c
                           00008D   125 _TH1	=	0x008d
                           000090   126 _P1	=	0x0090
                           000098   127 _SCON	=	0x0098
                           000099   128 _SBUF	=	0x0099
                           0000A0   129 _P2	=	0x00a0
                           0000A8   130 _IE	=	0x00a8
                           0000B0   131 _P3	=	0x00b0
                           0000B8   132 _IP	=	0x00b8
                           0000D0   133 _PSW	=	0x00d0
                           0000E0   134 _ACC	=	0x00e0
                           0000F0   135 _B	=	0x00f0
                                    136 ;--------------------------------------------------------
                                    137 ; special function bits
                                    138 ;--------------------------------------------------------
                                    139 	.area RSEG    (ABS,DATA)
      000000                        140 	.org 0x0000
                           000080   141 _P0_0	=	0x0080
                           000081   142 _P0_1	=	0x0081
                           000082   143 _P0_2	=	0x0082
                           000083   144 _P0_3	=	0x0083
                           000084   145 _P0_4	=	0x0084
                           000085   146 _P0_5	=	0x0085
                           000086   147 _P0_6	=	0x0086
                           000087   148 _P0_7	=	0x0087
                           000088   149 _IT0	=	0x0088
                           000089   150 _IE0	=	0x0089
                           00008A   151 _IT1	=	0x008a
                           00008B   152 _IE1	=	0x008b
                           00008C   153 _TR0	=	0x008c
                           00008D   154 _TF0	=	0x008d
                           00008E   155 _TR1	=	0x008e
                           00008F   156 _TF1	=	0x008f
                           000090   157 _P1_0	=	0x0090
                           000091   158 _P1_1	=	0x0091
                           000092   159 _P1_2	=	0x0092
                           000093   160 _P1_3	=	0x0093
                           000094   161 _P1_4	=	0x0094
                           000095   162 _P1_5	=	0x0095
                           000096   163 _P1_6	=	0x0096
                           000097   164 _P1_7	=	0x0097
                           000098   165 _RI	=	0x0098
                           000099   166 _TI	=	0x0099
                           00009A   167 _RB8	=	0x009a
                           00009B   168 _TB8	=	0x009b
                           00009C   169 _REN	=	0x009c
                           00009D   170 _SM2	=	0x009d
                           00009E   171 _SM1	=	0x009e
                           00009F   172 _SM0	=	0x009f
                           0000A0   173 _P2_0	=	0x00a0
                           0000A1   174 _P2_1	=	0x00a1
                           0000A2   175 _P2_2	=	0x00a2
                           0000A3   176 _P2_3	=	0x00a3
                           0000A4   177 _P2_4	=	0x00a4
                           0000A5   178 _P2_5	=	0x00a5
                           0000A6   179 _P2_6	=	0x00a6
                           0000A7   180 _P2_7	=	0x00a7
                           0000A8   181 _EX0	=	0x00a8
                           0000A9   182 _ET0	=	0x00a9
                           0000AA   183 _EX1	=	0x00aa
                           0000AB   184 _ET1	=	0x00ab
                           0000AC   185 _ES	=	0x00ac
                           0000AF   186 _EA	=	0x00af
                           0000B0   187 _P3_0	=	0x00b0
                           0000B1   188 _P3_1	=	0x00b1
                           0000B2   189 _P3_2	=	0x00b2
                           0000B3   190 _P3_3	=	0x00b3
                           0000B4   191 _P3_4	=	0x00b4
                           0000B5   192 _P3_5	=	0x00b5
                           0000B6   193 _P3_6	=	0x00b6
                           0000B7   194 _P3_7	=	0x00b7
                           0000B0   195 _RXD	=	0x00b0
                           0000B1   196 _TXD	=	0x00b1
                           0000B2   197 _INT0	=	0x00b2
                           0000B3   198 _INT1	=	0x00b3
                           0000B4   199 _T0	=	0x00b4
                           0000B5   200 _T1	=	0x00b5
                           0000B6   201 _WR	=	0x00b6
                           0000B7   202 _RD	=	0x00b7
                           0000B8   203 _PX0	=	0x00b8
                           0000B9   204 _PT0	=	0x00b9
                           0000BA   205 _PX1	=	0x00ba
                           0000BB   206 _PT1	=	0x00bb
                           0000BC   207 _PS	=	0x00bc
                           0000D0   208 _P	=	0x00d0
                           0000D1   209 _F1	=	0x00d1
                           0000D2   210 _OV	=	0x00d2
                           0000D3   211 _RS0	=	0x00d3
                           0000D4   212 _RS1	=	0x00d4
                           0000D5   213 _F0	=	0x00d5
                           0000D6   214 _AC	=	0x00d6
                           0000D7   215 _CY	=	0x00d7
                                    216 ;--------------------------------------------------------
                                    217 ; overlayable register banks
                                    218 ;--------------------------------------------------------
                                    219 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                        220 	.ds 8
                                    221 ;--------------------------------------------------------
                                    222 ; internal ram data
                                    223 ;--------------------------------------------------------
                                    224 	.area DSEG    (DATA)
      000008                        225 _main_table_65536_3:
      000008                        226 	.ds 8
      000010                        227 _main_num_65536_3:
      000010                        228 	.ds 8
      000018                        229 _main_row_65536_3:
      000018                        230 	.ds 2
      00001A                        231 _main_previous_65537_4:
      00001A                        232 	.ds 2
                                    233 ;--------------------------------------------------------
                                    234 ; overlayable items in internal ram 
                                    235 ;--------------------------------------------------------
                                    236 ;--------------------------------------------------------
                                    237 ; Stack segment in internal ram 
                                    238 ;--------------------------------------------------------
                                    239 	.area	SSEG
      000022                        240 __start__stack:
      000022                        241 	.ds	1
                                    242 
                                    243 ;--------------------------------------------------------
                                    244 ; indirectly addressable internal ram data
                                    245 ;--------------------------------------------------------
                                    246 	.area ISEG    (DATA)
                                    247 ;--------------------------------------------------------
                                    248 ; absolute internal ram data
                                    249 ;--------------------------------------------------------
                                    250 	.area IABS    (ABS,DATA)
                                    251 	.area IABS    (ABS,DATA)
                                    252 ;--------------------------------------------------------
                                    253 ; bit data
                                    254 ;--------------------------------------------------------
                                    255 	.area BSEG    (BIT)
                                    256 ;--------------------------------------------------------
                                    257 ; paged external ram data
                                    258 ;--------------------------------------------------------
                                    259 	.area PSEG    (PAG,XDATA)
                                    260 ;--------------------------------------------------------
                                    261 ; external ram data
                                    262 ;--------------------------------------------------------
                                    263 	.area XSEG    (XDATA)
                                    264 ;--------------------------------------------------------
                                    265 ; absolute external ram data
                                    266 ;--------------------------------------------------------
                                    267 	.area XABS    (ABS,XDATA)
                                    268 ;--------------------------------------------------------
                                    269 ; external initialized ram data
                                    270 ;--------------------------------------------------------
                                    271 	.area XISEG   (XDATA)
                                    272 	.area HOME    (CODE)
                                    273 	.area GSINIT0 (CODE)
                                    274 	.area GSINIT1 (CODE)
                                    275 	.area GSINIT2 (CODE)
                                    276 	.area GSINIT3 (CODE)
                                    277 	.area GSINIT4 (CODE)
                                    278 	.area GSINIT5 (CODE)
                                    279 	.area GSINIT  (CODE)
                                    280 	.area GSFINAL (CODE)
                                    281 	.area CSEG    (CODE)
                                    282 ;--------------------------------------------------------
                                    283 ; interrupt vector 
                                    284 ;--------------------------------------------------------
                                    285 	.area HOME    (CODE)
      000000                        286 __interrupt_vect:
      000000 02 00 06         [24]  287 	ljmp	__sdcc_gsinit_startup
                                    288 ;--------------------------------------------------------
                                    289 ; global & static initialisations
                                    290 ;--------------------------------------------------------
                                    291 	.area HOME    (CODE)
                                    292 	.area GSINIT  (CODE)
                                    293 	.area GSFINAL (CODE)
                                    294 	.area GSINIT  (CODE)
                                    295 	.globl __sdcc_gsinit_startup
                                    296 	.globl __sdcc_program_startup
                                    297 	.globl __start__stack
                                    298 	.globl __mcs51_genXINIT
                                    299 	.globl __mcs51_genXRAMCLEAR
                                    300 	.globl __mcs51_genRAMCLEAR
                                    301 	.area GSFINAL (CODE)
      00005F 02 00 03         [24]  302 	ljmp	__sdcc_program_startup
                                    303 ;--------------------------------------------------------
                                    304 ; Home
                                    305 ;--------------------------------------------------------
                                    306 	.area HOME    (CODE)
                                    307 	.area HOME    (CODE)
      000003                        308 __sdcc_program_startup:
      000003 02 00 62         [24]  309 	ljmp	_main
                                    310 ;	return from main will return to caller
                                    311 ;--------------------------------------------------------
                                    312 ; code
                                    313 ;--------------------------------------------------------
                                    314 	.area CSEG    (CODE)
                                    315 ;------------------------------------------------------------
                                    316 ;Allocation info for local variables in function 'main'
                                    317 ;------------------------------------------------------------
                                    318 ;table                     Allocated with name '_main_table_65536_3'
                                    319 ;num                       Allocated with name '_main_num_65536_3'
                                    320 ;row                       Allocated with name '_main_row_65536_3'
                                    321 ;count                     Allocated to registers r4 r5 
                                    322 ;number                    Allocated to registers 
                                    323 ;previous                  Allocated with name '_main_previous_65537_4'
                                    324 ;key                       Allocated to registers r2 r3 
                                    325 ;------------------------------------------------------------
                                    326 ;	Lab3-main.c:5: int main() {
                                    327 ;	-----------------------------------------
                                    328 ;	 function main
                                    329 ;	-----------------------------------------
      000062                        330 _main:
                           000007   331 	ar7 = 0x07
                           000006   332 	ar6 = 0x06
                           000005   333 	ar5 = 0x05
                           000004   334 	ar4 = 0x04
                           000003   335 	ar3 = 0x03
                           000002   336 	ar2 = 0x02
                           000001   337 	ar1 = 0x01
                           000000   338 	ar0 = 0x00
                                    339 ;	Lab3-main.c:6: short table[4] = {0x70, 0xb0, 0xd0, 0xe0};
      000062 75 08 70         [24]  340 	mov	(_main_table_65536_3 + 0),#0x70
      000065 75 09 00         [24]  341 	mov	(_main_table_65536_3 + 1),#0x00
      000068 75 0A B0         [24]  342 	mov	((_main_table_65536_3 + 0x0002) + 0),#0xb0
      00006B 75 0B 00         [24]  343 	mov	((_main_table_65536_3 + 0x0002) + 1),#0x00
      00006E 75 0C D0         [24]  344 	mov	((_main_table_65536_3 + 0x0004) + 0),#0xd0
      000071 75 0D 00         [24]  345 	mov	((_main_table_65536_3 + 0x0004) + 1),#0x00
      000074 75 0E E0         [24]  346 	mov	((_main_table_65536_3 + 0x0006) + 0),#0xe0
      000077 75 0F 00         [24]  347 	mov	((_main_table_65536_3 + 0x0006) + 1),#0x00
                                    348 ;	Lab3-main.c:7: short num[4] = {15, 15, 15, 15};
      00007A 75 10 0F         [24]  349 	mov	(_main_num_65536_3 + 0),#0x0f
      00007D 75 11 00         [24]  350 	mov	(_main_num_65536_3 + 1),#0x00
      000080 75 12 0F         [24]  351 	mov	((_main_num_65536_3 + 0x0002) + 0),#0x0f
      000083 75 13 00         [24]  352 	mov	((_main_num_65536_3 + 0x0002) + 1),#0x00
      000086 75 14 0F         [24]  353 	mov	((_main_num_65536_3 + 0x0004) + 0),#0x0f
      000089 75 15 00         [24]  354 	mov	((_main_num_65536_3 + 0x0004) + 1),#0x00
      00008C 75 16 0F         [24]  355 	mov	((_main_num_65536_3 + 0x0006) + 0),#0x0f
                                    356 ;	Lab3-main.c:8: short row = 0;
      00008F E4               [12]  357 	clr	a
      000090 F5 17            [12]  358 	mov	((_main_num_65536_3 + 0x0006) + 1),a
      000092 F5 18            [12]  359 	mov	_main_row_65536_3,a
      000094 F5 19            [12]  360 	mov	(_main_row_65536_3 + 1),a
                                    361 ;	Lab3-main.c:9: P2=0b11111110;
      000096 75 A0 FE         [24]  362 	mov	_P2,#0xfe
                                    363 ;	Lab3-main.c:10: short count = 1;
      000099 7C 01            [12]  364 	mov	r4,#0x01
      00009B 7D 00            [12]  365 	mov	r5,#0x00
                                    366 ;	Lab3-main.c:12: short previous = -1;
      00009D 75 1A FF         [24]  367 	mov	_main_previous_65537_4,#0xff
      0000A0 75 1B FF         [24]  368 	mov	(_main_previous_65537_4 + 1),#0xff
                                    369 ;	Lab3-main.c:13: while (1) {
      0000A3                        370 00107$:
                                    371 ;	Lab3-main.c:14: P2    =count^0b11111111;
      0000A3 74 FF            [12]  372 	mov	a,#0xff
      0000A5 6C               [12]  373 	xrl	a,r4
      0000A6 FA               [12]  374 	mov	r2,a
      0000A7 8D 03            [24]  375 	mov	ar3,r5
      0000A9 8A A0            [24]  376 	mov	_P2,r2
                                    377 ;	Lab3-main.c:15: count *=2;
      0000AB EC               [12]  378 	mov	a,r4
      0000AC 2C               [12]  379 	add	a,r4
      0000AD FC               [12]  380 	mov	r4,a
      0000AE ED               [12]  381 	mov	a,r5
      0000AF 33               [12]  382 	rlc	a
      0000B0 FD               [12]  383 	mov	r5,a
                                    384 ;	Lab3-main.c:16: short key = keyPressed(row);
      0000B1 85 18 82         [24]  385 	mov	dpl,_main_row_65536_3
      0000B4 85 19 83         [24]  386 	mov	dph,(_main_row_65536_3 + 1)
      0000B7 C0 05            [24]  387 	push	ar5
      0000B9 C0 04            [24]  388 	push	ar4
      0000BB 12 01 AD         [24]  389 	lcall	_keyPressed
      0000BE AA 82            [24]  390 	mov	r2,dpl
      0000C0 AB 83            [24]  391 	mov	r3,dph
      0000C2 D0 04            [24]  392 	pop	ar4
      0000C4 D0 05            [24]  393 	pop	ar5
                                    394 ;	Lab3-main.c:17: if (key != -1 && key != previous) {
      0000C6 BA FF 05         [24]  395 	cjne	r2,#0xff,00127$
      0000C9 BB FF 02         [24]  396 	cjne	r3,#0xff,00127$
      0000CC 80 2A            [24]  397 	sjmp	00102$
      0000CE                        398 00127$:
      0000CE EA               [12]  399 	mov	a,r2
      0000CF B5 1A 06         [24]  400 	cjne	a,_main_previous_65537_4,00128$
      0000D2 EB               [12]  401 	mov	a,r3
      0000D3 B5 1B 02         [24]  402 	cjne	a,(_main_previous_65537_4 + 1),00128$
      0000D6 80 20            [24]  403 	sjmp	00102$
      0000D8                        404 00128$:
                                    405 ;	Lab3-main.c:18: previous = key;
      0000D8 8A 1A            [24]  406 	mov	_main_previous_65537_4,r2
      0000DA 8B 1B            [24]  407 	mov	(_main_previous_65537_4 + 1),r3
                                    408 ;	Lab3-main.c:19: num[0] =num[1];
      0000DC AE 12            [24]  409 	mov	r6,((_main_num_65536_3 + 0x0002) + 0)
      0000DE AF 13            [24]  410 	mov	r7,((_main_num_65536_3 + 0x0002) + 1)
      0000E0 8E 10            [24]  411 	mov	(_main_num_65536_3 + 0),r6
      0000E2 8F 11            [24]  412 	mov	(_main_num_65536_3 + 1),r7
                                    413 ;	Lab3-main.c:20: num[1] =num[2];
      0000E4 AE 14            [24]  414 	mov	r6,((_main_num_65536_3 + 0x0004) + 0)
      0000E6 AF 15            [24]  415 	mov	r7,((_main_num_65536_3 + 0x0004) + 1)
      0000E8 8E 12            [24]  416 	mov	((_main_num_65536_3 + 0x0002) + 0),r6
      0000EA 8F 13            [24]  417 	mov	((_main_num_65536_3 + 0x0002) + 1),r7
                                    418 ;	Lab3-main.c:21: num[2] =num[3];			
      0000EC AE 16            [24]  419 	mov	r6,((_main_num_65536_3 + 0x0006) + 0)
      0000EE AF 17            [24]  420 	mov	r7,((_main_num_65536_3 + 0x0006) + 1)
      0000F0 8E 14            [24]  421 	mov	((_main_num_65536_3 + 0x0004) + 0),r6
      0000F2 8F 15            [24]  422 	mov	((_main_num_65536_3 + 0x0004) + 1),r7
                                    423 ;	Lab3-main.c:22: num[3] = key;
      0000F4 8A 16            [24]  424 	mov	((_main_num_65536_3 + 0x0006) + 0),r2
      0000F6 8B 17            [24]  425 	mov	((_main_num_65536_3 + 0x0006) + 1),r3
      0000F8                        426 00102$:
                                    427 ;	Lab3-main.c:24: row++;
      0000F8 05 18            [12]  428 	inc	_main_row_65536_3
      0000FA E4               [12]  429 	clr	a
      0000FB B5 18 02         [24]  430 	cjne	a,_main_row_65536_3,00129$
      0000FE 05 19            [12]  431 	inc	(_main_row_65536_3 + 1)
      000100                        432 00129$:
                                    433 ;	Lab3-main.c:25: if (count == 0x10) {
      000100 BC 10 0B         [24]  434 	cjne	r4,#0x10,00105$
      000103 BD 00 08         [24]  435 	cjne	r5,#0x00,00105$
                                    436 ;	Lab3-main.c:26: count = 1;
      000106 7C 01            [12]  437 	mov	r4,#0x01
                                    438 ;	Lab3-main.c:27: row   = 0;
      000108 E4               [12]  439 	clr	a
      000109 FD               [12]  440 	mov	r5,a
      00010A F5 18            [12]  441 	mov	_main_row_65536_3,a
      00010C F5 19            [12]  442 	mov	(_main_row_65536_3 + 1),a
      00010E                        443 00105$:
                                    444 ;	Lab3-main.c:29: LED_Display(table,num);
      00010E 75 1C 10         [24]  445 	mov	_LED_Display_PARM_2,#_main_num_65536_3
      000111 75 1D 00         [24]  446 	mov	(_LED_Display_PARM_2 + 1),#0x00
      000114 75 1E 40         [24]  447 	mov	(_LED_Display_PARM_2 + 2),#0x40
      000117 90 00 08         [24]  448 	mov	dptr,#_main_table_65536_3
      00011A 75 F0 40         [24]  449 	mov	b,#0x40
      00011D C0 05            [24]  450 	push	ar5
      00011F C0 04            [24]  451 	push	ar4
      000121 12 01 2B         [24]  452 	lcall	_LED_Display
      000124 D0 04            [24]  453 	pop	ar4
      000126 D0 05            [24]  454 	pop	ar5
                                    455 ;	Lab3-main.c:31: }
      000128 02 00 A3         [24]  456 	ljmp	00107$
                                    457 	.area CSEG    (CODE)
                                    458 	.area CONST   (CODE)
                                    459 	.area XINIT   (CODE)
                                    460 	.area CABS    (ABS,CODE)
