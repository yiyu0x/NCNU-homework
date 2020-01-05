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
                                     11 	.globl _LED_Display_PARM_2
                                     12 	.globl _SPIN
                                     13 	.globl _main
                                     14 	.globl _LED_Display
                                     15 	.globl _keyPressed
                                     16 	.globl _timer_isr
                                     17 	.globl _delay
                                     18 	.globl _CY
                                     19 	.globl _AC
                                     20 	.globl _F0
                                     21 	.globl _RS1
                                     22 	.globl _RS0
                                     23 	.globl _OV
                                     24 	.globl _F1
                                     25 	.globl _P
                                     26 	.globl _PS
                                     27 	.globl _PT1
                                     28 	.globl _PX1
                                     29 	.globl _PT0
                                     30 	.globl _PX0
                                     31 	.globl _RD
                                     32 	.globl _WR
                                     33 	.globl _T1
                                     34 	.globl _T0
                                     35 	.globl _INT1
                                     36 	.globl _INT0
                                     37 	.globl _TXD
                                     38 	.globl _RXD
                                     39 	.globl _P3_7
                                     40 	.globl _P3_6
                                     41 	.globl _P3_5
                                     42 	.globl _P3_4
                                     43 	.globl _P3_3
                                     44 	.globl _P3_2
                                     45 	.globl _P3_1
                                     46 	.globl _P3_0
                                     47 	.globl _EA
                                     48 	.globl _ES
                                     49 	.globl _ET1
                                     50 	.globl _EX1
                                     51 	.globl _ET0
                                     52 	.globl _EX0
                                     53 	.globl _P2_7
                                     54 	.globl _P2_6
                                     55 	.globl _P2_5
                                     56 	.globl _P2_4
                                     57 	.globl _P2_3
                                     58 	.globl _P2_2
                                     59 	.globl _P2_1
                                     60 	.globl _P2_0
                                     61 	.globl _SM0
                                     62 	.globl _SM1
                                     63 	.globl _SM2
                                     64 	.globl _REN
                                     65 	.globl _TB8
                                     66 	.globl _RB8
                                     67 	.globl _TI
                                     68 	.globl _RI
                                     69 	.globl _P1_7
                                     70 	.globl _P1_6
                                     71 	.globl _P1_5
                                     72 	.globl _P1_4
                                     73 	.globl _P1_3
                                     74 	.globl _P1_2
                                     75 	.globl _P1_1
                                     76 	.globl _P1_0
                                     77 	.globl _TF1
                                     78 	.globl _TR1
                                     79 	.globl _TF0
                                     80 	.globl _TR0
                                     81 	.globl _IE1
                                     82 	.globl _IT1
                                     83 	.globl _IE0
                                     84 	.globl _IT0
                                     85 	.globl _P0_7
                                     86 	.globl _P0_6
                                     87 	.globl _P0_5
                                     88 	.globl _P0_4
                                     89 	.globl _P0_3
                                     90 	.globl _P0_2
                                     91 	.globl _P0_1
                                     92 	.globl _P0_0
                                     93 	.globl _B
                                     94 	.globl _ACC
                                     95 	.globl _PSW
                                     96 	.globl _IP
                                     97 	.globl _P3
                                     98 	.globl _IE
                                     99 	.globl _P2
                                    100 	.globl _SBUF
                                    101 	.globl _SCON
                                    102 	.globl _P1
                                    103 	.globl _TH1
                                    104 	.globl _TH0
                                    105 	.globl _TL1
                                    106 	.globl _TL0
                                    107 	.globl _TMOD
                                    108 	.globl _TCON
                                    109 	.globl _PCON
                                    110 	.globl _DPH
                                    111 	.globl _DPL
                                    112 	.globl _SP
                                    113 	.globl _P0
                                    114 	.globl _speed
                                    115 	.globl _step
                                    116 	.globl _direct
                                    117 	.globl _max
                                    118 	.globl _count
                                    119 ;--------------------------------------------------------
                                    120 ; special function registers
                                    121 ;--------------------------------------------------------
                                    122 	.area RSEG    (ABS,DATA)
      000000                        123 	.org 0x0000
                           000080   124 _P0	=	0x0080
                           000081   125 _SP	=	0x0081
                           000082   126 _DPL	=	0x0082
                           000083   127 _DPH	=	0x0083
                           000087   128 _PCON	=	0x0087
                           000088   129 _TCON	=	0x0088
                           000089   130 _TMOD	=	0x0089
                           00008A   131 _TL0	=	0x008a
                           00008B   132 _TL1	=	0x008b
                           00008C   133 _TH0	=	0x008c
                           00008D   134 _TH1	=	0x008d
                           000090   135 _P1	=	0x0090
                           000098   136 _SCON	=	0x0098
                           000099   137 _SBUF	=	0x0099
                           0000A0   138 _P2	=	0x00a0
                           0000A8   139 _IE	=	0x00a8
                           0000B0   140 _P3	=	0x00b0
                           0000B8   141 _IP	=	0x00b8
                           0000D0   142 _PSW	=	0x00d0
                           0000E0   143 _ACC	=	0x00e0
                           0000F0   144 _B	=	0x00f0
                                    145 ;--------------------------------------------------------
                                    146 ; special function bits
                                    147 ;--------------------------------------------------------
                                    148 	.area RSEG    (ABS,DATA)
      000000                        149 	.org 0x0000
                           000080   150 _P0_0	=	0x0080
                           000081   151 _P0_1	=	0x0081
                           000082   152 _P0_2	=	0x0082
                           000083   153 _P0_3	=	0x0083
                           000084   154 _P0_4	=	0x0084
                           000085   155 _P0_5	=	0x0085
                           000086   156 _P0_6	=	0x0086
                           000087   157 _P0_7	=	0x0087
                           000088   158 _IT0	=	0x0088
                           000089   159 _IE0	=	0x0089
                           00008A   160 _IT1	=	0x008a
                           00008B   161 _IE1	=	0x008b
                           00008C   162 _TR0	=	0x008c
                           00008D   163 _TF0	=	0x008d
                           00008E   164 _TR1	=	0x008e
                           00008F   165 _TF1	=	0x008f
                           000090   166 _P1_0	=	0x0090
                           000091   167 _P1_1	=	0x0091
                           000092   168 _P1_2	=	0x0092
                           000093   169 _P1_3	=	0x0093
                           000094   170 _P1_4	=	0x0094
                           000095   171 _P1_5	=	0x0095
                           000096   172 _P1_6	=	0x0096
                           000097   173 _P1_7	=	0x0097
                           000098   174 _RI	=	0x0098
                           000099   175 _TI	=	0x0099
                           00009A   176 _RB8	=	0x009a
                           00009B   177 _TB8	=	0x009b
                           00009C   178 _REN	=	0x009c
                           00009D   179 _SM2	=	0x009d
                           00009E   180 _SM1	=	0x009e
                           00009F   181 _SM0	=	0x009f
                           0000A0   182 _P2_0	=	0x00a0
                           0000A1   183 _P2_1	=	0x00a1
                           0000A2   184 _P2_2	=	0x00a2
                           0000A3   185 _P2_3	=	0x00a3
                           0000A4   186 _P2_4	=	0x00a4
                           0000A5   187 _P2_5	=	0x00a5
                           0000A6   188 _P2_6	=	0x00a6
                           0000A7   189 _P2_7	=	0x00a7
                           0000A8   190 _EX0	=	0x00a8
                           0000A9   191 _ET0	=	0x00a9
                           0000AA   192 _EX1	=	0x00aa
                           0000AB   193 _ET1	=	0x00ab
                           0000AC   194 _ES	=	0x00ac
                           0000AF   195 _EA	=	0x00af
                           0000B0   196 _P3_0	=	0x00b0
                           0000B1   197 _P3_1	=	0x00b1
                           0000B2   198 _P3_2	=	0x00b2
                           0000B3   199 _P3_3	=	0x00b3
                           0000B4   200 _P3_4	=	0x00b4
                           0000B5   201 _P3_5	=	0x00b5
                           0000B6   202 _P3_6	=	0x00b6
                           0000B7   203 _P3_7	=	0x00b7
                           0000B0   204 _RXD	=	0x00b0
                           0000B1   205 _TXD	=	0x00b1
                           0000B2   206 _INT0	=	0x00b2
                           0000B3   207 _INT1	=	0x00b3
                           0000B4   208 _T0	=	0x00b4
                           0000B5   209 _T1	=	0x00b5
                           0000B6   210 _WR	=	0x00b6
                           0000B7   211 _RD	=	0x00b7
                           0000B8   212 _PX0	=	0x00b8
                           0000B9   213 _PT0	=	0x00b9
                           0000BA   214 _PX1	=	0x00ba
                           0000BB   215 _PT1	=	0x00bb
                           0000BC   216 _PS	=	0x00bc
                           0000D0   217 _P	=	0x00d0
                           0000D1   218 _F1	=	0x00d1
                           0000D2   219 _OV	=	0x00d2
                           0000D3   220 _RS0	=	0x00d3
                           0000D4   221 _RS1	=	0x00d4
                           0000D5   222 _F0	=	0x00d5
                           0000D6   223 _AC	=	0x00d6
                           0000D7   224 _CY	=	0x00d7
                                    225 ;--------------------------------------------------------
                                    226 ; overlayable register banks
                                    227 ;--------------------------------------------------------
                                    228 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                        229 	.ds 8
                                    230 	.area REG_BANK_1	(REL,OVR,DATA)
      000008                        231 	.ds 8
                                    232 ;--------------------------------------------------------
                                    233 ; internal ram data
                                    234 ;--------------------------------------------------------
                                    235 	.area DSEG    (DATA)
      000010                        236 _count::
      000010                        237 	.ds 2
      000012                        238 _max::
      000012                        239 	.ds 2
      000014                        240 _direct::
      000014                        241 	.ds 1
      000015                        242 _step::
      000015                        243 	.ds 1
      000016                        244 _speed::
      000016                        245 	.ds 2
      000018                        246 _main_table_65537_51:
      000018                        247 	.ds 8
      000020                        248 _main_num_65537_51:
      000020                        249 	.ds 8
      000028                        250 _main_row_65537_51:
      000028                        251 	.ds 2
      00002A                        252 _main_cnt_65538_52:
      00002A                        253 	.ds 2
      00002C                        254 _main_previous_65538_52:
      00002C                        255 	.ds 2
      00002E                        256 _main_previous2_65538_52:
      00002E                        257 	.ds 2
                                    258 ;--------------------------------------------------------
                                    259 ; overlayable items in internal ram 
                                    260 ;--------------------------------------------------------
                                    261 	.area	OSEG    (OVR,DATA)
                                    262 	.area	OSEG    (OVR,DATA)
      000030                        263 _keyPressed_row_65536_38:
      000030                        264 	.ds 2
                                    265 	.area	OSEG    (OVR,DATA)
      000030                        266 _LED_Display_PARM_2:
      000030                        267 	.ds 3
      000033                        268 _LED_Display_table_65536_44:
      000033                        269 	.ds 3
                                    270 ;--------------------------------------------------------
                                    271 ; Stack segment in internal ram 
                                    272 ;--------------------------------------------------------
                                    273 	.area	SSEG
      000036                        274 __start__stack:
      000036                        275 	.ds	1
                                    276 
                                    277 ;--------------------------------------------------------
                                    278 ; indirectly addressable internal ram data
                                    279 ;--------------------------------------------------------
                                    280 	.area ISEG    (DATA)
                                    281 ;--------------------------------------------------------
                                    282 ; absolute internal ram data
                                    283 ;--------------------------------------------------------
                                    284 	.area IABS    (ABS,DATA)
                                    285 	.area IABS    (ABS,DATA)
                                    286 ;--------------------------------------------------------
                                    287 ; bit data
                                    288 ;--------------------------------------------------------
                                    289 	.area BSEG    (BIT)
                                    290 ;--------------------------------------------------------
                                    291 ; paged external ram data
                                    292 ;--------------------------------------------------------
                                    293 	.area PSEG    (PAG,XDATA)
                                    294 ;--------------------------------------------------------
                                    295 ; external ram data
                                    296 ;--------------------------------------------------------
                                    297 	.area XSEG    (XDATA)
                                    298 ;--------------------------------------------------------
                                    299 ; absolute external ram data
                                    300 ;--------------------------------------------------------
                                    301 	.area XABS    (ABS,XDATA)
                                    302 ;--------------------------------------------------------
                                    303 ; external initialized ram data
                                    304 ;--------------------------------------------------------
                                    305 	.area XISEG   (XDATA)
                                    306 	.area HOME    (CODE)
                                    307 	.area GSINIT0 (CODE)
                                    308 	.area GSINIT1 (CODE)
                                    309 	.area GSINIT2 (CODE)
                                    310 	.area GSINIT3 (CODE)
                                    311 	.area GSINIT4 (CODE)
                                    312 	.area GSINIT5 (CODE)
                                    313 	.area GSINIT  (CODE)
                                    314 	.area GSFINAL (CODE)
                                    315 	.area CSEG    (CODE)
                                    316 ;--------------------------------------------------------
                                    317 ; interrupt vector 
                                    318 ;--------------------------------------------------------
                                    319 	.area HOME    (CODE)
      000000                        320 __interrupt_vect:
      000000 02 00 11         [24]  321 	ljmp	__sdcc_gsinit_startup
      000003 32               [24]  322 	reti
      000004                        323 	.ds	7
      00000B 02 00 B0         [24]  324 	ljmp	_timer_isr
                                    325 ;--------------------------------------------------------
                                    326 ; global & static initialisations
                                    327 ;--------------------------------------------------------
                                    328 	.area HOME    (CODE)
                                    329 	.area GSINIT  (CODE)
                                    330 	.area GSFINAL (CODE)
                                    331 	.area GSINIT  (CODE)
                                    332 	.globl __sdcc_gsinit_startup
                                    333 	.globl __sdcc_program_startup
                                    334 	.globl __start__stack
                                    335 	.globl __mcs51_genXINIT
                                    336 	.globl __mcs51_genXRAMCLEAR
                                    337 	.globl __mcs51_genRAMCLEAR
                                    338 ;	main.c:5: int count=50; // 一圈200步
      00006A 75 10 32         [24]  339 	mov	_count,#0x32
      00006D 75 11 00         [24]  340 	mov	(_count + 1),#0x00
                                    341 ;	main.c:6: int max=50;
      000070 75 12 32         [24]  342 	mov	_max,#0x32
      000073 75 13 00         [24]  343 	mov	(_max + 1),#0x00
                                    344 ;	main.c:7: char direct=0; 
      000076 75 14 00         [24]  345 	mov	_direct,#0x00
                                    346 ;	main.c:8: unsigned char step=0x01; 
      000079 75 15 01         [24]  347 	mov	_step,#0x01
                                    348 ;	main.c:9: unsigned int speed=(65536-30000);
      00007C 75 16 D0         [24]  349 	mov	_speed,#0xd0
      00007F 75 17 8A         [24]  350 	mov	(_speed + 1),#0x8a
                                    351 	.area GSFINAL (CODE)
      000082 02 00 0E         [24]  352 	ljmp	__sdcc_program_startup
                                    353 ;--------------------------------------------------------
                                    354 ; Home
                                    355 ;--------------------------------------------------------
                                    356 	.area HOME    (CODE)
                                    357 	.area HOME    (CODE)
      00000E                        358 __sdcc_program_startup:
      00000E 02 01 EA         [24]  359 	ljmp	_main
                                    360 ;	return from main will return to caller
                                    361 ;--------------------------------------------------------
                                    362 ; code
                                    363 ;--------------------------------------------------------
                                    364 	.area CSEG    (CODE)
                                    365 ;------------------------------------------------------------
                                    366 ;Allocation info for local variables in function 'delay'
                                    367 ;------------------------------------------------------------
                                    368 ;time                      Allocated to registers r6 r7 
                                    369 ;i                         Allocated to registers r4 r5 
                                    370 ;j                         Allocated to registers r2 r3 
                                    371 ;------------------------------------------------------------
                                    372 ;	main.c:10: void delay(unsigned int time)
                                    373 ;	-----------------------------------------
                                    374 ;	 function delay
                                    375 ;	-----------------------------------------
      000085                        376 _delay:
                           000007   377 	ar7 = 0x07
                           000006   378 	ar6 = 0x06
                           000005   379 	ar5 = 0x05
                           000004   380 	ar4 = 0x04
                           000003   381 	ar3 = 0x03
                           000002   382 	ar2 = 0x02
                           000001   383 	ar1 = 0x01
                           000000   384 	ar0 = 0x00
      000085 AE 82            [24]  385 	mov	r6,dpl
      000087 AF 83            [24]  386 	mov	r7,dph
                                    387 ;	main.c:13: for(i=0;i<time;i++)    
      000089 7C 00            [12]  388 	mov	r4,#0x00
      00008B 7D 00            [12]  389 	mov	r5,#0x00
      00008D                        390 00107$:
      00008D C3               [12]  391 	clr	c
      00008E EC               [12]  392 	mov	a,r4
      00008F 9E               [12]  393 	subb	a,r6
      000090 ED               [12]  394 	mov	a,r5
      000091 9F               [12]  395 	subb	a,r7
      000092 50 1B            [24]  396 	jnc	00109$
                                    397 ;	main.c:14: for(j=0;j<1275;j++);
      000094 7A FB            [12]  398 	mov	r2,#0xfb
      000096 7B 04            [12]  399 	mov	r3,#0x04
      000098                        400 00105$:
      000098 EA               [12]  401 	mov	a,r2
      000099 24 FF            [12]  402 	add	a,#0xff
      00009B F8               [12]  403 	mov	r0,a
      00009C EB               [12]  404 	mov	a,r3
      00009D 34 FF            [12]  405 	addc	a,#0xff
      00009F F9               [12]  406 	mov	r1,a
      0000A0 88 02            [24]  407 	mov	ar2,r0
      0000A2 89 03            [24]  408 	mov	ar3,r1
      0000A4 E8               [12]  409 	mov	a,r0
      0000A5 49               [12]  410 	orl	a,r1
      0000A6 70 F0            [24]  411 	jnz	00105$
                                    412 ;	main.c:13: for(i=0;i<time;i++)    
      0000A8 0C               [12]  413 	inc	r4
      0000A9 BC 00 E1         [24]  414 	cjne	r4,#0x00,00107$
      0000AC 0D               [12]  415 	inc	r5
      0000AD 80 DE            [24]  416 	sjmp	00107$
      0000AF                        417 00109$:
                                    418 ;	main.c:15: }
      0000AF 22               [24]  419 	ret
                                    420 ;------------------------------------------------------------
                                    421 ;Allocation info for local variables in function 'timer_isr'
                                    422 ;------------------------------------------------------------
                                    423 ;	main.c:16: void timer_isr (void) __interrupt (1) __using (1) {	//timer 0 interrupt 訊號		using register bank 1
                                    424 ;	-----------------------------------------
                                    425 ;	 function timer_isr
                                    426 ;	-----------------------------------------
      0000B0                        427 _timer_isr:
                           00000F   428 	ar7 = 0x0f
                           00000E   429 	ar6 = 0x0e
                           00000D   430 	ar5 = 0x0d
                           00000C   431 	ar4 = 0x0c
                           00000B   432 	ar3 = 0x0b
                           00000A   433 	ar2 = 0x0a
                           000009   434 	ar1 = 0x09
                           000008   435 	ar0 = 0x08
      0000B0 C0 E0            [24]  436 	push	acc
      0000B2 C0 F0            [24]  437 	push	b
      0000B4 C0 D0            [24]  438 	push	psw
      0000B6 75 D0 08         [24]  439 	mov	psw,#0x08
                                    440 ;	main.c:17: TH0=speed/256; 
      0000B9 AE 17            [24]  441 	mov	r6,(_speed + 1)
      0000BB 8E 8C            [24]  442 	mov	_TH0,r6
                                    443 ;	main.c:18: TL0=speed%16; 
      0000BD 74 0F            [12]  444 	mov	a,#0x0f
      0000BF 55 16            [12]  445 	anl	a,_speed
      0000C1 FE               [12]  446 	mov	r6,a
      0000C2 7F 00            [12]  447 	mov	r7,#0x00
      0000C4 8E 8A            [24]  448 	mov	_TL0,r6
                                    449 ;	main.c:20: if(direct==0) { 
      0000C6 E5 14            [12]  450 	mov	a,_direct
      0000C8 70 14            [24]  451 	jnz	00106$
                                    452 ;	main.c:21: step>>=1; 
      0000CA E5 15            [12]  453 	mov	a,_step
      0000CC C3               [12]  454 	clr	c
      0000CD 13               [12]  455 	rrc	a
                                    456 ;	main.c:22: if(step==0x00) step=0x08;
      0000CE F5 15            [12]  457 	mov	_step,a
      0000D0 70 03            [24]  458 	jnz	00102$
      0000D2 75 15 08         [24]  459 	mov	_step,#0x08
      0000D5                        460 00102$:
                                    461 ;	main.c:23: P0&=0xf0; 
      0000D5 53 80 F0         [24]  462 	anl	_P0,#0xf0
                                    463 ;	main.c:24: P0|=step; 
      0000D8 E5 15            [12]  464 	mov	a,_step
      0000DA 42 80            [12]  465 	orl	_P0,a
      0000DC 80 16            [24]  466 	sjmp	00107$
      0000DE                        467 00106$:
                                    468 ;	main.c:27: step<<=1; 
      0000DE E5 15            [12]  469 	mov	a,_step
      0000E0 FF               [12]  470 	mov	r7,a
      0000E1 25 E0            [12]  471 	add	a,acc
      0000E3 F5 15            [12]  472 	mov	_step,a
                                    473 ;	main.c:28: if(step==0x10) 
      0000E5 74 10            [12]  474 	mov	a,#0x10
      0000E7 B5 15 03         [24]  475 	cjne	a,_step,00104$
                                    476 ;	main.c:29: step=0x01;
      0000EA 75 15 01         [24]  477 	mov	_step,#0x01
      0000ED                        478 00104$:
                                    479 ;	main.c:30: P0&=0xf0; 
      0000ED 53 80 F0         [24]  480 	anl	_P0,#0xf0
                                    481 ;	main.c:31: P0|=step; 
      0000F0 E5 15            [12]  482 	mov	a,_step
      0000F2 42 80            [12]  483 	orl	_P0,a
      0000F4                        484 00107$:
                                    485 ;	main.c:33: if(--count<=0){
      0000F4 15 10            [12]  486 	dec	_count
      0000F6 74 FF            [12]  487 	mov	a,#0xff
      0000F8 B5 10 02         [24]  488 	cjne	a,_count,00132$
      0000FB 15 11            [12]  489 	dec	(_count + 1)
      0000FD                        490 00132$:
      0000FD C3               [12]  491 	clr	c
      0000FE E4               [12]  492 	clr	a
      0000FF 95 10            [12]  493 	subb	a,_count
      000101 74 80            [12]  494 	mov	a,#(0x00 ^ 0x80)
      000103 85 11 F0         [24]  495 	mov	b,(_count + 1)
      000106 63 F0 80         [24]  496 	xrl	b,#0x80
      000109 95 F0            [12]  497 	subb	a,b
      00010B 40 02            [24]  498 	jc	00110$
                                    499 ;	main.c:34: TR0=0;
                                    500 ;	assignBit
      00010D C2 8C            [12]  501 	clr	_TR0
      00010F                        502 00110$:
                                    503 ;	main.c:36: }
      00010F D0 D0            [24]  504 	pop	psw
      000111 D0 F0            [24]  505 	pop	b
      000113 D0 E0            [24]  506 	pop	acc
      000115 32               [24]  507 	reti
                                    508 ;	eliminated unneeded push/pop dpl
                                    509 ;	eliminated unneeded push/pop dph
                                    510 ;------------------------------------------------------------
                                    511 ;Allocation info for local variables in function 'keyPressed'
                                    512 ;------------------------------------------------------------
                                    513 ;row                       Allocated with name '_keyPressed_row_65536_38'
                                    514 ;c                         Allocated to registers r4 r5 
                                    515 ;col                       Allocated to registers r2 r3 
                                    516 ;magic                     Allocated to registers r7 r6 
                                    517 ;------------------------------------------------------------
                                    518 ;	main.c:38: short keyPressed(short row) {
                                    519 ;	-----------------------------------------
                                    520 ;	 function keyPressed
                                    521 ;	-----------------------------------------
      000116                        522 _keyPressed:
                           000007   523 	ar7 = 0x07
                           000006   524 	ar6 = 0x06
                           000005   525 	ar5 = 0x05
                           000004   526 	ar4 = 0x04
                           000003   527 	ar3 = 0x03
                           000002   528 	ar2 = 0x02
                           000001   529 	ar1 = 0x01
                           000000   530 	ar0 = 0x00
      000116 85 82 30         [24]  531 	mov	_keyPressed_row_65536_38,dpl
      000119 85 83 31         [24]  532 	mov	(_keyPressed_row_65536_38 + 1),dph
                                    533 ;	main.c:39: if((P2 & 0b11110000) != 0b11110000){	//if 按下按鈕
      00011C AC A0            [24]  534 	mov	r4,_P2
      00011E 53 04 F0         [24]  535 	anl	ar4,#0xf0
      000121 7D 00            [12]  536 	mov	r5,#0x00
      000123 BC F0 05         [24]  537 	cjne	r4,#0xf0,00127$
      000126 BD 00 02         [24]  538 	cjne	r5,#0x00,00127$
      000129 80 55            [24]  539 	sjmp	00105$
      00012B                        540 00127$:
                                    541 ;	main.c:40: for (short c = 1, col = 0; col < 4; c *= 2, col++) {
      00012B 7C 01            [12]  542 	mov	r4,#0x01
      00012D 7D 00            [12]  543 	mov	r5,#0x00
      00012F 7A 00            [12]  544 	mov	r2,#0x00
      000131 7B 00            [12]  545 	mov	r3,#0x00
      000133 78 00            [12]  546 	mov	r0,#0x00
      000135 79 00            [12]  547 	mov	r1,#0x00
      000137                        548 00107$:
      000137 C3               [12]  549 	clr	c
      000138 E8               [12]  550 	mov	a,r0
      000139 94 04            [12]  551 	subb	a,#0x04
      00013B E9               [12]  552 	mov	a,r1
      00013C 64 80            [12]  553 	xrl	a,#0x80
      00013E 94 80            [12]  554 	subb	a,#0x80
      000140 50 3E            [24]  555 	jnc	00105$
                                    556 ;	main.c:42: `			short magic = ((P2 >> 4) ^ 0b11111111) & 0b00001111;
      000142 E5 A0            [12]  557 	mov	a,_P2
      000144 C4               [12]  558 	swap	a
      000145 54 0F            [12]  559 	anl	a,#0x0f
      000147 FF               [12]  560 	mov	r7,a
      000148 63 07 FF         [24]  561 	xrl	ar7,#0xff
      00014B 53 07 0F         [24]  562 	anl	ar7,#0x0f
      00014E 7E 00            [12]  563 	mov	r6,#0x00
                                    564 ;	main.c:43: if (magic == c) {
      000150 EF               [12]  565 	mov	a,r7
      000151 B5 04 1B         [24]  566 	cjne	a,ar4,00108$
      000154 EE               [12]  567 	mov	a,r6
      000155 B5 05 17         [24]  568 	cjne	a,ar5,00108$
                                    569 ;	main.c:44: return col * 4 + row;
      000158 EA               [12]  570 	mov	a,r2
      000159 2A               [12]  571 	add	a,r2
      00015A FE               [12]  572 	mov	r6,a
      00015B EB               [12]  573 	mov	a,r3
      00015C 33               [12]  574 	rlc	a
      00015D FF               [12]  575 	mov	r7,a
      00015E EE               [12]  576 	mov	a,r6
      00015F 2E               [12]  577 	add	a,r6
      000160 FE               [12]  578 	mov	r6,a
      000161 EF               [12]  579 	mov	a,r7
      000162 33               [12]  580 	rlc	a
      000163 FF               [12]  581 	mov	r7,a
      000164 E5 30            [12]  582 	mov	a,_keyPressed_row_65536_38
      000166 2E               [12]  583 	add	a,r6
      000167 F5 82            [12]  584 	mov	dpl,a
      000169 E5 31            [12]  585 	mov	a,(_keyPressed_row_65536_38 + 1)
      00016B 3F               [12]  586 	addc	a,r7
      00016C F5 83            [12]  587 	mov	dph,a
      00016E 22               [24]  588 	ret
      00016F                        589 00108$:
                                    590 ;	main.c:40: for (short c = 1, col = 0; col < 4; c *= 2, col++) {
      00016F EC               [12]  591 	mov	a,r4
      000170 2C               [12]  592 	add	a,r4
      000171 FC               [12]  593 	mov	r4,a
      000172 ED               [12]  594 	mov	a,r5
      000173 33               [12]  595 	rlc	a
      000174 FD               [12]  596 	mov	r5,a
      000175 08               [12]  597 	inc	r0
      000176 B8 00 01         [24]  598 	cjne	r0,#0x00,00131$
      000179 09               [12]  599 	inc	r1
      00017A                        600 00131$:
      00017A 88 02            [24]  601 	mov	ar2,r0
      00017C 89 03            [24]  602 	mov	ar3,r1
      00017E 80 B7            [24]  603 	sjmp	00107$
      000180                        604 00105$:
                                    605 ;	main.c:48: return -1;	//沒按 return -1
      000180 90 FF FF         [24]  606 	mov	dptr,#0xffff
                                    607 ;	main.c:49: }
      000183 22               [24]  608 	ret
                                    609 ;------------------------------------------------------------
                                    610 ;Allocation info for local variables in function 'LED_Display'
                                    611 ;------------------------------------------------------------
                                    612 ;num                       Allocated with name '_LED_Display_PARM_2'
                                    613 ;table                     Allocated with name '_LED_Display_table_65536_44'
                                    614 ;i                         Allocated to registers r3 r4 
                                    615 ;j                         Allocated to registers r6 r7 
                                    616 ;------------------------------------------------------------
                                    617 ;	main.c:50: void LED_Display(short table[], short num[]) {
                                    618 ;	-----------------------------------------
                                    619 ;	 function LED_Display
                                    620 ;	-----------------------------------------
      000184                        621 _LED_Display:
      000184 85 82 33         [24]  622 	mov	_LED_Display_table_65536_44,dpl
      000187 85 83 34         [24]  623 	mov	(_LED_Display_table_65536_44 + 1),dph
      00018A 85 F0 35         [24]  624 	mov	(_LED_Display_table_65536_44 + 2),b
                                    625 ;	main.c:51: for(short i = 0; i < 4; i++) {
      00018D 7B 00            [12]  626 	mov	r3,#0x00
      00018F 7C 00            [12]  627 	mov	r4,#0x00
      000191                        628 00107$:
      000191 C3               [12]  629 	clr	c
      000192 EB               [12]  630 	mov	a,r3
      000193 94 04            [12]  631 	subb	a,#0x04
      000195 EC               [12]  632 	mov	a,r4
      000196 64 80            [12]  633 	xrl	a,#0x80
      000198 94 80            [12]  634 	subb	a,#0x80
      00019A 50 4D            [24]  635 	jnc	00109$
                                    636 ;	main.c:52: P1  = table[i] + num[i];
      00019C EB               [12]  637 	mov	a,r3
      00019D 2B               [12]  638 	add	a,r3
      00019E F9               [12]  639 	mov	r1,a
      00019F EC               [12]  640 	mov	a,r4
      0001A0 33               [12]  641 	rlc	a
      0001A1 FA               [12]  642 	mov	r2,a
      0001A2 E9               [12]  643 	mov	a,r1
      0001A3 25 33            [12]  644 	add	a,_LED_Display_table_65536_44
      0001A5 F8               [12]  645 	mov	r0,a
      0001A6 EA               [12]  646 	mov	a,r2
      0001A7 35 34            [12]  647 	addc	a,(_LED_Display_table_65536_44 + 1)
      0001A9 FE               [12]  648 	mov	r6,a
      0001AA AF 35            [24]  649 	mov	r7,(_LED_Display_table_65536_44 + 2)
      0001AC 88 82            [24]  650 	mov	dpl,r0
      0001AE 8E 83            [24]  651 	mov	dph,r6
      0001B0 8F F0            [24]  652 	mov	b,r7
      0001B2 12 06 35         [24]  653 	lcall	__gptrget
      0001B5 F8               [12]  654 	mov	r0,a
      0001B6 E9               [12]  655 	mov	a,r1
      0001B7 25 30            [12]  656 	add	a,_LED_Display_PARM_2
      0001B9 F9               [12]  657 	mov	r1,a
      0001BA EA               [12]  658 	mov	a,r2
      0001BB 35 31            [12]  659 	addc	a,(_LED_Display_PARM_2 + 1)
      0001BD FA               [12]  660 	mov	r2,a
      0001BE AF 32            [24]  661 	mov	r7,(_LED_Display_PARM_2 + 2)
      0001C0 89 82            [24]  662 	mov	dpl,r1
      0001C2 8A 83            [24]  663 	mov	dph,r2
      0001C4 8F F0            [24]  664 	mov	b,r7
      0001C6 12 06 35         [24]  665 	lcall	__gptrget
      0001C9 28               [12]  666 	add	a,r0
      0001CA F5 90            [12]  667 	mov	_P1,a
                                    668 ;	main.c:53: for(int j = 0; j < 1000; j++){}
      0001CC 7E 00            [12]  669 	mov	r6,#0x00
      0001CE 7F 00            [12]  670 	mov	r7,#0x00
      0001D0                        671 00104$:
      0001D0 C3               [12]  672 	clr	c
      0001D1 EE               [12]  673 	mov	a,r6
      0001D2 94 E8            [12]  674 	subb	a,#0xe8
      0001D4 EF               [12]  675 	mov	a,r7
      0001D5 64 80            [12]  676 	xrl	a,#0x80
      0001D7 94 83            [12]  677 	subb	a,#0x83
      0001D9 50 07            [24]  678 	jnc	00108$
      0001DB 0E               [12]  679 	inc	r6
      0001DC BE 00 F1         [24]  680 	cjne	r6,#0x00,00104$
      0001DF 0F               [12]  681 	inc	r7
      0001E0 80 EE            [24]  682 	sjmp	00104$
      0001E2                        683 00108$:
                                    684 ;	main.c:51: for(short i = 0; i < 4; i++) {
      0001E2 0B               [12]  685 	inc	r3
      0001E3 BB 00 AB         [24]  686 	cjne	r3,#0x00,00107$
      0001E6 0C               [12]  687 	inc	r4
      0001E7 80 A8            [24]  688 	sjmp	00107$
      0001E9                        689 00109$:
                                    690 ;	main.c:55: }
      0001E9 22               [24]  691 	ret
                                    692 ;------------------------------------------------------------
                                    693 ;Allocation info for local variables in function 'main'
                                    694 ;------------------------------------------------------------
                                    695 ;table                     Allocated with name '_main_table_65537_51'
                                    696 ;num                       Allocated with name '_main_num_65537_51'
                                    697 ;row                       Allocated with name '_main_row_65537_51'
                                    698 ;cnt                       Allocated with name '_main_cnt_65538_52'
                                    699 ;previous                  Allocated with name '_main_previous_65538_52'
                                    700 ;previous2                 Allocated with name '_main_previous2_65538_52'
                                    701 ;key                       Allocated to registers r2 r3 
                                    702 ;------------------------------------------------------------
                                    703 ;	main.c:57: int main(){
                                    704 ;	-----------------------------------------
                                    705 ;	 function main
                                    706 ;	-----------------------------------------
      0001EA                        707 _main:
                                    708 ;	main.c:58: IE=0x82;
      0001EA 75 A8 82         [24]  709 	mov	_IE,#0x82
                                    710 ;	main.c:59: TMOD=0x01;
      0001ED 75 89 01         [24]  711 	mov	_TMOD,#0x01
                                    712 ;	main.c:60: TH0=speed/256;
      0001F0 AE 17            [24]  713 	mov	r6,(_speed + 1)
      0001F2 8E 8C            [24]  714 	mov	_TH0,r6
                                    715 ;	main.c:61: TL0=speed%16;
      0001F4 74 0F            [12]  716 	mov	a,#0x0f
      0001F6 55 16            [12]  717 	anl	a,_speed
      0001F8 FE               [12]  718 	mov	r6,a
      0001F9 7F 00            [12]  719 	mov	r7,#0x00
      0001FB 8E 8A            [24]  720 	mov	_TL0,r6
                                    721 ;	main.c:63: short table[4] = {0x70, 0xb0, 0xd0, 0xe0};
      0001FD 75 18 70         [24]  722 	mov	(_main_table_65537_51 + 0),#0x70
                                    723 ;	1-genFromRTrack replaced	mov	(_main_table_65537_51 + 1),#0x00
      000200 8F 19            [24]  724 	mov	(_main_table_65537_51 + 1),r7
      000202 75 1A B0         [24]  725 	mov	((_main_table_65537_51 + 0x0002) + 0),#0xb0
                                    726 ;	1-genFromRTrack replaced	mov	((_main_table_65537_51 + 0x0002) + 1),#0x00
      000205 8F 1B            [24]  727 	mov	((_main_table_65537_51 + 0x0002) + 1),r7
      000207 75 1C D0         [24]  728 	mov	((_main_table_65537_51 + 0x0004) + 0),#0xd0
                                    729 ;	1-genFromRTrack replaced	mov	((_main_table_65537_51 + 0x0004) + 1),#0x00
      00020A 8F 1D            [24]  730 	mov	((_main_table_65537_51 + 0x0004) + 1),r7
      00020C 75 1E E0         [24]  731 	mov	((_main_table_65537_51 + 0x0006) + 0),#0xe0
                                    732 ;	1-genFromRTrack replaced	mov	((_main_table_65537_51 + 0x0006) + 1),#0x00
      00020F 8F 1F            [24]  733 	mov	((_main_table_65537_51 + 0x0006) + 1),r7
                                    734 ;	main.c:64: int num[4] = {0,0,0,0};
      000211 E4               [12]  735 	clr	a
      000212 F5 20            [12]  736 	mov	(_main_num_65537_51 + 0),a
      000214 F5 21            [12]  737 	mov	(_main_num_65537_51 + 1),a
      000216 F5 22            [12]  738 	mov	((_main_num_65537_51 + 0x0002) + 0),a
      000218 F5 23            [12]  739 	mov	((_main_num_65537_51 + 0x0002) + 1),a
      00021A F5 24            [12]  740 	mov	((_main_num_65537_51 + 0x0004) + 0),a
      00021C F5 25            [12]  741 	mov	((_main_num_65537_51 + 0x0004) + 1),a
      00021E F5 26            [12]  742 	mov	((_main_num_65537_51 + 0x0006) + 0),a
      000220 F5 27            [12]  743 	mov	((_main_num_65537_51 + 0x0006) + 1),a
                                    744 ;	main.c:65: short row = 0;
      000222 F5 28            [12]  745 	mov	_main_row_65537_51,a
      000224 F5 29            [12]  746 	mov	(_main_row_65537_51 + 1),a
                                    747 ;	main.c:66: P2=0b11111110;
      000226 75 A0 FE         [24]  748 	mov	_P2,#0xfe
                                    749 ;	main.c:67: short cnt = 1;
      000229 75 2A 01         [24]  750 	mov	_main_cnt_65538_52,#0x01
                                    751 ;	1-genFromRTrack replaced	mov	(_main_cnt_65538_52 + 1),#0x00
      00022C F5 2B            [12]  752 	mov	(_main_cnt_65538_52 + 1),a
                                    753 ;	main.c:69: short previous = -1;
      00022E 75 2C FF         [24]  754 	mov	_main_previous_65538_52,#0xff
      000231 75 2D FF         [24]  755 	mov	(_main_previous_65538_52 + 1),#0xff
                                    756 ;	main.c:70: short previous2=-1;
      000234 75 2E FF         [24]  757 	mov	_main_previous2_65538_52,#0xff
      000237 75 2F FF         [24]  758 	mov	(_main_previous2_65538_52 + 1),#0xff
                                    759 ;	main.c:71: while (1) {
      00023A                        760 00115$:
                                    761 ;	main.c:72: P2    =cnt^0b11111111;
      00023A 74 FF            [12]  762 	mov	a,#0xff
      00023C 65 2A            [12]  763 	xrl	a,_main_cnt_65538_52
      00023E FA               [12]  764 	mov	r2,a
      00023F 8A A0            [24]  765 	mov	_P2,r2
                                    766 ;	main.c:73: cnt *=2; //shift
      000241 E5 2A            [12]  767 	mov	a,_main_cnt_65538_52
      000243 25 2A            [12]  768 	add	a,_main_cnt_65538_52
      000245 F5 2A            [12]  769 	mov	_main_cnt_65538_52,a
      000247 E5 2B            [12]  770 	mov	a,(_main_cnt_65538_52 + 1)
      000249 33               [12]  771 	rlc	a
      00024A F5 2B            [12]  772 	mov	(_main_cnt_65538_52 + 1),a
                                    773 ;	main.c:74: short key = keyPressed(row);
      00024C 85 28 82         [24]  774 	mov	dpl,_main_row_65537_51
      00024F 85 29 83         [24]  775 	mov	dph,(_main_row_65537_51 + 1)
      000252 12 01 16         [24]  776 	lcall	_keyPressed
      000255 AA 82            [24]  777 	mov	r2,dpl
      000257 AB 83            [24]  778 	mov	r3,dph
                                    779 ;	main.c:75: if (key != -1 && key != previous && key!=10 && key!=11) {	//有按且不等於上一按 => 處理debounce
      000259 BA FF 05         [24]  780 	cjne	r2,#0xff,00155$
      00025C BB FF 02         [24]  781 	cjne	r3,#0xff,00155$
      00025F 80 3E            [24]  782 	sjmp	00102$
      000261                        783 00155$:
      000261 EA               [12]  784 	mov	a,r2
      000262 B5 2C 06         [24]  785 	cjne	a,_main_previous_65538_52,00156$
      000265 EB               [12]  786 	mov	a,r3
      000266 B5 2D 02         [24]  787 	cjne	a,(_main_previous_65538_52 + 1),00156$
      000269 80 34            [24]  788 	sjmp	00102$
      00026B                        789 00156$:
      00026B BA 0A 05         [24]  790 	cjne	r2,#0x0a,00157$
      00026E BB 00 02         [24]  791 	cjne	r3,#0x00,00157$
      000271 80 2C            [24]  792 	sjmp	00102$
      000273                        793 00157$:
      000273 BA 0B 05         [24]  794 	cjne	r2,#0x0b,00158$
      000276 BB 00 02         [24]  795 	cjne	r3,#0x00,00158$
      000279 80 24            [24]  796 	sjmp	00102$
      00027B                        797 00158$:
                                    798 ;	main.c:76: previous = key;
      00027B 8A 2C            [24]  799 	mov	_main_previous_65538_52,r2
      00027D 8B 2D            [24]  800 	mov	(_main_previous_65538_52 + 1),r3
                                    801 ;	main.c:77: previous2=key;
      00027F 8A 2E            [24]  802 	mov	_main_previous2_65538_52,r2
      000281 8B 2F            [24]  803 	mov	(_main_previous2_65538_52 + 1),r3
                                    804 ;	main.c:78: num[0] =num[1];
      000283 AE 22            [24]  805 	mov	r6,((_main_num_65537_51 + 0x0002) + 0)
      000285 AF 23            [24]  806 	mov	r7,((_main_num_65537_51 + 0x0002) + 1)
      000287 8E 20            [24]  807 	mov	(_main_num_65537_51 + 0),r6
      000289 8F 21            [24]  808 	mov	(_main_num_65537_51 + 1),r7
                                    809 ;	main.c:79: num[1] =num[2];
      00028B AE 24            [24]  810 	mov	r6,((_main_num_65537_51 + 0x0004) + 0)
      00028D AF 25            [24]  811 	mov	r7,((_main_num_65537_51 + 0x0004) + 1)
      00028F 8E 22            [24]  812 	mov	((_main_num_65537_51 + 0x0002) + 0),r6
      000291 8F 23            [24]  813 	mov	((_main_num_65537_51 + 0x0002) + 1),r7
                                    814 ;	main.c:80: num[2] =num[3];			
      000293 AE 26            [24]  815 	mov	r6,((_main_num_65537_51 + 0x0006) + 0)
      000295 AF 27            [24]  816 	mov	r7,((_main_num_65537_51 + 0x0006) + 1)
      000297 8E 24            [24]  817 	mov	((_main_num_65537_51 + 0x0004) + 0),r6
      000299 8F 25            [24]  818 	mov	((_main_num_65537_51 + 0x0004) + 1),r7
                                    819 ;	main.c:81: num[3] = key;	//往前推
      00029B 8A 26            [24]  820 	mov	((_main_num_65537_51 + 0x0006) + 0),r2
      00029D 8B 27            [24]  821 	mov	((_main_num_65537_51 + 0x0006) + 1),r3
      00029F                        822 00102$:
                                    823 ;	main.c:84: if((key==10 || key==11)&& previous2!=key){	//debounce!
      00029F BA 0A 05         [24]  824 	cjne	r2,#0x0a,00159$
      0002A2 BB 00 02         [24]  825 	cjne	r3,#0x00,00159$
      0002A5 80 0B            [24]  826 	sjmp	00111$
      0002A7                        827 00159$:
      0002A7 BA 0B 05         [24]  828 	cjne	r2,#0x0b,00160$
      0002AA BB 00 02         [24]  829 	cjne	r3,#0x00,00160$
      0002AD 80 03            [24]  830 	sjmp	00161$
      0002AF                        831 00160$:
      0002AF 02 03 8D         [24]  832 	ljmp	00109$
      0002B2                        833 00161$:
      0002B2                        834 00111$:
      0002B2 EA               [12]  835 	mov	a,r2
      0002B3 B5 2E 07         [24]  836 	cjne	a,_main_previous2_65538_52,00162$
      0002B6 EB               [12]  837 	mov	a,r3
      0002B7 B5 2F 03         [24]  838 	cjne	a,(_main_previous2_65538_52 + 1),00162$
      0002BA 02 03 8D         [24]  839 	ljmp	00109$
      0002BD                        840 00162$:
                                    841 ;	main.c:85: previous2= key;
      0002BD 8A 2E            [24]  842 	mov	_main_previous2_65538_52,r2
      0002BF 8B 2F            [24]  843 	mov	(_main_previous2_65538_52 + 1),r3
                                    844 ;	main.c:86: count=(num[1]*100+num[2]*10+num[3])/360.0*200.0;
      0002C1 85 22 30         [24]  845 	mov	__mulint_PARM_2,((_main_num_65537_51 + 0x0002) + 0)
      0002C4 85 23 31         [24]  846 	mov	(__mulint_PARM_2 + 1),((_main_num_65537_51 + 0x0002) + 1)
      0002C7 90 00 64         [24]  847 	mov	dptr,#0x0064
      0002CA C0 03            [24]  848 	push	ar3
      0002CC C0 02            [24]  849 	push	ar2
      0002CE 12 04 C5         [24]  850 	lcall	__mulint
      0002D1 AE 82            [24]  851 	mov	r6,dpl
      0002D3 AF 83            [24]  852 	mov	r7,dph
      0002D5 D0 02            [24]  853 	pop	ar2
      0002D7 D0 03            [24]  854 	pop	ar3
      0002D9 85 24 30         [24]  855 	mov	__mulint_PARM_2,((_main_num_65537_51 + 0x0004) + 0)
      0002DC 85 25 31         [24]  856 	mov	(__mulint_PARM_2 + 1),((_main_num_65537_51 + 0x0004) + 1)
      0002DF 90 00 0A         [24]  857 	mov	dptr,#0x000a
      0002E2 C0 07            [24]  858 	push	ar7
      0002E4 C0 06            [24]  859 	push	ar6
      0002E6 C0 03            [24]  860 	push	ar3
      0002E8 C0 02            [24]  861 	push	ar2
      0002EA 12 04 C5         [24]  862 	lcall	__mulint
      0002ED AC 82            [24]  863 	mov	r4,dpl
      0002EF AD 83            [24]  864 	mov	r5,dph
      0002F1 D0 02            [24]  865 	pop	ar2
      0002F3 D0 03            [24]  866 	pop	ar3
      0002F5 D0 06            [24]  867 	pop	ar6
      0002F7 D0 07            [24]  868 	pop	ar7
      0002F9 EC               [12]  869 	mov	a,r4
      0002FA 2E               [12]  870 	add	a,r6
      0002FB FE               [12]  871 	mov	r6,a
      0002FC ED               [12]  872 	mov	a,r5
      0002FD 3F               [12]  873 	addc	a,r7
      0002FE FF               [12]  874 	mov	r7,a
      0002FF E5 26            [12]  875 	mov	a,(_main_num_65537_51 + 0x0006)
      000301 2E               [12]  876 	add	a,r6
      000302 F5 82            [12]  877 	mov	dpl,a
      000304 E5 27            [12]  878 	mov	a,((_main_num_65537_51 + 0x0006) + 1)
      000306 3F               [12]  879 	addc	a,r7
      000307 F5 83            [12]  880 	mov	dph,a
      000309 C0 03            [24]  881 	push	ar3
      00030B C0 02            [24]  882 	push	ar2
      00030D 12 04 E2         [24]  883 	lcall	___sint2fs
      000310 AC 82            [24]  884 	mov	r4,dpl
      000312 AD 83            [24]  885 	mov	r5,dph
      000314 AE F0            [24]  886 	mov	r6,b
      000316 FF               [12]  887 	mov	r7,a
      000317 E4               [12]  888 	clr	a
      000318 C0 E0            [24]  889 	push	acc
      00031A C0 E0            [24]  890 	push	acc
      00031C 74 B4            [12]  891 	mov	a,#0xb4
      00031E C0 E0            [24]  892 	push	acc
      000320 74 43            [12]  893 	mov	a,#0x43
      000322 C0 E0            [24]  894 	push	acc
      000324 8C 82            [24]  895 	mov	dpl,r4
      000326 8D 83            [24]  896 	mov	dph,r5
      000328 8E F0            [24]  897 	mov	b,r6
      00032A EF               [12]  898 	mov	a,r7
      00032B 12 05 72         [24]  899 	lcall	___fsdiv
      00032E AC 82            [24]  900 	mov	r4,dpl
      000330 AD 83            [24]  901 	mov	r5,dph
      000332 AE F0            [24]  902 	mov	r6,b
      000334 FF               [12]  903 	mov	r7,a
      000335 E5 81            [12]  904 	mov	a,sp
      000337 24 FC            [12]  905 	add	a,#0xfc
      000339 F5 81            [12]  906 	mov	sp,a
      00033B C0 04            [24]  907 	push	ar4
      00033D C0 05            [24]  908 	push	ar5
      00033F C0 06            [24]  909 	push	ar6
      000341 C0 07            [24]  910 	push	ar7
      000343 90 00 00         [24]  911 	mov	dptr,#0x0000
      000346 75 F0 48         [24]  912 	mov	b,#0x48
      000349 74 43            [12]  913 	mov	a,#0x43
      00034B 12 03 C1         [24]  914 	lcall	___fsmul
      00034E AC 82            [24]  915 	mov	r4,dpl
      000350 AD 83            [24]  916 	mov	r5,dph
      000352 AE F0            [24]  917 	mov	r6,b
      000354 FF               [12]  918 	mov	r7,a
      000355 E5 81            [12]  919 	mov	a,sp
      000357 24 FC            [12]  920 	add	a,#0xfc
      000359 F5 81            [12]  921 	mov	sp,a
      00035B 8C 82            [24]  922 	mov	dpl,r4
      00035D 8D 83            [24]  923 	mov	dph,r5
      00035F 8E F0            [24]  924 	mov	b,r6
      000361 EF               [12]  925 	mov	a,r7
      000362 12 04 EF         [24]  926 	lcall	___fs2sint
      000365 85 82 10         [24]  927 	mov	_count,dpl
      000368 85 83 11         [24]  928 	mov	(_count + 1),dph
      00036B D0 02            [24]  929 	pop	ar2
      00036D D0 03            [24]  930 	pop	ar3
                                    931 ;	main.c:87: num[0]=0,num[1]=0,num[2]=0,num[3]=0;
      00036F E4               [12]  932 	clr	a
      000370 F5 20            [12]  933 	mov	(_main_num_65537_51 + 0),a
      000372 F5 21            [12]  934 	mov	(_main_num_65537_51 + 1),a
      000374 F5 22            [12]  935 	mov	((_main_num_65537_51 + 0x0002) + 0),a
      000376 F5 23            [12]  936 	mov	((_main_num_65537_51 + 0x0002) + 1),a
      000378 F5 24            [12]  937 	mov	((_main_num_65537_51 + 0x0004) + 0),a
      00037A F5 25            [12]  938 	mov	((_main_num_65537_51 + 0x0004) + 1),a
      00037C F5 26            [12]  939 	mov	((_main_num_65537_51 + 0x0006) + 0),a
      00037E F5 27            [12]  940 	mov	((_main_num_65537_51 + 0x0006) + 1),a
                                    941 ;	main.c:88: direct=0;
                                    942 ;	1-genFromRTrack replaced	mov	_direct,#0x00
      000380 F5 14            [12]  943 	mov	_direct,a
                                    944 ;	main.c:89: if(key==11)
      000382 BA 0B 06         [24]  945 	cjne	r2,#0x0b,00107$
      000385 BB 00 03         [24]  946 	cjne	r3,#0x00,00107$
                                    947 ;	main.c:90: direct=1;
      000388 75 14 01         [24]  948 	mov	_direct,#0x01
      00038B                        949 00107$:
                                    950 ;	main.c:91: TR0=1;
                                    951 ;	assignBit
      00038B D2 8C            [12]  952 	setb	_TR0
      00038D                        953 00109$:
                                    954 ;	main.c:93: row++;
      00038D 05 28            [12]  955 	inc	_main_row_65537_51
      00038F E4               [12]  956 	clr	a
      000390 B5 28 02         [24]  957 	cjne	a,_main_row_65537_51,00165$
      000393 05 29            [12]  958 	inc	(_main_row_65537_51 + 1)
      000395                        959 00165$:
                                    960 ;	main.c:94: if (cnt == 0x10) {	//用cnt從上往下掃 
      000395 74 10            [12]  961 	mov	a,#0x10
      000397 B5 2A 06         [24]  962 	cjne	a,_main_cnt_65538_52,00166$
      00039A E4               [12]  963 	clr	a
      00039B B5 2B 02         [24]  964 	cjne	a,(_main_cnt_65538_52 + 1),00166$
      00039E 80 02            [24]  965 	sjmp	00167$
      0003A0                        966 00166$:
      0003A0 80 0A            [24]  967 	sjmp	00113$
      0003A2                        968 00167$:
                                    969 ;	main.c:95: cnt = 1;
      0003A2 75 2A 01         [24]  970 	mov	_main_cnt_65538_52,#0x01
                                    971 ;	main.c:96: row = 0;
      0003A5 E4               [12]  972 	clr	a
      0003A6 F5 2B            [12]  973 	mov	(_main_cnt_65538_52 + 1),a
      0003A8 F5 28            [12]  974 	mov	_main_row_65537_51,a
      0003AA F5 29            [12]  975 	mov	(_main_row_65537_51 + 1),a
      0003AC                        976 00113$:
                                    977 ;	main.c:98: LED_Display(table,num);
      0003AC 75 30 20         [24]  978 	mov	_LED_Display_PARM_2,#_main_num_65537_51
      0003AF 75 31 00         [24]  979 	mov	(_LED_Display_PARM_2 + 1),#0x00
      0003B2 75 32 40         [24]  980 	mov	(_LED_Display_PARM_2 + 2),#0x40
      0003B5 90 00 18         [24]  981 	mov	dptr,#_main_table_65537_51
      0003B8 75 F0 40         [24]  982 	mov	b,#0x40
      0003BB 12 01 84         [24]  983 	lcall	_LED_Display
                                    984 ;	main.c:100: }
      0003BE 02 02 3A         [24]  985 	ljmp	00115$
                                    986 	.area CSEG    (CODE)
                                    987 	.area CONST   (CODE)
      000732                        988 _SPIN:
      000732 03 00                  989 	.byte #0x03,#0x00	;  3
      000734 06 00                  990 	.byte #0x06,#0x00	;  6
      000736 0C 00                  991 	.byte #0x0c,#0x00	;  12
      000738 09 00                  992 	.byte #0x09,#0x00	;  9
                                    993 	.area XINIT   (CODE)
                                    994 	.area CABS    (ABS,CODE)
