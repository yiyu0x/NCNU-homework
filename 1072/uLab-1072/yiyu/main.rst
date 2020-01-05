                                      1 ;--------------------------------------------------------
                                      2 ; File Created by SDCC : free open source ANSI-C Compiler
                                      3 ; Version 3.9.0 #11195 (MINGW64)
                                      4 ;--------------------------------------------------------
                                      5 	.module main
                                      6 	.optsdcc -mmcs51 --model-small
                                      7 	
                                      8 ;--------------------------------------------------------
                                      9 ; Public variables in this module
                                     10 ;--------------------------------------------------------
                                     11 	.globl _check_sound_trigger_PARM_2
                                     12 	.globl _display_PARM_4
                                     13 	.globl _display_PARM_3
                                     14 	.globl _display_PARM_2
                                     15 	.globl _music
                                     16 	.globl _table_LED
                                     17 	.globl _main
                                     18 	.globl _init
                                     19 	.globl _check_sound_trigger
                                     20 	.globl _display
                                     21 	.globl _keyPressed
                                     22 	.globl _timer1
                                     23 	.globl _timer_isr
                                     24 	.globl _run_clock
                                     25 	.globl _CY
                                     26 	.globl _AC
                                     27 	.globl _F0
                                     28 	.globl _RS1
                                     29 	.globl _RS0
                                     30 	.globl _OV
                                     31 	.globl _F1
                                     32 	.globl _P
                                     33 	.globl _PS
                                     34 	.globl _PT1
                                     35 	.globl _PX1
                                     36 	.globl _PT0
                                     37 	.globl _PX0
                                     38 	.globl _RD
                                     39 	.globl _WR
                                     40 	.globl _T1
                                     41 	.globl _T0
                                     42 	.globl _INT1
                                     43 	.globl _INT0
                                     44 	.globl _TXD
                                     45 	.globl _RXD
                                     46 	.globl _P3_7
                                     47 	.globl _P3_6
                                     48 	.globl _P3_5
                                     49 	.globl _P3_4
                                     50 	.globl _P3_3
                                     51 	.globl _P3_2
                                     52 	.globl _P3_1
                                     53 	.globl _P3_0
                                     54 	.globl _EA
                                     55 	.globl _ES
                                     56 	.globl _ET1
                                     57 	.globl _EX1
                                     58 	.globl _ET0
                                     59 	.globl _EX0
                                     60 	.globl _P2_7
                                     61 	.globl _P2_6
                                     62 	.globl _P2_5
                                     63 	.globl _P2_4
                                     64 	.globl _P2_3
                                     65 	.globl _P2_2
                                     66 	.globl _P2_1
                                     67 	.globl _P2_0
                                     68 	.globl _SM0
                                     69 	.globl _SM1
                                     70 	.globl _SM2
                                     71 	.globl _REN
                                     72 	.globl _TB8
                                     73 	.globl _RB8
                                     74 	.globl _TI
                                     75 	.globl _RI
                                     76 	.globl _P1_7
                                     77 	.globl _P1_6
                                     78 	.globl _P1_5
                                     79 	.globl _P1_4
                                     80 	.globl _P1_3
                                     81 	.globl _P1_2
                                     82 	.globl _P1_1
                                     83 	.globl _P1_0
                                     84 	.globl _TF1
                                     85 	.globl _TR1
                                     86 	.globl _TF0
                                     87 	.globl _TR0
                                     88 	.globl _IE1
                                     89 	.globl _IT1
                                     90 	.globl _IE0
                                     91 	.globl _IT0
                                     92 	.globl _P0_7
                                     93 	.globl _P0_6
                                     94 	.globl _P0_5
                                     95 	.globl _P0_4
                                     96 	.globl _P0_3
                                     97 	.globl _P0_2
                                     98 	.globl _P0_1
                                     99 	.globl _P0_0
                                    100 	.globl _B
                                    101 	.globl _ACC
                                    102 	.globl _PSW
                                    103 	.globl _IP
                                    104 	.globl _P3
                                    105 	.globl _IE
                                    106 	.globl _P2
                                    107 	.globl _SBUF
                                    108 	.globl _SCON
                                    109 	.globl _P1
                                    110 	.globl _TH1
                                    111 	.globl _TH0
                                    112 	.globl _TL1
                                    113 	.globl _TL0
                                    114 	.globl _TMOD
                                    115 	.globl _TCON
                                    116 	.globl _PCON
                                    117 	.globl _DPH
                                    118 	.globl _DPL
                                    119 	.globl _SP
                                    120 	.globl _P0
                                    121 	.globl _table
                                    122 	.globl _music_counter
                                    123 	.globl _music_index
                                    124 	.globl _counter
                                    125 ;--------------------------------------------------------
                                    126 ; special function registers
                                    127 ;--------------------------------------------------------
                                    128 	.area RSEG    (ABS,DATA)
      000000                        129 	.org 0x0000
                           000080   130 _P0	=	0x0080
                           000081   131 _SP	=	0x0081
                           000082   132 _DPL	=	0x0082
                           000083   133 _DPH	=	0x0083
                           000087   134 _PCON	=	0x0087
                           000088   135 _TCON	=	0x0088
                           000089   136 _TMOD	=	0x0089
                           00008A   137 _TL0	=	0x008a
                           00008B   138 _TL1	=	0x008b
                           00008C   139 _TH0	=	0x008c
                           00008D   140 _TH1	=	0x008d
                           000090   141 _P1	=	0x0090
                           000098   142 _SCON	=	0x0098
                           000099   143 _SBUF	=	0x0099
                           0000A0   144 _P2	=	0x00a0
                           0000A8   145 _IE	=	0x00a8
                           0000B0   146 _P3	=	0x00b0
                           0000B8   147 _IP	=	0x00b8
                           0000D0   148 _PSW	=	0x00d0
                           0000E0   149 _ACC	=	0x00e0
                           0000F0   150 _B	=	0x00f0
                                    151 ;--------------------------------------------------------
                                    152 ; special function bits
                                    153 ;--------------------------------------------------------
                                    154 	.area RSEG    (ABS,DATA)
      000000                        155 	.org 0x0000
                           000080   156 _P0_0	=	0x0080
                           000081   157 _P0_1	=	0x0081
                           000082   158 _P0_2	=	0x0082
                           000083   159 _P0_3	=	0x0083
                           000084   160 _P0_4	=	0x0084
                           000085   161 _P0_5	=	0x0085
                           000086   162 _P0_6	=	0x0086
                           000087   163 _P0_7	=	0x0087
                           000088   164 _IT0	=	0x0088
                           000089   165 _IE0	=	0x0089
                           00008A   166 _IT1	=	0x008a
                           00008B   167 _IE1	=	0x008b
                           00008C   168 _TR0	=	0x008c
                           00008D   169 _TF0	=	0x008d
                           00008E   170 _TR1	=	0x008e
                           00008F   171 _TF1	=	0x008f
                           000090   172 _P1_0	=	0x0090
                           000091   173 _P1_1	=	0x0091
                           000092   174 _P1_2	=	0x0092
                           000093   175 _P1_3	=	0x0093
                           000094   176 _P1_4	=	0x0094
                           000095   177 _P1_5	=	0x0095
                           000096   178 _P1_6	=	0x0096
                           000097   179 _P1_7	=	0x0097
                           000098   180 _RI	=	0x0098
                           000099   181 _TI	=	0x0099
                           00009A   182 _RB8	=	0x009a
                           00009B   183 _TB8	=	0x009b
                           00009C   184 _REN	=	0x009c
                           00009D   185 _SM2	=	0x009d
                           00009E   186 _SM1	=	0x009e
                           00009F   187 _SM0	=	0x009f
                           0000A0   188 _P2_0	=	0x00a0
                           0000A1   189 _P2_1	=	0x00a1
                           0000A2   190 _P2_2	=	0x00a2
                           0000A3   191 _P2_3	=	0x00a3
                           0000A4   192 _P2_4	=	0x00a4
                           0000A5   193 _P2_5	=	0x00a5
                           0000A6   194 _P2_6	=	0x00a6
                           0000A7   195 _P2_7	=	0x00a7
                           0000A8   196 _EX0	=	0x00a8
                           0000A9   197 _ET0	=	0x00a9
                           0000AA   198 _EX1	=	0x00aa
                           0000AB   199 _ET1	=	0x00ab
                           0000AC   200 _ES	=	0x00ac
                           0000AF   201 _EA	=	0x00af
                           0000B0   202 _P3_0	=	0x00b0
                           0000B1   203 _P3_1	=	0x00b1
                           0000B2   204 _P3_2	=	0x00b2
                           0000B3   205 _P3_3	=	0x00b3
                           0000B4   206 _P3_4	=	0x00b4
                           0000B5   207 _P3_5	=	0x00b5
                           0000B6   208 _P3_6	=	0x00b6
                           0000B7   209 _P3_7	=	0x00b7
                           0000B0   210 _RXD	=	0x00b0
                           0000B1   211 _TXD	=	0x00b1
                           0000B2   212 _INT0	=	0x00b2
                           0000B3   213 _INT1	=	0x00b3
                           0000B4   214 _T0	=	0x00b4
                           0000B5   215 _T1	=	0x00b5
                           0000B6   216 _WR	=	0x00b6
                           0000B7   217 _RD	=	0x00b7
                           0000B8   218 _PX0	=	0x00b8
                           0000B9   219 _PT0	=	0x00b9
                           0000BA   220 _PX1	=	0x00ba
                           0000BB   221 _PT1	=	0x00bb
                           0000BC   222 _PS	=	0x00bc
                           0000D0   223 _P	=	0x00d0
                           0000D1   224 _F1	=	0x00d1
                           0000D2   225 _OV	=	0x00d2
                           0000D3   226 _RS0	=	0x00d3
                           0000D4   227 _RS1	=	0x00d4
                           0000D5   228 _F0	=	0x00d5
                           0000D6   229 _AC	=	0x00d6
                           0000D7   230 _CY	=	0x00d7
                                    231 ;--------------------------------------------------------
                                    232 ; overlayable register banks
                                    233 ;--------------------------------------------------------
                                    234 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                        235 	.ds 8
                                    236 	.area REG_BANK_1	(REL,OVR,DATA)
      000008                        237 	.ds 8
                                    238 	.area REG_BANK_2	(REL,OVR,DATA)
      000010                        239 	.ds 8
                                    240 ;--------------------------------------------------------
                                    241 ; internal ram data
                                    242 ;--------------------------------------------------------
                                    243 	.area DSEG    (DATA)
      000018                        244 _counter::
      000018                        245 	.ds 2
      00001A                        246 _music_index::
      00001A                        247 	.ds 2
      00001C                        248 _music_counter::
      00001C                        249 	.ds 2
      00001E                        250 _table::
      00001E                        251 	.ds 14
      00002C                        252 _main_previous_65537_42:
      00002C                        253 	.ds 2
      00002E                        254 _main_row_65537_42:
      00002E                        255 	.ds 2
      000030                        256 _main_count_65537_42:
      000030                        257 	.ds 2
      000032                        258 _main_num_65537_42:
      000032                        259 	.ds 8
      00003A                        260 _main_num_bi_65537_42:
      00003A                        261 	.ds 8
      000042                        262 _main_alpha_65537_42:
      000042                        263 	.ds 22
      000058                        264 _main_index_65538_43:
      000058                        265 	.ds 2
      00005A                        266 _main_flash_flag_65538_43:
      00005A                        267 	.ds 4
                                    268 ;--------------------------------------------------------
                                    269 ; overlayable items in internal ram 
                                    270 ;--------------------------------------------------------
                                    271 	.area	OSEG    (OVR,DATA)
      00005E                        272 _run_clock_sloc0_1_0:
      00005E                        273 	.ds 3
                                    274 	.area	OSEG    (OVR,DATA)
      00005E                        275 _keyPressed_row_65536_12:
      00005E                        276 	.ds 2
                                    277 	.area	OSEG    (OVR,DATA)
      00005E                        278 _display_PARM_2:
      00005E                        279 	.ds 3
      000061                        280 _display_PARM_3:
      000061                        281 	.ds 1
      000062                        282 _display_PARM_4:
      000062                        283 	.ds 4
      000066                        284 _display_t_262144_22:
      000066                        285 	.ds 2
      000068                        286 _display_t_196608_27:
      000068                        287 	.ds 2
                                    288 	.area	OSEG    (OVR,DATA)
      00005E                        289 _check_sound_trigger_PARM_2:
      00005E                        290 	.ds 3
      000061                        291 _check_sound_trigger_num_65536_31:
      000061                        292 	.ds 3
                                    293 ;--------------------------------------------------------
                                    294 ; Stack segment in internal ram 
                                    295 ;--------------------------------------------------------
                                    296 	.area	SSEG
      00006A                        297 __start__stack:
      00006A                        298 	.ds	1
                                    299 
                                    300 ;--------------------------------------------------------
                                    301 ; indirectly addressable internal ram data
                                    302 ;--------------------------------------------------------
                                    303 	.area ISEG    (DATA)
                                    304 ;--------------------------------------------------------
                                    305 ; absolute internal ram data
                                    306 ;--------------------------------------------------------
                                    307 	.area IABS    (ABS,DATA)
                                    308 	.area IABS    (ABS,DATA)
                                    309 ;--------------------------------------------------------
                                    310 ; bit data
                                    311 ;--------------------------------------------------------
                                    312 	.area BSEG    (BIT)
                                    313 ;--------------------------------------------------------
                                    314 ; paged external ram data
                                    315 ;--------------------------------------------------------
                                    316 	.area PSEG    (PAG,XDATA)
                                    317 ;--------------------------------------------------------
                                    318 ; external ram data
                                    319 ;--------------------------------------------------------
                                    320 	.area XSEG    (XDATA)
                                    321 ;--------------------------------------------------------
                                    322 ; absolute external ram data
                                    323 ;--------------------------------------------------------
                                    324 	.area XABS    (ABS,XDATA)
                                    325 ;--------------------------------------------------------
                                    326 ; external initialized ram data
                                    327 ;--------------------------------------------------------
                                    328 	.area XISEG   (XDATA)
                                    329 	.area HOME    (CODE)
                                    330 	.area GSINIT0 (CODE)
                                    331 	.area GSINIT1 (CODE)
                                    332 	.area GSINIT2 (CODE)
                                    333 	.area GSINIT3 (CODE)
                                    334 	.area GSINIT4 (CODE)
                                    335 	.area GSINIT5 (CODE)
                                    336 	.area GSINIT  (CODE)
                                    337 	.area GSFINAL (CODE)
                                    338 	.area CSEG    (CODE)
                                    339 ;--------------------------------------------------------
                                    340 ; interrupt vector 
                                    341 ;--------------------------------------------------------
                                    342 	.area HOME    (CODE)
      000000                        343 __interrupt_vect:
      000000 02 00 21         [24]  344 	ljmp	__sdcc_gsinit_startup
      000003 32               [24]  345 	reti
      000004                        346 	.ds	7
      00000B 02 01 D1         [24]  347 	ljmp	_timer_isr
      00000E                        348 	.ds	5
      000013 32               [24]  349 	reti
      000014                        350 	.ds	7
      00001B 02 02 21         [24]  351 	ljmp	_timer1
                                    352 ;--------------------------------------------------------
                                    353 ; global & static initialisations
                                    354 ;--------------------------------------------------------
                                    355 	.area HOME    (CODE)
                                    356 	.area GSINIT  (CODE)
                                    357 	.area GSFINAL (CODE)
                                    358 	.area GSINIT  (CODE)
                                    359 	.globl __sdcc_gsinit_startup
                                    360 	.globl __sdcc_program_startup
                                    361 	.globl __start__stack
                                    362 	.globl __mcs51_genXINIT
                                    363 	.globl __mcs51_genXRAMCLEAR
                                    364 	.globl __mcs51_genRAMCLEAR
                                    365 ;	main.c:12: short counter = 0;
      00007A E4               [12]  366 	clr	a
      00007B F5 18            [12]  367 	mov	_counter,a
      00007D F5 19            [12]  368 	mov	(_counter + 1),a
                                    369 ;	main.c:13: short music_index = 0;
      00007F F5 1A            [12]  370 	mov	_music_index,a
      000081 F5 1B            [12]  371 	mov	(_music_index + 1),a
                                    372 ;	main.c:14: short music_counter = 0;
      000083 F5 1C            [12]  373 	mov	_music_counter,a
      000085 F5 1D            [12]  374 	mov	(_music_counter + 1),a
                                    375 ;	main.c:19: int table[] = {262, 294, 330, 349, 392, 440, 494};
      000087 75 1E 06         [24]  376 	mov	(_table + 0),#0x06
      00008A 75 1F 01         [24]  377 	mov	(_table + 1),#0x01
      00008D 75 20 26         [24]  378 	mov	((_table + 0x0002) + 0),#0x26
      000090 75 21 01         [24]  379 	mov	((_table + 0x0002) + 1),#0x01
      000093 75 22 4A         [24]  380 	mov	((_table + 0x0004) + 0),#0x4a
      000096 75 23 01         [24]  381 	mov	((_table + 0x0004) + 1),#0x01
      000099 75 24 5D         [24]  382 	mov	((_table + 0x0006) + 0),#0x5d
      00009C 75 25 01         [24]  383 	mov	((_table + 0x0006) + 1),#0x01
      00009F 75 26 88         [24]  384 	mov	((_table + 0x0008) + 0),#0x88
      0000A2 75 27 01         [24]  385 	mov	((_table + 0x0008) + 1),#0x01
      0000A5 75 28 B8         [24]  386 	mov	((_table + 0x000a) + 0),#0xb8
      0000A8 75 29 01         [24]  387 	mov	((_table + 0x000a) + 1),#0x01
      0000AB 75 2A EE         [24]  388 	mov	((_table + 0x000c) + 0),#0xee
      0000AE 75 2B 01         [24]  389 	mov	((_table + 0x000c) + 1),#0x01
                                    390 	.area GSFINAL (CODE)
      0000B1 02 00 1E         [24]  391 	ljmp	__sdcc_program_startup
                                    392 ;--------------------------------------------------------
                                    393 ; Home
                                    394 ;--------------------------------------------------------
                                    395 	.area HOME    (CODE)
                                    396 	.area HOME    (CODE)
      00001E                        397 __sdcc_program_startup:
      00001E 02 05 C4         [24]  398 	ljmp	_main
                                    399 ;	return from main will return to caller
                                    400 ;--------------------------------------------------------
                                    401 ; code
                                    402 ;--------------------------------------------------------
                                    403 	.area CSEG    (CODE)
                                    404 ;------------------------------------------------------------
                                    405 ;Allocation info for local variables in function 'run_clock'
                                    406 ;------------------------------------------------------------
                                    407 ;num                       Allocated to registers r5 r6 r7 
                                    408 ;sloc0                     Allocated with name '_run_clock_sloc0_1_0'
                                    409 ;------------------------------------------------------------
                                    410 ;	main.c:20: void run_clock(short num[]) {
                                    411 ;	-----------------------------------------
                                    412 ;	 function run_clock
                                    413 ;	-----------------------------------------
      0000B4                        414 _run_clock:
                           000007   415 	ar7 = 0x07
                           000006   416 	ar6 = 0x06
                           000005   417 	ar5 = 0x05
                           000004   418 	ar4 = 0x04
                           000003   419 	ar3 = 0x03
                           000002   420 	ar2 = 0x02
                           000001   421 	ar1 = 0x01
                           000000   422 	ar0 = 0x00
      0000B4 AD 82            [24]  423 	mov	r5,dpl
      0000B6 AE 83            [24]  424 	mov	r6,dph
      0000B8 AF F0            [24]  425 	mov	r7,b
                                    426 ;	main.c:21: if (counter >= 20) {
      0000BA C3               [12]  427 	clr	c
      0000BB E5 18            [12]  428 	mov	a,_counter
      0000BD 94 14            [12]  429 	subb	a,#0x14
      0000BF E5 19            [12]  430 	mov	a,(_counter + 1)
      0000C1 64 80            [12]  431 	xrl	a,#0x80
      0000C3 94 80            [12]  432 	subb	a,#0x80
      0000C5 50 01            [24]  433 	jnc	00127$
      0000C7 22               [24]  434 	ret
      0000C8                        435 00127$:
                                    436 ;	main.c:22: num[3]++;
      0000C8 74 06            [12]  437 	mov	a,#0x06
      0000CA 2D               [12]  438 	add	a,r5
      0000CB FA               [12]  439 	mov	r2,a
      0000CC E4               [12]  440 	clr	a
      0000CD 3E               [12]  441 	addc	a,r6
      0000CE FB               [12]  442 	mov	r3,a
      0000CF 8F 04            [24]  443 	mov	ar4,r7
      0000D1 8A 82            [24]  444 	mov	dpl,r2
      0000D3 8B 83            [24]  445 	mov	dph,r3
      0000D5 8C F0            [24]  446 	mov	b,r4
      0000D7 12 0A D5         [24]  447 	lcall	__gptrget
      0000DA F8               [12]  448 	mov	r0,a
      0000DB A3               [24]  449 	inc	dptr
      0000DC 12 0A D5         [24]  450 	lcall	__gptrget
      0000DF F9               [12]  451 	mov	r1,a
      0000E0 08               [12]  452 	inc	r0
      0000E1 B8 00 01         [24]  453 	cjne	r0,#0x00,00128$
      0000E4 09               [12]  454 	inc	r1
      0000E5                        455 00128$:
      0000E5 8A 82            [24]  456 	mov	dpl,r2
      0000E7 8B 83            [24]  457 	mov	dph,r3
      0000E9 8C F0            [24]  458 	mov	b,r4
      0000EB E8               [12]  459 	mov	a,r0
      0000EC 12 09 67         [24]  460 	lcall	__gptrput
      0000EF A3               [24]  461 	inc	dptr
      0000F0 E9               [12]  462 	mov	a,r1
      0000F1 12 09 67         [24]  463 	lcall	__gptrput
                                    464 ;	main.c:23: counter = 0;
      0000F4 E4               [12]  465 	clr	a
      0000F5 F5 18            [12]  466 	mov	_counter,a
      0000F7 F5 19            [12]  467 	mov	(_counter + 1),a
                                    468 ;	main.c:24: if (num[3] == 10) {
      0000F9 8A 82            [24]  469 	mov	dpl,r2
      0000FB 8B 83            [24]  470 	mov	dph,r3
      0000FD 8C F0            [24]  471 	mov	b,r4
      0000FF 12 0A D5         [24]  472 	lcall	__gptrget
      000102 F8               [12]  473 	mov	r0,a
      000103 A3               [24]  474 	inc	dptr
      000104 12 0A D5         [24]  475 	lcall	__gptrget
      000107 F9               [12]  476 	mov	r1,a
      000108 B8 0A 05         [24]  477 	cjne	r0,#0x0a,00129$
      00010B B9 00 02         [24]  478 	cjne	r1,#0x00,00129$
      00010E 80 01            [24]  479 	sjmp	00130$
      000110                        480 00129$:
      000110 22               [24]  481 	ret
      000111                        482 00130$:
                                    483 ;	main.c:25: num[3] = 0;
      000111 8A 82            [24]  484 	mov	dpl,r2
      000113 8B 83            [24]  485 	mov	dph,r3
      000115 8C F0            [24]  486 	mov	b,r4
      000117 E4               [12]  487 	clr	a
      000118 12 09 67         [24]  488 	lcall	__gptrput
      00011B A3               [24]  489 	inc	dptr
      00011C 12 09 67         [24]  490 	lcall	__gptrput
                                    491 ;	main.c:26: num[2]++;
      00011F 74 04            [12]  492 	mov	a,#0x04
      000121 2D               [12]  493 	add	a,r5
      000122 FA               [12]  494 	mov	r2,a
      000123 E4               [12]  495 	clr	a
      000124 3E               [12]  496 	addc	a,r6
      000125 FB               [12]  497 	mov	r3,a
      000126 8F 04            [24]  498 	mov	ar4,r7
      000128 8A 82            [24]  499 	mov	dpl,r2
      00012A 8B 83            [24]  500 	mov	dph,r3
      00012C 8C F0            [24]  501 	mov	b,r4
      00012E 12 0A D5         [24]  502 	lcall	__gptrget
      000131 F8               [12]  503 	mov	r0,a
      000132 A3               [24]  504 	inc	dptr
      000133 12 0A D5         [24]  505 	lcall	__gptrget
      000136 F9               [12]  506 	mov	r1,a
      000137 08               [12]  507 	inc	r0
      000138 B8 00 01         [24]  508 	cjne	r0,#0x00,00131$
      00013B 09               [12]  509 	inc	r1
      00013C                        510 00131$:
      00013C 8A 82            [24]  511 	mov	dpl,r2
      00013E 8B 83            [24]  512 	mov	dph,r3
      000140 8C F0            [24]  513 	mov	b,r4
      000142 E8               [12]  514 	mov	a,r0
      000143 12 09 67         [24]  515 	lcall	__gptrput
      000146 A3               [24]  516 	inc	dptr
      000147 E9               [12]  517 	mov	a,r1
      000148 12 09 67         [24]  518 	lcall	__gptrput
                                    519 ;	main.c:27: if (num[2] == 6) {
      00014B B8 06 05         [24]  520 	cjne	r0,#0x06,00132$
      00014E B9 00 02         [24]  521 	cjne	r1,#0x00,00132$
      000151 80 01            [24]  522 	sjmp	00133$
      000153                        523 00132$:
      000153 22               [24]  524 	ret
      000154                        525 00133$:
                                    526 ;	main.c:28: num[1]++;
      000154 74 02            [12]  527 	mov	a,#0x02
      000156 2D               [12]  528 	add	a,r5
      000157 F5 5E            [12]  529 	mov	_run_clock_sloc0_1_0,a
      000159 E4               [12]  530 	clr	a
      00015A 3E               [12]  531 	addc	a,r6
      00015B F5 5F            [12]  532 	mov	(_run_clock_sloc0_1_0 + 1),a
      00015D 8F 60            [24]  533 	mov	(_run_clock_sloc0_1_0 + 2),r7
      00015F 85 5E 82         [24]  534 	mov	dpl,_run_clock_sloc0_1_0
      000162 85 5F 83         [24]  535 	mov	dph,(_run_clock_sloc0_1_0 + 1)
      000165 85 60 F0         [24]  536 	mov	b,(_run_clock_sloc0_1_0 + 2)
      000168 12 0A D5         [24]  537 	lcall	__gptrget
      00016B F8               [12]  538 	mov	r0,a
      00016C A3               [24]  539 	inc	dptr
      00016D 12 0A D5         [24]  540 	lcall	__gptrget
      000170 F9               [12]  541 	mov	r1,a
      000171 08               [12]  542 	inc	r0
      000172 B8 00 01         [24]  543 	cjne	r0,#0x00,00134$
      000175 09               [12]  544 	inc	r1
      000176                        545 00134$:
      000176 85 5E 82         [24]  546 	mov	dpl,_run_clock_sloc0_1_0
      000179 85 5F 83         [24]  547 	mov	dph,(_run_clock_sloc0_1_0 + 1)
      00017C 85 60 F0         [24]  548 	mov	b,(_run_clock_sloc0_1_0 + 2)
      00017F E8               [12]  549 	mov	a,r0
      000180 12 09 67         [24]  550 	lcall	__gptrput
      000183 A3               [24]  551 	inc	dptr
      000184 E9               [12]  552 	mov	a,r1
      000185 12 09 67         [24]  553 	lcall	__gptrput
                                    554 ;	main.c:29: num[2] = 0;
      000188 8A 82            [24]  555 	mov	dpl,r2
      00018A 8B 83            [24]  556 	mov	dph,r3
      00018C 8C F0            [24]  557 	mov	b,r4
      00018E E4               [12]  558 	clr	a
      00018F 12 09 67         [24]  559 	lcall	__gptrput
      000192 A3               [24]  560 	inc	dptr
      000193 12 09 67         [24]  561 	lcall	__gptrput
                                    562 ;	main.c:30: if (num[1] == 10) {
      000196 B8 0A 37         [24]  563 	cjne	r0,#0x0a,00109$
      000199 B9 00 34         [24]  564 	cjne	r1,#0x00,00109$
                                    565 ;	main.c:31: num[1] = 0;
      00019C 85 5E 82         [24]  566 	mov	dpl,_run_clock_sloc0_1_0
      00019F 85 5F 83         [24]  567 	mov	dph,(_run_clock_sloc0_1_0 + 1)
      0001A2 85 60 F0         [24]  568 	mov	b,(_run_clock_sloc0_1_0 + 2)
      0001A5 E4               [12]  569 	clr	a
      0001A6 12 09 67         [24]  570 	lcall	__gptrput
      0001A9 A3               [24]  571 	inc	dptr
      0001AA 12 09 67         [24]  572 	lcall	__gptrput
                                    573 ;	main.c:32: num[0]++;
      0001AD 8D 82            [24]  574 	mov	dpl,r5
      0001AF 8E 83            [24]  575 	mov	dph,r6
      0001B1 8F F0            [24]  576 	mov	b,r7
      0001B3 12 0A D5         [24]  577 	lcall	__gptrget
      0001B6 FB               [12]  578 	mov	r3,a
      0001B7 A3               [24]  579 	inc	dptr
      0001B8 12 0A D5         [24]  580 	lcall	__gptrget
      0001BB FC               [12]  581 	mov	r4,a
      0001BC 0B               [12]  582 	inc	r3
      0001BD BB 00 01         [24]  583 	cjne	r3,#0x00,00137$
      0001C0 0C               [12]  584 	inc	r4
      0001C1                        585 00137$:
      0001C1 8D 82            [24]  586 	mov	dpl,r5
      0001C3 8E 83            [24]  587 	mov	dph,r6
      0001C5 8F F0            [24]  588 	mov	b,r7
      0001C7 EB               [12]  589 	mov	a,r3
      0001C8 12 09 67         [24]  590 	lcall	__gptrput
      0001CB A3               [24]  591 	inc	dptr
      0001CC EC               [12]  592 	mov	a,r4
                                    593 ;	main.c:37: }
      0001CD 02 09 67         [24]  594 	ljmp	__gptrput
      0001D0                        595 00109$:
      0001D0 22               [24]  596 	ret
                                    597 ;------------------------------------------------------------
                                    598 ;Allocation info for local variables in function 'timer_isr'
                                    599 ;------------------------------------------------------------
                                    600 ;	main.c:39: void timer_isr (void) __interrupt (1) __using (1) {	//控制聲音頻率
                                    601 ;	-----------------------------------------
                                    602 ;	 function timer_isr
                                    603 ;	-----------------------------------------
      0001D1                        604 _timer_isr:
                           00000F   605 	ar7 = 0x0f
                           00000E   606 	ar6 = 0x0e
                           00000D   607 	ar5 = 0x0d
                           00000C   608 	ar4 = 0x0c
                           00000B   609 	ar3 = 0x0b
                           00000A   610 	ar2 = 0x0a
                           000009   611 	ar1 = 0x09
                           000008   612 	ar0 = 0x08
      0001D1 C0 E0            [24]  613 	push	acc
      0001D3 C0 D0            [24]  614 	push	psw
      0001D5 75 D0 08         [24]  615 	mov	psw,#0x08
                                    616 ;	main.c:40: TH0  = 15536 >> 8;
      0001D8 75 8C 3C         [24]  617 	mov	_TH0,#0x3c
                                    618 ;	main.c:41: TL0  = 15536 & 0xff;
      0001DB 75 8A B0         [24]  619 	mov	_TL0,#0xb0
                                    620 ;	main.c:44: counter++;
      0001DE 05 18            [12]  621 	inc	_counter
      0001E0 E4               [12]  622 	clr	a
      0001E1 B5 18 02         [24]  623 	cjne	a,_counter,00115$
      0001E4 05 19            [12]  624 	inc	(_counter + 1)
      0001E6                        625 00115$:
                                    626 ;	main.c:45: if (music_counter++ >= 20) {
      0001E6 AE 1C            [24]  627 	mov	r6,_music_counter
      0001E8 AF 1D            [24]  628 	mov	r7,(_music_counter + 1)
      0001EA 05 1C            [12]  629 	inc	_music_counter
      0001EC E4               [12]  630 	clr	a
      0001ED B5 1C 02         [24]  631 	cjne	a,_music_counter,00116$
      0001F0 05 1D            [12]  632 	inc	(_music_counter + 1)
      0001F2                        633 00116$:
      0001F2 C3               [12]  634 	clr	c
      0001F3 EE               [12]  635 	mov	a,r6
      0001F4 94 14            [12]  636 	subb	a,#0x14
      0001F6 EF               [12]  637 	mov	a,r7
      0001F7 64 80            [12]  638 	xrl	a,#0x80
      0001F9 94 80            [12]  639 	subb	a,#0x80
      0001FB 40 1F            [24]  640 	jc	00105$
                                    641 ;	main.c:46: music_index++;
      0001FD 05 1A            [12]  642 	inc	_music_index
      0001FF E4               [12]  643 	clr	a
      000200 B5 1A 02         [24]  644 	cjne	a,_music_index,00118$
      000203 05 1B            [12]  645 	inc	(_music_index + 1)
      000205                        646 00118$:
                                    647 ;	main.c:47: if (music_index >= 42)
      000205 C3               [12]  648 	clr	c
      000206 E5 1A            [12]  649 	mov	a,_music_index
      000208 94 2A            [12]  650 	subb	a,#0x2a
      00020A E5 1B            [12]  651 	mov	a,(_music_index + 1)
      00020C 64 80            [12]  652 	xrl	a,#0x80
      00020E 94 80            [12]  653 	subb	a,#0x80
      000210 40 05            [24]  654 	jc	00102$
                                    655 ;	main.c:48: music_index = 0;
      000212 E4               [12]  656 	clr	a
      000213 F5 1A            [12]  657 	mov	_music_index,a
      000215 F5 1B            [12]  658 	mov	(_music_index + 1),a
      000217                        659 00102$:
                                    660 ;	main.c:49: music_counter = 0;
      000217 E4               [12]  661 	clr	a
      000218 F5 1C            [12]  662 	mov	_music_counter,a
      00021A F5 1D            [12]  663 	mov	(_music_counter + 1),a
      00021C                        664 00105$:
                                    665 ;	main.c:51: }
      00021C D0 D0            [24]  666 	pop	psw
      00021E D0 E0            [24]  667 	pop	acc
      000220 32               [24]  668 	reti
                                    669 ;	eliminated unneeded push/pop dpl
                                    670 ;	eliminated unneeded push/pop dph
                                    671 ;	eliminated unneeded push/pop b
                                    672 ;------------------------------------------------------------
                                    673 ;Allocation info for local variables in function 'timer1'
                                    674 ;------------------------------------------------------------
                                    675 ;	main.c:53: void timer1 (void) __interrupt (3) __using (2) {	//頻率
                                    676 ;	-----------------------------------------
                                    677 ;	 function timer1
                                    678 ;	-----------------------------------------
      000221                        679 _timer1:
                           000017   680 	ar7 = 0x17
                           000016   681 	ar6 = 0x16
                           000015   682 	ar5 = 0x15
                           000014   683 	ar4 = 0x14
                           000013   684 	ar3 = 0x13
                           000012   685 	ar2 = 0x12
                           000011   686 	ar1 = 0x11
                           000010   687 	ar0 = 0x10
      000221 C0 E0            [24]  688 	push	acc
      000223 C0 82            [24]  689 	push	dpl
      000225 C0 83            [24]  690 	push	dph
      000227 C0 D0            [24]  691 	push	psw
      000229 75 D0 10         [24]  692 	mov	psw,#0x10
                                    693 ;	main.c:54: TH1  = (PERIOD-table[music[music_index]-1]) >> 8;
      00022C E5 1A            [12]  694 	mov	a,_music_index
      00022E 25 1A            [12]  695 	add	a,_music_index
      000230 FE               [12]  696 	mov	r6,a
      000231 E5 1B            [12]  697 	mov	a,(_music_index + 1)
      000233 33               [12]  698 	rlc	a
      000234 FF               [12]  699 	mov	r7,a
      000235 EE               [12]  700 	mov	a,r6
      000236 24 F2            [12]  701 	add	a,#_music
      000238 F5 82            [12]  702 	mov	dpl,a
      00023A EF               [12]  703 	mov	a,r7
      00023B 34 0B            [12]  704 	addc	a,#(_music >> 8)
      00023D F5 83            [12]  705 	mov	dph,a
      00023F E4               [12]  706 	clr	a
      000240 93               [24]  707 	movc	a,@a+dptr
      000241 FF               [12]  708 	mov	r7,a
      000242 1F               [12]  709 	dec	r7
      000243 EF               [12]  710 	mov	a,r7
      000244 2F               [12]  711 	add	a,r7
      000245 24 1E            [12]  712 	add	a,#_table
      000247 F9               [12]  713 	mov	r1,a
      000248 87 16            [24]  714 	mov	ar6,@r1
      00024A 09               [12]  715 	inc	r1
      00024B 87 17            [24]  716 	mov	ar7,@r1
      00024D 8E 12            [24]  717 	mov	ar2,r6
      00024F EF               [12]  718 	mov	a,r7
      000250 FB               [12]  719 	mov	r3,a
      000251 33               [12]  720 	rlc	a
      000252 95 E0            [12]  721 	subb	a,acc
      000254 FC               [12]  722 	mov	r4,a
      000255 FD               [12]  723 	mov	r5,a
      000256 E4               [12]  724 	clr	a
      000257 C3               [12]  725 	clr	c
      000258 9A               [12]  726 	subb	a,r2
      000259 E4               [12]  727 	clr	a
      00025A 9B               [12]  728 	subb	a,r3
      00025B FB               [12]  729 	mov	r3,a
      00025C 74 01            [12]  730 	mov	a,#0x01
      00025E 9C               [12]  731 	subb	a,r4
      00025F E4               [12]  732 	clr	a
      000260 9D               [12]  733 	subb	a,r5
      000261 8B 8D            [24]  734 	mov	_TH1,r3
                                    735 ;	main.c:55: TL1  = (PERIOD-table[music[music_index]-1]) & 0xff;
      000263 C3               [12]  736 	clr	c
      000264 E4               [12]  737 	clr	a
      000265 9E               [12]  738 	subb	a,r6
      000266 FE               [12]  739 	mov	r6,a
      000267 8E 8B            [24]  740 	mov	_TL1,r6
                                    741 ;	main.c:56: P1_5 = !P1_5;
      000269 B2 95            [12]  742 	cpl	_P1_5
                                    743 ;	main.c:58: }
      00026B D0 D0            [24]  744 	pop	psw
      00026D D0 83            [24]  745 	pop	dph
      00026F D0 82            [24]  746 	pop	dpl
      000271 D0 E0            [24]  747 	pop	acc
      000273 32               [24]  748 	reti
                                    749 ;	eliminated unneeded push/pop b
                                    750 ;------------------------------------------------------------
                                    751 ;Allocation info for local variables in function 'keyPressed'
                                    752 ;------------------------------------------------------------
                                    753 ;row                       Allocated with name '_keyPressed_row_65536_12'
                                    754 ;c                         Allocated to registers r4 r5 
                                    755 ;col                       Allocated to registers r2 r3 
                                    756 ;magic                     Allocated to registers r7 r6 
                                    757 ;------------------------------------------------------------
                                    758 ;	main.c:61: short keyPressed(short row) {
                                    759 ;	-----------------------------------------
                                    760 ;	 function keyPressed
                                    761 ;	-----------------------------------------
      000274                        762 _keyPressed:
                           000007   763 	ar7 = 0x07
                           000006   764 	ar6 = 0x06
                           000005   765 	ar5 = 0x05
                           000004   766 	ar4 = 0x04
                           000003   767 	ar3 = 0x03
                           000002   768 	ar2 = 0x02
                           000001   769 	ar1 = 0x01
                           000000   770 	ar0 = 0x00
      000274 85 82 5E         [24]  771 	mov	_keyPressed_row_65536_12,dpl
      000277 85 83 5F         [24]  772 	mov	(_keyPressed_row_65536_12 + 1),dph
                                    773 ;	main.c:62: if((P0 & 0b11110000) != 0b11110000){	//if 按下按鈕
      00027A AC 80            [24]  774 	mov	r4,_P0
      00027C 53 04 F0         [24]  775 	anl	ar4,#0xf0
      00027F 7D 00            [12]  776 	mov	r5,#0x00
      000281 BC F0 05         [24]  777 	cjne	r4,#0xf0,00127$
      000284 BD 00 02         [24]  778 	cjne	r5,#0x00,00127$
      000287 80 56            [24]  779 	sjmp	00105$
      000289                        780 00127$:
                                    781 ;	main.c:63: for (short c = 1, col = 0; col < 4; c *= 2, col++) {
      000289 7C 01            [12]  782 	mov	r4,#0x01
      00028B 7D 00            [12]  783 	mov	r5,#0x00
      00028D 7A 00            [12]  784 	mov	r2,#0x00
      00028F 7B 00            [12]  785 	mov	r3,#0x00
      000291 78 00            [12]  786 	mov	r0,#0x00
      000293 79 00            [12]  787 	mov	r1,#0x00
      000295                        788 00107$:
      000295 C3               [12]  789 	clr	c
      000296 E8               [12]  790 	mov	a,r0
      000297 94 04            [12]  791 	subb	a,#0x04
      000299 E9               [12]  792 	mov	a,r1
      00029A 64 80            [12]  793 	xrl	a,#0x80
      00029C 94 80            [12]  794 	subb	a,#0x80
      00029E 50 3F            [24]  795 	jnc	00105$
                                    796 ;	main.c:65: `			short magic = ((P0 >> 4) ^ 0b11111111) & 0b00001111;
      0002A0 E5 80            [12]  797 	mov	a,_P0
      0002A2 C4               [12]  798 	swap	a
      0002A3 54 0F            [12]  799 	anl	a,#0x0f
      0002A5 FF               [12]  800 	mov	r7,a
      0002A6 63 07 FF         [24]  801 	xrl	ar7,#0xff
      0002A9 53 07 0F         [24]  802 	anl	ar7,#0x0f
      0002AC 7E 00            [12]  803 	mov	r6,#0x00
                                    804 ;	main.c:66: if (magic == c) {
      0002AE EF               [12]  805 	mov	a,r7
      0002AF B5 04 1C         [24]  806 	cjne	a,ar4,00108$
      0002B2 EE               [12]  807 	mov	a,r6
      0002B3 B5 05 18         [24]  808 	cjne	a,ar5,00108$
                                    809 ;	main.c:67: return row * 4 + col;
      0002B6 E5 5E            [12]  810 	mov	a,_keyPressed_row_65536_12
      0002B8 25 5E            [12]  811 	add	a,_keyPressed_row_65536_12
      0002BA FE               [12]  812 	mov	r6,a
      0002BB E5 5F            [12]  813 	mov	a,(_keyPressed_row_65536_12 + 1)
      0002BD 33               [12]  814 	rlc	a
      0002BE FF               [12]  815 	mov	r7,a
      0002BF EE               [12]  816 	mov	a,r6
      0002C0 2E               [12]  817 	add	a,r6
      0002C1 FE               [12]  818 	mov	r6,a
      0002C2 EF               [12]  819 	mov	a,r7
      0002C3 33               [12]  820 	rlc	a
      0002C4 FF               [12]  821 	mov	r7,a
      0002C5 EA               [12]  822 	mov	a,r2
      0002C6 2E               [12]  823 	add	a,r6
      0002C7 F5 82            [12]  824 	mov	dpl,a
      0002C9 EB               [12]  825 	mov	a,r3
      0002CA 3F               [12]  826 	addc	a,r7
      0002CB F5 83            [12]  827 	mov	dph,a
      0002CD 22               [24]  828 	ret
      0002CE                        829 00108$:
                                    830 ;	main.c:63: for (short c = 1, col = 0; col < 4; c *= 2, col++) {
      0002CE EC               [12]  831 	mov	a,r4
      0002CF 2C               [12]  832 	add	a,r4
      0002D0 FC               [12]  833 	mov	r4,a
      0002D1 ED               [12]  834 	mov	a,r5
      0002D2 33               [12]  835 	rlc	a
      0002D3 FD               [12]  836 	mov	r5,a
      0002D4 08               [12]  837 	inc	r0
      0002D5 B8 00 01         [24]  838 	cjne	r0,#0x00,00131$
      0002D8 09               [12]  839 	inc	r1
      0002D9                        840 00131$:
      0002D9 88 02            [24]  841 	mov	ar2,r0
      0002DB 89 03            [24]  842 	mov	ar3,r1
      0002DD 80 B6            [24]  843 	sjmp	00107$
      0002DF                        844 00105$:
                                    845 ;	main.c:71: return -1;	//沒按 return -1
      0002DF 90 FF FF         [24]  846 	mov	dptr,#0xffff
                                    847 ;	main.c:72: }
      0002E2 22               [24]  848 	ret
                                    849 ;------------------------------------------------------------
                                    850 ;Allocation info for local variables in function 'display'
                                    851 ;------------------------------------------------------------
                                    852 ;num                       Allocated with name '_display_PARM_2'
                                    853 ;isSetting                 Allocated with name '_display_PARM_3'
                                    854 ;flash_flag                Allocated with name '_display_PARM_4'
                                    855 ;alpha                     Allocated to registers r5 r6 r7 
                                    856 ;i                         Allocated to registers r1 r2 
                                    857 ;t                         Allocated with name '_display_t_262144_22'
                                    858 ;j                         Allocated to registers r3 r4 
                                    859 ;i                         Allocated to registers r1 r2 
                                    860 ;t                         Allocated with name '_display_t_196608_27'
                                    861 ;j                         Allocated to registers r3 r4 
                                    862 ;------------------------------------------------------------
                                    863 ;	main.c:74: void display(short alpha[], short num[], bool isSetting, long flash_flag) {
                                    864 ;	-----------------------------------------
                                    865 ;	 function display
                                    866 ;	-----------------------------------------
      0002E3                        867 _display:
      0002E3 AD 82            [24]  868 	mov	r5,dpl
      0002E5 AE 83            [24]  869 	mov	r6,dph
      0002E7 AF F0            [24]  870 	mov	r7,b
                                    871 ;	main.c:75: if (isSetting) { // flashing
      0002E9 E5 61            [12]  872 	mov	a,_display_PARM_3
      0002EB 70 03            [24]  873 	jnz	00168$
      0002ED 02 03 CD         [24]  874 	ljmp	00108$
      0002F0                        875 00168$:
                                    876 ;	main.c:76: if (flash_flag > 7800) { // 頻率
      0002F0 C3               [12]  877 	clr	c
      0002F1 74 78            [12]  878 	mov	a,#0x78
      0002F3 95 62            [12]  879 	subb	a,_display_PARM_4
      0002F5 74 1E            [12]  880 	mov	a,#0x1e
      0002F7 95 63            [12]  881 	subb	a,(_display_PARM_4 + 1)
      0002F9 E4               [12]  882 	clr	a
      0002FA 95 64            [12]  883 	subb	a,(_display_PARM_4 + 2)
      0002FC 74 80            [12]  884 	mov	a,#(0x00 ^ 0x80)
      0002FE 85 65 F0         [24]  885 	mov	b,(_display_PARM_4 + 3)
      000301 63 F0 80         [24]  886 	xrl	b,#0x80
      000304 95 F0            [12]  887 	subb	a,b
      000306 40 01            [24]  888 	jc	00169$
      000308 22               [24]  889 	ret
      000309                        890 00169$:
                                    891 ;	main.c:77: for(short i = 0,t=1; i < 4; i++,t*=2) {
      000309 75 66 01         [24]  892 	mov	_display_t_262144_22,#0x01
      00030C 75 67 00         [24]  893 	mov	(_display_t_262144_22 + 1),#0x00
      00030F 79 00            [12]  894 	mov	r1,#0x00
      000311 7A 00            [12]  895 	mov	r2,#0x00
      000313                        896 00114$:
      000313 C3               [12]  897 	clr	c
      000314 E9               [12]  898 	mov	a,r1
      000315 94 04            [12]  899 	subb	a,#0x04
      000317 EA               [12]  900 	mov	a,r2
      000318 64 80            [12]  901 	xrl	a,#0x80
      00031A 94 80            [12]  902 	subb	a,#0x80
      00031C 40 01            [24]  903 	jc	00170$
      00031E 22               [24]  904 	ret
      00031F                        905 00170$:
                                    906 ;	main.c:78: P1_0 = table_LED[i][3];
      00031F 89 00            [24]  907 	mov	ar0,r1
      000321 EA               [12]  908 	mov	a,r2
      000322 C4               [12]  909 	swap	a
      000323 03               [12]  910 	rr	a
      000324 54 F8            [12]  911 	anl	a,#0xf8
      000326 C8               [12]  912 	xch	a,r0
      000327 C4               [12]  913 	swap	a
      000328 03               [12]  914 	rr	a
      000329 C8               [12]  915 	xch	a,r0
      00032A 68               [12]  916 	xrl	a,r0
      00032B C8               [12]  917 	xch	a,r0
      00032C 54 F8            [12]  918 	anl	a,#0xf8
      00032E C8               [12]  919 	xch	a,r0
      00032F 68               [12]  920 	xrl	a,r0
      000330 FC               [12]  921 	mov	r4,a
      000331 E8               [12]  922 	mov	a,r0
      000332 24 D2            [12]  923 	add	a,#_table_LED
      000334 F8               [12]  924 	mov	r0,a
      000335 EC               [12]  925 	mov	a,r4
      000336 34 0B            [12]  926 	addc	a,#(_table_LED >> 8)
      000338 FC               [12]  927 	mov	r4,a
      000339 74 06            [12]  928 	mov	a,#0x06
      00033B 28               [12]  929 	add	a,r0
      00033C F5 82            [12]  930 	mov	dpl,a
      00033E E4               [12]  931 	clr	a
      00033F 3C               [12]  932 	addc	a,r4
      000340 F5 83            [12]  933 	mov	dph,a
      000342 E4               [12]  934 	clr	a
      000343 93               [24]  935 	movc	a,@a+dptr
      000344 24 FF            [12]  936 	add	a,#0xff
      000346 92 90            [24]  937 	mov	_P1_0,c
                                    938 ;	main.c:79: P1_1 = table_LED[i][2];
      000348 88 82            [24]  939 	mov	dpl,r0
      00034A 8C 83            [24]  940 	mov	dph,r4
      00034C A3               [24]  941 	inc	dptr
      00034D A3               [24]  942 	inc	dptr
      00034E A3               [24]  943 	inc	dptr
      00034F A3               [24]  944 	inc	dptr
      000350 E4               [12]  945 	clr	a
      000351 93               [24]  946 	movc	a,@a+dptr
      000352 24 FF            [12]  947 	add	a,#0xff
      000354 92 91            [24]  948 	mov	_P1_1,c
                                    949 ;	main.c:80: P1_2 = table_LED[i][1];
      000356 88 82            [24]  950 	mov	dpl,r0
      000358 8C 83            [24]  951 	mov	dph,r4
      00035A A3               [24]  952 	inc	dptr
      00035B A3               [24]  953 	inc	dptr
      00035C E4               [12]  954 	clr	a
      00035D 93               [24]  955 	movc	a,@a+dptr
      00035E 24 FF            [12]  956 	add	a,#0xff
      000360 92 92            [24]  957 	mov	_P1_2,c
                                    958 ;	main.c:81: P1_3 = table_LED[i][0];
      000362 88 82            [24]  959 	mov	dpl,r0
      000364 8C 83            [24]  960 	mov	dph,r4
      000366 E4               [12]  961 	clr	a
      000367 93               [24]  962 	movc	a,@a+dptr
      000368 24 FF            [12]  963 	add	a,#0xff
      00036A 92 93            [24]  964 	mov	_P1_3,c
                                    965 ;	main.c:82: P2 = alpha[num[i]];
      00036C E9               [12]  966 	mov	a,r1
      00036D 29               [12]  967 	add	a,r1
      00036E FB               [12]  968 	mov	r3,a
      00036F EA               [12]  969 	mov	a,r2
      000370 33               [12]  970 	rlc	a
      000371 FC               [12]  971 	mov	r4,a
      000372 EB               [12]  972 	mov	a,r3
      000373 25 5E            [12]  973 	add	a,_display_PARM_2
      000375 FB               [12]  974 	mov	r3,a
      000376 EC               [12]  975 	mov	a,r4
      000377 35 5F            [12]  976 	addc	a,(_display_PARM_2 + 1)
      000379 F8               [12]  977 	mov	r0,a
      00037A AC 60            [24]  978 	mov	r4,(_display_PARM_2 + 2)
      00037C 8B 82            [24]  979 	mov	dpl,r3
      00037E 88 83            [24]  980 	mov	dph,r0
      000380 8C F0            [24]  981 	mov	b,r4
      000382 12 0A D5         [24]  982 	lcall	__gptrget
      000385 FB               [12]  983 	mov	r3,a
      000386 A3               [24]  984 	inc	dptr
      000387 12 0A D5         [24]  985 	lcall	__gptrget
      00038A F8               [12]  986 	mov	r0,a
      00038B EB               [12]  987 	mov	a,r3
      00038C 2B               [12]  988 	add	a,r3
      00038D FB               [12]  989 	mov	r3,a
      00038E E8               [12]  990 	mov	a,r0
      00038F 33               [12]  991 	rlc	a
      000390 F8               [12]  992 	mov	r0,a
      000391 EB               [12]  993 	mov	a,r3
      000392 2D               [12]  994 	add	a,r5
      000393 FB               [12]  995 	mov	r3,a
      000394 E8               [12]  996 	mov	a,r0
      000395 3E               [12]  997 	addc	a,r6
      000396 F8               [12]  998 	mov	r0,a
      000397 8F 04            [24]  999 	mov	ar4,r7
      000399 8B 82            [24] 1000 	mov	dpl,r3
      00039B 88 83            [24] 1001 	mov	dph,r0
      00039D 8C F0            [24] 1002 	mov	b,r4
      00039F 12 0A D5         [24] 1003 	lcall	__gptrget
      0003A2 F5 A0            [12] 1004 	mov	_P2,a
                                   1005 ;	main.c:83: for(int j = 0; j < 500; j++){}
      0003A4 7B 00            [12] 1006 	mov	r3,#0x00
      0003A6 7C 00            [12] 1007 	mov	r4,#0x00
      0003A8                       1008 00111$:
      0003A8 C3               [12] 1009 	clr	c
      0003A9 EB               [12] 1010 	mov	a,r3
      0003AA 94 F4            [12] 1011 	subb	a,#0xf4
      0003AC EC               [12] 1012 	mov	a,r4
      0003AD 64 80            [12] 1013 	xrl	a,#0x80
      0003AF 94 81            [12] 1014 	subb	a,#0x81
      0003B1 50 07            [24] 1015 	jnc	00115$
      0003B3 0B               [12] 1016 	inc	r3
      0003B4 BB 00 F1         [24] 1017 	cjne	r3,#0x00,00111$
      0003B7 0C               [12] 1018 	inc	r4
      0003B8 80 EE            [24] 1019 	sjmp	00111$
      0003BA                       1020 00115$:
                                   1021 ;	main.c:77: for(short i = 0,t=1; i < 4; i++,t*=2) {
      0003BA 09               [12] 1022 	inc	r1
      0003BB B9 00 01         [24] 1023 	cjne	r1,#0x00,00173$
      0003BE 0A               [12] 1024 	inc	r2
      0003BF                       1025 00173$:
      0003BF E5 66            [12] 1026 	mov	a,_display_t_262144_22
      0003C1 25 66            [12] 1027 	add	a,_display_t_262144_22
      0003C3 F5 66            [12] 1028 	mov	_display_t_262144_22,a
      0003C5 E5 67            [12] 1029 	mov	a,(_display_t_262144_22 + 1)
      0003C7 33               [12] 1030 	rlc	a
      0003C8 F5 67            [12] 1031 	mov	(_display_t_262144_22 + 1),a
      0003CA 02 03 13         [24] 1032 	ljmp	00114$
      0003CD                       1033 00108$:
                                   1034 ;	main.c:87: for(short i = 0,t=1; i < 4; i++,t*=2) {
      0003CD 75 68 01         [24] 1035 	mov	_display_t_196608_27,#0x01
      0003D0 75 69 00         [24] 1036 	mov	(_display_t_196608_27 + 1),#0x00
      0003D3 79 00            [12] 1037 	mov	r1,#0x00
      0003D5 7A 00            [12] 1038 	mov	r2,#0x00
      0003D7                       1039 00120$:
      0003D7 C3               [12] 1040 	clr	c
      0003D8 E9               [12] 1041 	mov	a,r1
      0003D9 94 04            [12] 1042 	subb	a,#0x04
      0003DB EA               [12] 1043 	mov	a,r2
      0003DC 64 80            [12] 1044 	xrl	a,#0x80
      0003DE 94 80            [12] 1045 	subb	a,#0x80
      0003E0 40 01            [24] 1046 	jc	00174$
      0003E2 22               [24] 1047 	ret
      0003E3                       1048 00174$:
                                   1049 ;	main.c:88: P1_0 = table_LED[i][3];
      0003E3 89 00            [24] 1050 	mov	ar0,r1
      0003E5 EA               [12] 1051 	mov	a,r2
      0003E6 C4               [12] 1052 	swap	a
      0003E7 03               [12] 1053 	rr	a
      0003E8 54 F8            [12] 1054 	anl	a,#0xf8
      0003EA C8               [12] 1055 	xch	a,r0
      0003EB C4               [12] 1056 	swap	a
      0003EC 03               [12] 1057 	rr	a
      0003ED C8               [12] 1058 	xch	a,r0
      0003EE 68               [12] 1059 	xrl	a,r0
      0003EF C8               [12] 1060 	xch	a,r0
      0003F0 54 F8            [12] 1061 	anl	a,#0xf8
      0003F2 C8               [12] 1062 	xch	a,r0
      0003F3 68               [12] 1063 	xrl	a,r0
      0003F4 FC               [12] 1064 	mov	r4,a
      0003F5 E8               [12] 1065 	mov	a,r0
      0003F6 24 D2            [12] 1066 	add	a,#_table_LED
      0003F8 F8               [12] 1067 	mov	r0,a
      0003F9 EC               [12] 1068 	mov	a,r4
      0003FA 34 0B            [12] 1069 	addc	a,#(_table_LED >> 8)
      0003FC FC               [12] 1070 	mov	r4,a
      0003FD 74 06            [12] 1071 	mov	a,#0x06
      0003FF 28               [12] 1072 	add	a,r0
      000400 F5 82            [12] 1073 	mov	dpl,a
      000402 E4               [12] 1074 	clr	a
      000403 3C               [12] 1075 	addc	a,r4
      000404 F5 83            [12] 1076 	mov	dph,a
      000406 E4               [12] 1077 	clr	a
      000407 93               [24] 1078 	movc	a,@a+dptr
      000408 24 FF            [12] 1079 	add	a,#0xff
      00040A 92 90            [24] 1080 	mov	_P1_0,c
                                   1081 ;	main.c:89: P1_1 = table_LED[i][2];
      00040C 88 82            [24] 1082 	mov	dpl,r0
      00040E 8C 83            [24] 1083 	mov	dph,r4
      000410 A3               [24] 1084 	inc	dptr
      000411 A3               [24] 1085 	inc	dptr
      000412 A3               [24] 1086 	inc	dptr
      000413 A3               [24] 1087 	inc	dptr
      000414 E4               [12] 1088 	clr	a
      000415 93               [24] 1089 	movc	a,@a+dptr
      000416 24 FF            [12] 1090 	add	a,#0xff
      000418 92 91            [24] 1091 	mov	_P1_1,c
                                   1092 ;	main.c:90: P1_2 = table_LED[i][1];
      00041A 88 82            [24] 1093 	mov	dpl,r0
      00041C 8C 83            [24] 1094 	mov	dph,r4
      00041E A3               [24] 1095 	inc	dptr
      00041F A3               [24] 1096 	inc	dptr
      000420 E4               [12] 1097 	clr	a
      000421 93               [24] 1098 	movc	a,@a+dptr
      000422 24 FF            [12] 1099 	add	a,#0xff
      000424 92 92            [24] 1100 	mov	_P1_2,c
                                   1101 ;	main.c:91: P1_3 = table_LED[i][0];
      000426 88 82            [24] 1102 	mov	dpl,r0
      000428 8C 83            [24] 1103 	mov	dph,r4
      00042A E4               [12] 1104 	clr	a
      00042B 93               [24] 1105 	movc	a,@a+dptr
      00042C 24 FF            [12] 1106 	add	a,#0xff
      00042E 92 93            [24] 1107 	mov	_P1_3,c
                                   1108 ;	main.c:92: P2 = alpha[num[i]];
      000430 E9               [12] 1109 	mov	a,r1
      000431 29               [12] 1110 	add	a,r1
      000432 FB               [12] 1111 	mov	r3,a
      000433 EA               [12] 1112 	mov	a,r2
      000434 33               [12] 1113 	rlc	a
      000435 FC               [12] 1114 	mov	r4,a
      000436 EB               [12] 1115 	mov	a,r3
      000437 25 5E            [12] 1116 	add	a,_display_PARM_2
      000439 FB               [12] 1117 	mov	r3,a
      00043A EC               [12] 1118 	mov	a,r4
      00043B 35 5F            [12] 1119 	addc	a,(_display_PARM_2 + 1)
      00043D F8               [12] 1120 	mov	r0,a
      00043E AC 60            [24] 1121 	mov	r4,(_display_PARM_2 + 2)
      000440 8B 82            [24] 1122 	mov	dpl,r3
      000442 88 83            [24] 1123 	mov	dph,r0
      000444 8C F0            [24] 1124 	mov	b,r4
      000446 12 0A D5         [24] 1125 	lcall	__gptrget
      000449 FB               [12] 1126 	mov	r3,a
      00044A A3               [24] 1127 	inc	dptr
      00044B 12 0A D5         [24] 1128 	lcall	__gptrget
      00044E F8               [12] 1129 	mov	r0,a
      00044F EB               [12] 1130 	mov	a,r3
      000450 2B               [12] 1131 	add	a,r3
      000451 FB               [12] 1132 	mov	r3,a
      000452 E8               [12] 1133 	mov	a,r0
      000453 33               [12] 1134 	rlc	a
      000454 F8               [12] 1135 	mov	r0,a
      000455 EB               [12] 1136 	mov	a,r3
      000456 2D               [12] 1137 	add	a,r5
      000457 FB               [12] 1138 	mov	r3,a
      000458 E8               [12] 1139 	mov	a,r0
      000459 3E               [12] 1140 	addc	a,r6
      00045A F8               [12] 1141 	mov	r0,a
      00045B 8F 04            [24] 1142 	mov	ar4,r7
      00045D 8B 82            [24] 1143 	mov	dpl,r3
      00045F 88 83            [24] 1144 	mov	dph,r0
      000461 8C F0            [24] 1145 	mov	b,r4
      000463 12 0A D5         [24] 1146 	lcall	__gptrget
      000466 F5 A0            [12] 1147 	mov	_P2,a
                                   1148 ;	main.c:93: for(int j = 0; j < 1000; j++){}
      000468 7B 00            [12] 1149 	mov	r3,#0x00
      00046A 7C 00            [12] 1150 	mov	r4,#0x00
      00046C                       1151 00117$:
      00046C C3               [12] 1152 	clr	c
      00046D EB               [12] 1153 	mov	a,r3
      00046E 94 E8            [12] 1154 	subb	a,#0xe8
      000470 EC               [12] 1155 	mov	a,r4
      000471 64 80            [12] 1156 	xrl	a,#0x80
      000473 94 83            [12] 1157 	subb	a,#0x83
      000475 50 07            [24] 1158 	jnc	00121$
      000477 0B               [12] 1159 	inc	r3
      000478 BB 00 F1         [24] 1160 	cjne	r3,#0x00,00117$
      00047B 0C               [12] 1161 	inc	r4
      00047C 80 EE            [24] 1162 	sjmp	00117$
      00047E                       1163 00121$:
                                   1164 ;	main.c:87: for(short i = 0,t=1; i < 4; i++,t*=2) {
      00047E 09               [12] 1165 	inc	r1
      00047F B9 00 01         [24] 1166 	cjne	r1,#0x00,00177$
      000482 0A               [12] 1167 	inc	r2
      000483                       1168 00177$:
      000483 E5 68            [12] 1169 	mov	a,_display_t_196608_27
      000485 25 68            [12] 1170 	add	a,_display_t_196608_27
      000487 F5 68            [12] 1171 	mov	_display_t_196608_27,a
      000489 E5 69            [12] 1172 	mov	a,(_display_t_196608_27 + 1)
      00048B 33               [12] 1173 	rlc	a
      00048C F5 69            [12] 1174 	mov	(_display_t_196608_27 + 1),a
                                   1175 ;	main.c:96: }
      00048E 02 03 D7         [24] 1176 	ljmp	00120$
                                   1177 ;------------------------------------------------------------
                                   1178 ;Allocation info for local variables in function 'check_sound_trigger'
                                   1179 ;------------------------------------------------------------
                                   1180 ;num_bi                    Allocated with name '_check_sound_trigger_PARM_2'
                                   1181 ;num                       Allocated with name '_check_sound_trigger_num_65536_31'
                                   1182 ;i                         Allocated to registers r3 r4 
                                   1183 ;------------------------------------------------------------
                                   1184 ;	main.c:98: void check_sound_trigger(short num[], short num_bi[]) {
                                   1185 ;	-----------------------------------------
                                   1186 ;	 function check_sound_trigger
                                   1187 ;	-----------------------------------------
      000491                       1188 _check_sound_trigger:
      000491 85 82 61         [24] 1189 	mov	_check_sound_trigger_num_65536_31,dpl
      000494 85 83 62         [24] 1190 	mov	(_check_sound_trigger_num_65536_31 + 1),dph
      000497 85 F0 63         [24] 1191 	mov	(_check_sound_trigger_num_65536_31 + 2),b
                                   1192 ;	main.c:99: for (int i = 0; i < 4; i++) {
      00049A 7B 00            [12] 1193 	mov	r3,#0x00
      00049C 7C 00            [12] 1194 	mov	r4,#0x00
      00049E                       1195 00105$:
      00049E C3               [12] 1196 	clr	c
      00049F EB               [12] 1197 	mov	a,r3
      0004A0 94 04            [12] 1198 	subb	a,#0x04
      0004A2 EC               [12] 1199 	mov	a,r4
      0004A3 64 80            [12] 1200 	xrl	a,#0x80
      0004A5 94 80            [12] 1201 	subb	a,#0x80
      0004A7 50 47            [24] 1202 	jnc	00103$
                                   1203 ;	main.c:100: if (num[i] != num_bi[i]) 
      0004A9 EB               [12] 1204 	mov	a,r3
      0004AA 2B               [12] 1205 	add	a,r3
      0004AB F9               [12] 1206 	mov	r1,a
      0004AC EC               [12] 1207 	mov	a,r4
      0004AD 33               [12] 1208 	rlc	a
      0004AE FA               [12] 1209 	mov	r2,a
      0004AF E9               [12] 1210 	mov	a,r1
      0004B0 25 61            [12] 1211 	add	a,_check_sound_trigger_num_65536_31
      0004B2 F8               [12] 1212 	mov	r0,a
      0004B3 EA               [12] 1213 	mov	a,r2
      0004B4 35 62            [12] 1214 	addc	a,(_check_sound_trigger_num_65536_31 + 1)
      0004B6 FE               [12] 1215 	mov	r6,a
      0004B7 AF 63            [24] 1216 	mov	r7,(_check_sound_trigger_num_65536_31 + 2)
      0004B9 88 82            [24] 1217 	mov	dpl,r0
      0004BB 8E 83            [24] 1218 	mov	dph,r6
      0004BD 8F F0            [24] 1219 	mov	b,r7
      0004BF 12 0A D5         [24] 1220 	lcall	__gptrget
      0004C2 F8               [12] 1221 	mov	r0,a
      0004C3 A3               [24] 1222 	inc	dptr
      0004C4 12 0A D5         [24] 1223 	lcall	__gptrget
      0004C7 FE               [12] 1224 	mov	r6,a
      0004C8 E9               [12] 1225 	mov	a,r1
      0004C9 25 5E            [12] 1226 	add	a,_check_sound_trigger_PARM_2
      0004CB F9               [12] 1227 	mov	r1,a
      0004CC EA               [12] 1228 	mov	a,r2
      0004CD 35 5F            [12] 1229 	addc	a,(_check_sound_trigger_PARM_2 + 1)
      0004CF FA               [12] 1230 	mov	r2,a
      0004D0 AF 60            [24] 1231 	mov	r7,(_check_sound_trigger_PARM_2 + 2)
      0004D2 89 82            [24] 1232 	mov	dpl,r1
      0004D4 8A 83            [24] 1233 	mov	dph,r2
      0004D6 8F F0            [24] 1234 	mov	b,r7
      0004D8 12 0A D5         [24] 1235 	lcall	__gptrget
      0004DB F9               [12] 1236 	mov	r1,a
      0004DC A3               [24] 1237 	inc	dptr
      0004DD 12 0A D5         [24] 1238 	lcall	__gptrget
      0004E0 FA               [12] 1239 	mov	r2,a
      0004E1 E8               [12] 1240 	mov	a,r0
                                   1241 ;	main.c:101: return;
      0004E2 B5 01 0D         [24] 1242 	cjne	a,ar1,00107$
      0004E5 EE               [12] 1243 	mov	a,r6
      0004E6 B5 02 09         [24] 1244 	cjne	a,ar2,00107$
                                   1245 ;	main.c:99: for (int i = 0; i < 4; i++) {
      0004E9 0B               [12] 1246 	inc	r3
      0004EA BB 00 B1         [24] 1247 	cjne	r3,#0x00,00105$
      0004ED 0C               [12] 1248 	inc	r4
      0004EE 80 AE            [24] 1249 	sjmp	00105$
      0004F0                       1250 00103$:
                                   1251 ;	main.c:103: TR1 = 1;
                                   1252 ;	assignBit
      0004F0 D2 8E            [12] 1253 	setb	_TR1
      0004F2                       1254 00107$:
                                   1255 ;	main.c:104: }
      0004F2 22               [24] 1256 	ret
                                   1257 ;------------------------------------------------------------
                                   1258 ;Allocation info for local variables in function 'init'
                                   1259 ;------------------------------------------------------------
                                   1260 ;tmp                       Allocated to registers r2 r3 r4 r5 
                                   1261 ;i                         Allocated to registers r6 r7 
                                   1262 ;i                         Allocated to registers r6 r7 
                                   1263 ;------------------------------------------------------------
                                   1264 ;	main.c:106: void init(){
                                   1265 ;	-----------------------------------------
                                   1266 ;	 function init
                                   1267 ;	-----------------------------------------
      0004F3                       1268 _init:
                                   1269 ;	main.c:107: music_index=0;
      0004F3 E4               [12] 1270 	clr	a
      0004F4 F5 1A            [12] 1271 	mov	_music_index,a
      0004F6 F5 1B            [12] 1272 	mov	(_music_index + 1),a
                                   1273 ;	main.c:109: for(int i=7;i<16;i++){
      0004F8 7E 07            [12] 1274 	mov	r6,#0x07
      0004FA 7F 00            [12] 1275 	mov	r7,#0x00
      0004FC                       1276 00104$:
      0004FC C3               [12] 1277 	clr	c
      0004FD EE               [12] 1278 	mov	a,r6
      0004FE 94 10            [12] 1279 	subb	a,#0x10
      000500 EF               [12] 1280 	mov	a,r7
      000501 64 80            [12] 1281 	xrl	a,#0x80
      000503 94 80            [12] 1282 	subb	a,#0x80
      000505 50 2C            [24] 1283 	jnc	00101$
                                   1284 ;	main.c:110: table[i]=table[i-7]*2;
      000507 EE               [12] 1285 	mov	a,r6
      000508 2E               [12] 1286 	add	a,r6
      000509 FC               [12] 1287 	mov	r4,a
      00050A EF               [12] 1288 	mov	a,r7
      00050B 33               [12] 1289 	rlc	a
      00050C EC               [12] 1290 	mov	a,r4
      00050D 24 1E            [12] 1291 	add	a,#_table
      00050F F9               [12] 1292 	mov	r1,a
      000510 8E 05            [24] 1293 	mov	ar5,r6
      000512 ED               [12] 1294 	mov	a,r5
      000513 24 F9            [12] 1295 	add	a,#0xf9
      000515 25 E0            [12] 1296 	add	a,acc
      000517 24 1E            [12] 1297 	add	a,#_table
      000519 F8               [12] 1298 	mov	r0,a
      00051A 86 04            [24] 1299 	mov	ar4,@r0
      00051C 08               [12] 1300 	inc	r0
      00051D 86 05            [24] 1301 	mov	ar5,@r0
      00051F 18               [12] 1302 	dec	r0
      000520 EC               [12] 1303 	mov	a,r4
      000521 2C               [12] 1304 	add	a,r4
      000522 FC               [12] 1305 	mov	r4,a
      000523 ED               [12] 1306 	mov	a,r5
      000524 33               [12] 1307 	rlc	a
      000525 FD               [12] 1308 	mov	r5,a
      000526 A7 04            [24] 1309 	mov	@r1,ar4
      000528 09               [12] 1310 	inc	r1
      000529 A7 05            [24] 1311 	mov	@r1,ar5
      00052B 19               [12] 1312 	dec	r1
                                   1313 ;	main.c:109: for(int i=7;i<16;i++){
      00052C 0E               [12] 1314 	inc	r6
      00052D BE 00 CC         [24] 1315 	cjne	r6,#0x00,00104$
      000530 0F               [12] 1316 	inc	r7
      000531 80 C9            [24] 1317 	sjmp	00104$
      000533                       1318 00101$:
                                   1319 ;	main.c:112: for(int i=0;i<16;i++){
      000533 7E 00            [12] 1320 	mov	r6,#0x00
      000535 7F 00            [12] 1321 	mov	r7,#0x00
      000537                       1322 00107$:
      000537 C3               [12] 1323 	clr	c
      000538 EE               [12] 1324 	mov	a,r6
      000539 94 10            [12] 1325 	subb	a,#0x10
      00053B EF               [12] 1326 	mov	a,r7
      00053C 64 80            [12] 1327 	xrl	a,#0x80
      00053E 94 80            [12] 1328 	subb	a,#0x80
      000540 40 01            [24] 1329 	jc	00131$
      000542 22               [24] 1330 	ret
      000543                       1331 00131$:
                                   1332 ;	main.c:113: tmp=1.0/table[i]*1000000;
      000543 EE               [12] 1333 	mov	a,r6
      000544 2E               [12] 1334 	add	a,r6
      000545 FC               [12] 1335 	mov	r4,a
      000546 EF               [12] 1336 	mov	a,r7
      000547 33               [12] 1337 	rlc	a
      000548 EC               [12] 1338 	mov	a,r4
      000549 24 1E            [12] 1339 	add	a,#_table
      00054B F9               [12] 1340 	mov	r1,a
      00054C 87 82            [24] 1341 	mov	dpl,@r1
      00054E 09               [12] 1342 	inc	r1
      00054F 87 83            [24] 1343 	mov	dph,@r1
      000551 19               [12] 1344 	dec	r1
      000552 C0 07            [24] 1345 	push	ar7
      000554 C0 06            [24] 1346 	push	ar6
      000556 C0 01            [24] 1347 	push	ar1
      000558 12 09 82         [24] 1348 	lcall	___sint2fs
      00055B AA 82            [24] 1349 	mov	r2,dpl
      00055D AB 83            [24] 1350 	mov	r3,dph
      00055F AC F0            [24] 1351 	mov	r4,b
      000561 FD               [12] 1352 	mov	r5,a
      000562 C0 02            [24] 1353 	push	ar2
      000564 C0 03            [24] 1354 	push	ar3
      000566 C0 04            [24] 1355 	push	ar4
      000568 C0 05            [24] 1356 	push	ar5
      00056A 90 00 00         [24] 1357 	mov	dptr,#0x0000
      00056D 75 F0 80         [24] 1358 	mov	b,#0x80
      000570 74 3F            [12] 1359 	mov	a,#0x3f
      000572 12 0A 12         [24] 1360 	lcall	___fsdiv
      000575 AA 82            [24] 1361 	mov	r2,dpl
      000577 AB 83            [24] 1362 	mov	r3,dph
      000579 AC F0            [24] 1363 	mov	r4,b
      00057B FD               [12] 1364 	mov	r5,a
      00057C E5 81            [12] 1365 	mov	a,sp
      00057E 24 FC            [12] 1366 	add	a,#0xfc
      000580 F5 81            [12] 1367 	mov	sp,a
      000582 C0 02            [24] 1368 	push	ar2
      000584 C0 03            [24] 1369 	push	ar3
      000586 C0 04            [24] 1370 	push	ar4
      000588 C0 05            [24] 1371 	push	ar5
      00058A 90 24 00         [24] 1372 	mov	dptr,#0x2400
      00058D 75 F0 74         [24] 1373 	mov	b,#0x74
      000590 74 49            [12] 1374 	mov	a,#0x49
      000592 12 08 63         [24] 1375 	lcall	___fsmul
      000595 AA 82            [24] 1376 	mov	r2,dpl
      000597 AB 83            [24] 1377 	mov	r3,dph
      000599 AC F0            [24] 1378 	mov	r4,b
      00059B FD               [12] 1379 	mov	r5,a
      00059C E5 81            [12] 1380 	mov	a,sp
      00059E 24 FC            [12] 1381 	add	a,#0xfc
      0005A0 F5 81            [12] 1382 	mov	sp,a
                                   1383 ;	main.c:114: table[i]=tmp;
      0005A2 8A 82            [24] 1384 	mov	dpl,r2
      0005A4 8B 83            [24] 1385 	mov	dph,r3
      0005A6 8C F0            [24] 1386 	mov	b,r4
      0005A8 ED               [12] 1387 	mov	a,r5
      0005A9 12 09 8F         [24] 1388 	lcall	___fs2sint
      0005AC E5 82            [12] 1389 	mov	a,dpl
      0005AE 85 83 F0         [24] 1390 	mov	b,dph
      0005B1 D0 01            [24] 1391 	pop	ar1
      0005B3 D0 06            [24] 1392 	pop	ar6
      0005B5 D0 07            [24] 1393 	pop	ar7
      0005B7 F7               [12] 1394 	mov	@r1,a
      0005B8 09               [12] 1395 	inc	r1
      0005B9 A7 F0            [24] 1396 	mov	@r1,b
      0005BB 19               [12] 1397 	dec	r1
                                   1398 ;	main.c:112: for(int i=0;i<16;i++){
      0005BC 0E               [12] 1399 	inc	r6
      0005BD BE 00 01         [24] 1400 	cjne	r6,#0x00,00132$
      0005C0 0F               [12] 1401 	inc	r7
      0005C1                       1402 00132$:
                                   1403 ;	main.c:116: }
      0005C1 02 05 37         [24] 1404 	ljmp	00107$
                                   1405 ;------------------------------------------------------------
                                   1406 ;Allocation info for local variables in function 'main'
                                   1407 ;------------------------------------------------------------
                                   1408 ;previous                  Allocated with name '_main_previous_65537_42'
                                   1409 ;row                       Allocated with name '_main_row_65537_42'
                                   1410 ;count                     Allocated with name '_main_count_65537_42'
                                   1411 ;num                       Allocated with name '_main_num_65537_42'
                                   1412 ;num_bi                    Allocated with name '_main_num_bi_65537_42'
                                   1413 ;alpha                     Allocated with name '_main_alpha_65537_42'
                                   1414 ;index                     Allocated with name '_main_index_65538_43'
                                   1415 ;flash_flag                Allocated with name '_main_flash_flag_65538_43'
                                   1416 ;isSetting                 Allocated to registers r5 
                                   1417 ;afterSetting              Allocated to registers 
                                   1418 ;setting_bi_time           Allocated to registers r4 
                                   1419 ;key                       Allocated to registers r2 r3 
                                   1420 ;------------------------------------------------------------
                                   1421 ;	main.c:118: int main() {
                                   1422 ;	-----------------------------------------
                                   1423 ;	 function main
                                   1424 ;	-----------------------------------------
      0005C4                       1425 _main:
                                   1426 ;	main.c:119: init();
      0005C4 12 04 F3         [24] 1427 	lcall	_init
                                   1428 ;	main.c:130: P1_5=0;
                                   1429 ;	assignBit
      0005C7 C2 95            [12] 1430 	clr	_P1_5
                                   1431 ;	main.c:132: EA = 1;
                                   1432 ;	assignBit
      0005C9 D2 AF            [12] 1433 	setb	_EA
                                   1434 ;	main.c:133: TMOD = 0b00010001;
      0005CB 75 89 11         [24] 1435 	mov	_TMOD,#0x11
                                   1436 ;	main.c:134: IE   = 0x8A;
      0005CE 75 A8 8A         [24] 1437 	mov	_IE,#0x8a
                                   1438 ;	main.c:135: TR0  = 1;	//timer 0 control bit
                                   1439 ;	assignBit
      0005D1 D2 8C            [12] 1440 	setb	_TR0
                                   1441 ;	main.c:136: TR1  = 0;	//speaker timer 1 control bit
                                   1442 ;	assignBit
      0005D3 C2 8E            [12] 1443 	clr	_TR1
                                   1444 ;	main.c:138: short previous = -1;
      0005D5 75 2C FF         [24] 1445 	mov	_main_previous_65537_42,#0xff
      0005D8 75 2D FF         [24] 1446 	mov	(_main_previous_65537_42 + 1),#0xff
                                   1447 ;	main.c:139: short row = 0;
      0005DB E4               [12] 1448 	clr	a
      0005DC F5 2E            [12] 1449 	mov	_main_row_65537_42,a
      0005DE F5 2F            [12] 1450 	mov	(_main_row_65537_42 + 1),a
                                   1451 ;	main.c:140: short count = 1;
      0005E0 75 30 01         [24] 1452 	mov	_main_count_65537_42,#0x01
                                   1453 ;	1-genFromRTrack replaced	mov	(_main_count_65537_42 + 1),#0x00
      0005E3 F5 31            [12] 1454 	mov	(_main_count_65537_42 + 1),a
                                   1455 ;	main.c:141: short num[4] = {0};
      0005E5 F5 32            [12] 1456 	mov	(_main_num_65537_42 + 0),a
      0005E7 F5 33            [12] 1457 	mov	(_main_num_65537_42 + 1),a
      0005E9 F5 34            [12] 1458 	mov	((_main_num_65537_42 + 0x0002) + 0),a
      0005EB F5 35            [12] 1459 	mov	((_main_num_65537_42 + 0x0002) + 1),a
      0005ED F5 36            [12] 1460 	mov	((_main_num_65537_42 + 0x0004) + 0),a
      0005EF F5 37            [12] 1461 	mov	((_main_num_65537_42 + 0x0004) + 1),a
      0005F1 F5 38            [12] 1462 	mov	((_main_num_65537_42 + 0x0006) + 0),a
      0005F3 F5 39            [12] 1463 	mov	((_main_num_65537_42 + 0x0006) + 1),a
                                   1464 ;	main.c:142: short num_bi[4] = {-1};
      0005F5 75 3A FF         [24] 1465 	mov	(_main_num_bi_65537_42 + 0),#0xff
      0005F8 75 3B FF         [24] 1466 	mov	(_main_num_bi_65537_42 + 1),#0xff
      0005FB F5 3C            [12] 1467 	mov	((_main_num_bi_65537_42 + 0x0002) + 0),a
      0005FD F5 3D            [12] 1468 	mov	((_main_num_bi_65537_42 + 0x0002) + 1),a
      0005FF F5 3E            [12] 1469 	mov	((_main_num_bi_65537_42 + 0x0004) + 0),a
      000601 F5 3F            [12] 1470 	mov	((_main_num_bi_65537_42 + 0x0004) + 1),a
      000603 F5 40            [12] 1471 	mov	((_main_num_bi_65537_42 + 0x0006) + 0),a
      000605 F5 41            [12] 1472 	mov	((_main_num_bi_65537_42 + 0x0006) + 1),a
                                   1473 ;	main.c:143: const short alpha[11] = {
      000607 75 42 03         [24] 1474 	mov	(_main_alpha_65537_42 + 0),#0x03
                                   1475 ;	1-genFromRTrack replaced	mov	(_main_alpha_65537_42 + 1),#0x00
      00060A F5 43            [12] 1476 	mov	(_main_alpha_65537_42 + 1),a
      00060C 75 44 9F         [24] 1477 	mov	((_main_alpha_65537_42 + 0x0002) + 0),#0x9f
                                   1478 ;	1-genFromRTrack replaced	mov	((_main_alpha_65537_42 + 0x0002) + 1),#0x00
      00060F F5 45            [12] 1479 	mov	((_main_alpha_65537_42 + 0x0002) + 1),a
      000611 75 46 25         [24] 1480 	mov	((_main_alpha_65537_42 + 0x0004) + 0),#0x25
                                   1481 ;	1-genFromRTrack replaced	mov	((_main_alpha_65537_42 + 0x0004) + 1),#0x00
      000614 F5 47            [12] 1482 	mov	((_main_alpha_65537_42 + 0x0004) + 1),a
      000616 75 48 0D         [24] 1483 	mov	((_main_alpha_65537_42 + 0x0006) + 0),#0x0d
                                   1484 ;	1-genFromRTrack replaced	mov	((_main_alpha_65537_42 + 0x0006) + 1),#0x00
      000619 F5 49            [12] 1485 	mov	((_main_alpha_65537_42 + 0x0006) + 1),a
      00061B 75 4A 99         [24] 1486 	mov	((_main_alpha_65537_42 + 0x0008) + 0),#0x99
                                   1487 ;	1-genFromRTrack replaced	mov	((_main_alpha_65537_42 + 0x0008) + 1),#0x00
      00061E F5 4B            [12] 1488 	mov	((_main_alpha_65537_42 + 0x0008) + 1),a
      000620 75 4C 49         [24] 1489 	mov	((_main_alpha_65537_42 + 0x000a) + 0),#0x49
                                   1490 ;	1-genFromRTrack replaced	mov	((_main_alpha_65537_42 + 0x000a) + 1),#0x00
      000623 F5 4D            [12] 1491 	mov	((_main_alpha_65537_42 + 0x000a) + 1),a
      000625 75 4E 41         [24] 1492 	mov	((_main_alpha_65537_42 + 0x000c) + 0),#0x41
                                   1493 ;	1-genFromRTrack replaced	mov	((_main_alpha_65537_42 + 0x000c) + 1),#0x00
      000628 F5 4F            [12] 1494 	mov	((_main_alpha_65537_42 + 0x000c) + 1),a
      00062A 75 50 1F         [24] 1495 	mov	((_main_alpha_65537_42 + 0x000e) + 0),#0x1f
                                   1496 ;	1-genFromRTrack replaced	mov	((_main_alpha_65537_42 + 0x000e) + 1),#0x00
      00062D F5 51            [12] 1497 	mov	((_main_alpha_65537_42 + 0x000e) + 1),a
      00062F 75 52 01         [24] 1498 	mov	((_main_alpha_65537_42 + 0x0010) + 0),#0x01
                                   1499 ;	1-genFromRTrack replaced	mov	((_main_alpha_65537_42 + 0x0010) + 1),#0x00
      000632 F5 53            [12] 1500 	mov	((_main_alpha_65537_42 + 0x0010) + 1),a
      000634 75 54 09         [24] 1501 	mov	((_main_alpha_65537_42 + 0x0012) + 0),#0x09
                                   1502 ;	1-genFromRTrack replaced	mov	((_main_alpha_65537_42 + 0x0012) + 1),#0x00
      000637 F5 55            [12] 1503 	mov	((_main_alpha_65537_42 + 0x0012) + 1),a
      000639 75 56 FF         [24] 1504 	mov	((_main_alpha_65537_42 + 0x0014) + 0),#0xff
                                   1505 ;	1-genFromRTrack replaced	mov	((_main_alpha_65537_42 + 0x0014) + 1),#0x00
      00063C F5 57            [12] 1506 	mov	((_main_alpha_65537_42 + 0x0014) + 1),a
                                   1507 ;	main.c:157: P0 = 0b00001111;
      00063E 75 80 0F         [24] 1508 	mov	_P0,#0x0f
                                   1509 ;	main.c:158: short index = 0;
      000641 F5 58            [12] 1510 	mov	_main_index_65538_43,a
      000643 F5 59            [12] 1511 	mov	(_main_index_65538_43 + 1),a
                                   1512 ;	main.c:159: long flash_flag = 0;
      000645 F5 5A            [12] 1513 	mov	_main_flash_flag_65538_43,a
      000647 F5 5B            [12] 1514 	mov	(_main_flash_flag_65538_43 + 1),a
      000649 F5 5C            [12] 1515 	mov	(_main_flash_flag_65538_43 + 2),a
      00064B F5 5D            [12] 1516 	mov	(_main_flash_flag_65538_43 + 3),a
                                   1517 ;	main.c:160: bool isSetting = false;
      00064D 7D 00            [12] 1518 	mov	r5,#0x00
                                   1519 ;	main.c:162: bool setting_bi_time = false;
      00064F 7C 00            [12] 1520 	mov	r4,#0x00
                                   1521 ;	main.c:163: while (1) {
      000651                       1522 00145$:
                                   1523 ;	main.c:164: flash_flag++;
      000651 05 5A            [12] 1524 	inc	_main_flash_flag_65538_43
      000653 E4               [12] 1525 	clr	a
      000654 B5 5A 0C         [24] 1526 	cjne	a,_main_flash_flag_65538_43,00241$
      000657 05 5B            [12] 1527 	inc	(_main_flash_flag_65538_43 + 1)
      000659 B5 5B 07         [24] 1528 	cjne	a,(_main_flash_flag_65538_43 + 1),00241$
      00065C 05 5C            [12] 1529 	inc	(_main_flash_flag_65538_43 + 2)
      00065E B5 5C 02         [24] 1530 	cjne	a,(_main_flash_flag_65538_43 + 2),00241$
      000661 05 5D            [12] 1531 	inc	(_main_flash_flag_65538_43 + 3)
      000663                       1532 00241$:
                                   1533 ;	main.c:165: if (flash_flag >= 8000)  // 頻率
      000663 C3               [12] 1534 	clr	c
      000664 E5 5A            [12] 1535 	mov	a,_main_flash_flag_65538_43
      000666 94 40            [12] 1536 	subb	a,#0x40
      000668 E5 5B            [12] 1537 	mov	a,(_main_flash_flag_65538_43 + 1)
      00066A 94 1F            [12] 1538 	subb	a,#0x1f
      00066C E5 5C            [12] 1539 	mov	a,(_main_flash_flag_65538_43 + 2)
      00066E 94 00            [12] 1540 	subb	a,#0x00
      000670 E5 5D            [12] 1541 	mov	a,(_main_flash_flag_65538_43 + 3)
      000672 64 80            [12] 1542 	xrl	a,#0x80
      000674 94 80            [12] 1543 	subb	a,#0x80
      000676 40 09            [24] 1544 	jc	00102$
                                   1545 ;	main.c:166: flash_flag = 0;
      000678 E4               [12] 1546 	clr	a
      000679 F5 5A            [12] 1547 	mov	_main_flash_flag_65538_43,a
      00067B F5 5B            [12] 1548 	mov	(_main_flash_flag_65538_43 + 1),a
      00067D F5 5C            [12] 1549 	mov	(_main_flash_flag_65538_43 + 2),a
      00067F F5 5D            [12] 1550 	mov	(_main_flash_flag_65538_43 + 3),a
      000681                       1551 00102$:
                                   1552 ;	main.c:167: P0     =count^0b11111111;
      000681 74 FF            [12] 1553 	mov	a,#0xff
      000683 65 30            [12] 1554 	xrl	a,_main_count_65537_42
      000685 FA               [12] 1555 	mov	r2,a
      000686 8A 80            [24] 1556 	mov	_P0,r2
                                   1557 ;	main.c:168: count *=2; //shift
      000688 E5 30            [12] 1558 	mov	a,_main_count_65537_42
      00068A 25 30            [12] 1559 	add	a,_main_count_65537_42
      00068C F5 30            [12] 1560 	mov	_main_count_65537_42,a
      00068E E5 31            [12] 1561 	mov	a,(_main_count_65537_42 + 1)
      000690 33               [12] 1562 	rlc	a
      000691 F5 31            [12] 1563 	mov	(_main_count_65537_42 + 1),a
                                   1564 ;	main.c:169: short key = keyPressed(row);
      000693 85 2E 82         [24] 1565 	mov	dpl,_main_row_65537_42
      000696 85 2F 83         [24] 1566 	mov	dph,(_main_row_65537_42 + 1)
      000699 C0 05            [24] 1567 	push	ar5
      00069B C0 04            [24] 1568 	push	ar4
      00069D 12 02 74         [24] 1569 	lcall	_keyPressed
      0006A0 AA 82            [24] 1570 	mov	r2,dpl
      0006A2 AB 83            [24] 1571 	mov	r3,dph
      0006A4 D0 04            [24] 1572 	pop	ar4
      0006A6 D0 05            [24] 1573 	pop	ar5
                                   1574 ;	main.c:170: if (key != previous && key != -1) {	//有按且不等於上一按 => 處理debounce
      0006A8 EA               [12] 1575 	mov	a,r2
      0006A9 B5 2C 07         [24] 1576 	cjne	a,_main_previous_65537_42,00243$
      0006AC EB               [12] 1577 	mov	a,r3
      0006AD B5 2D 03         [24] 1578 	cjne	a,(_main_previous_65537_42 + 1),00243$
      0006B0 02 07 80         [24] 1579 	ljmp	00130$
      0006B3                       1580 00243$:
      0006B3 BA FF 06         [24] 1581 	cjne	r2,#0xff,00244$
      0006B6 BB FF 03         [24] 1582 	cjne	r3,#0xff,00244$
      0006B9 02 07 80         [24] 1583 	ljmp	00130$
      0006BC                       1584 00244$:
                                   1585 ;	main.c:171: previous = key;
      0006BC 8A 2C            [24] 1586 	mov	_main_previous_65537_42,r2
      0006BE 8B 2D            [24] 1587 	mov	(_main_previous_65537_42 + 1),r3
                                   1588 ;	main.c:173: if (key == 10) {
      0006C0 BA 0A 0A         [24] 1589 	cjne	r2,#0x0a,00104$
      0006C3 BB 00 07         [24] 1590 	cjne	r3,#0x00,00104$
                                   1591 ;	main.c:174: index = 0;
      0006C6 E4               [12] 1592 	clr	a
      0006C7 F5 58            [12] 1593 	mov	_main_index_65538_43,a
      0006C9 F5 59            [12] 1594 	mov	(_main_index_65538_43 + 1),a
                                   1595 ;	main.c:175: isSetting = true;
      0006CB 7D 01            [12] 1596 	mov	r5,#0x01
      0006CD                       1597 00104$:
                                   1598 ;	main.c:177: if (key == 11) isSetting = false;
      0006CD BA 0B 05         [24] 1599 	cjne	r2,#0x0b,00106$
      0006D0 BB 00 02         [24] 1600 	cjne	r3,#0x00,00106$
      0006D3 7D 00            [12] 1601 	mov	r5,#0x00
      0006D5                       1602 00106$:
                                   1603 ;	main.c:178: if (key == 12) {
      0006D5 BA 0C 0A         [24] 1604 	cjne	r2,#0x0c,00108$
      0006D8 BB 00 07         [24] 1605 	cjne	r3,#0x00,00108$
                                   1606 ;	main.c:179: index = 0;
      0006DB E4               [12] 1607 	clr	a
      0006DC F5 58            [12] 1608 	mov	_main_index_65538_43,a
      0006DE F5 59            [12] 1609 	mov	(_main_index_65538_43 + 1),a
                                   1610 ;	main.c:180: setting_bi_time = true;
      0006E0 7C 01            [12] 1611 	mov	r4,#0x01
      0006E2                       1612 00108$:
                                   1613 ;	main.c:182: if (key == 13) setting_bi_time = false;
      0006E2 BA 0D 05         [24] 1614 	cjne	r2,#0x0d,00110$
      0006E5 BB 00 02         [24] 1615 	cjne	r3,#0x00,00110$
      0006E8 7C 00            [12] 1616 	mov	r4,#0x00
      0006EA                       1617 00110$:
                                   1618 ;	main.c:183: if (key == 14) TR1 = 0;
      0006EA BA 0E 05         [24] 1619 	cjne	r2,#0x0e,00112$
      0006ED BB 00 02         [24] 1620 	cjne	r3,#0x00,00112$
                                   1621 ;	assignBit
      0006F0 C2 8E            [12] 1622 	clr	_TR1
      0006F2                       1623 00112$:
                                   1624 ;	main.c:184: if (key == 15) TR1 = 1;
      0006F2 BA 0F 05         [24] 1625 	cjne	r2,#0x0f,00114$
      0006F5 BB 00 02         [24] 1626 	cjne	r3,#0x00,00114$
                                   1627 ;	assignBit
      0006F8 D2 8E            [12] 1628 	setb	_TR1
      0006FA                       1629 00114$:
                                   1630 ;	main.c:187: if (isSetting) {
      0006FA ED               [12] 1631 	mov	a,r5
      0006FB 60 40            [24] 1632 	jz	00121$
                                   1633 ;	main.c:189: if (key >= 0 && key <= 9)
      0006FD EB               [12] 1634 	mov	a,r3
      0006FE 20 E7 2A         [24] 1635 	jb	acc.7,00116$
      000701 C3               [12] 1636 	clr	c
      000702 74 09            [12] 1637 	mov	a,#0x09
      000704 9A               [12] 1638 	subb	a,r2
      000705 74 80            [12] 1639 	mov	a,#(0x00 ^ 0x80)
      000707 8B F0            [24] 1640 	mov	b,r3
      000709 63 F0 80         [24] 1641 	xrl	b,#0x80
      00070C 95 F0            [12] 1642 	subb	a,b
      00070E 40 1B            [24] 1643 	jc	00116$
                                   1644 ;	main.c:190: num[index++] = key;
      000710 AE 58            [24] 1645 	mov	r6,_main_index_65538_43
      000712 AF 59            [24] 1646 	mov	r7,(_main_index_65538_43 + 1)
      000714 05 58            [12] 1647 	inc	_main_index_65538_43
      000716 E4               [12] 1648 	clr	a
      000717 B5 58 02         [24] 1649 	cjne	a,_main_index_65538_43,00260$
      00071A 05 59            [12] 1650 	inc	(_main_index_65538_43 + 1)
      00071C                       1651 00260$:
      00071C EE               [12] 1652 	mov	a,r6
      00071D 2E               [12] 1653 	add	a,r6
      00071E FE               [12] 1654 	mov	r6,a
      00071F EF               [12] 1655 	mov	a,r7
      000720 33               [12] 1656 	rlc	a
      000721 FF               [12] 1657 	mov	r7,a
      000722 EE               [12] 1658 	mov	a,r6
      000723 24 32            [12] 1659 	add	a,#_main_num_65537_42
      000725 F8               [12] 1660 	mov	r0,a
      000726 A6 02            [24] 1661 	mov	@r0,ar2
      000728 08               [12] 1662 	inc	r0
      000729 A6 03            [24] 1663 	mov	@r0,ar3
      00072B                       1664 00116$:
                                   1665 ;	main.c:191: if (index == 4) index = 0;
      00072B 74 04            [12] 1666 	mov	a,#0x04
      00072D B5 58 06         [24] 1667 	cjne	a,_main_index_65538_43,00261$
      000730 E4               [12] 1668 	clr	a
      000731 B5 59 02         [24] 1669 	cjne	a,(_main_index_65538_43 + 1),00261$
      000734 80 02            [24] 1670 	sjmp	00262$
      000736                       1671 00261$:
      000736 80 05            [24] 1672 	sjmp	00121$
      000738                       1673 00262$:
      000738 E4               [12] 1674 	clr	a
      000739 F5 58            [12] 1675 	mov	_main_index_65538_43,a
      00073B F5 59            [12] 1676 	mov	(_main_index_65538_43 + 1),a
      00073D                       1677 00121$:
                                   1678 ;	main.c:194: if (setting_bi_time) {
      00073D EC               [12] 1679 	mov	a,r4
      00073E 60 40            [24] 1680 	jz	00130$
                                   1681 ;	main.c:195: if (key >= 0 && key <= 9)
      000740 EB               [12] 1682 	mov	a,r3
      000741 20 E7 2A         [24] 1683 	jb	acc.7,00123$
      000744 C3               [12] 1684 	clr	c
      000745 74 09            [12] 1685 	mov	a,#0x09
      000747 9A               [12] 1686 	subb	a,r2
      000748 74 80            [12] 1687 	mov	a,#(0x00 ^ 0x80)
      00074A 8B F0            [24] 1688 	mov	b,r3
      00074C 63 F0 80         [24] 1689 	xrl	b,#0x80
      00074F 95 F0            [12] 1690 	subb	a,b
      000751 40 1B            [24] 1691 	jc	00123$
                                   1692 ;	main.c:196: num_bi[index++] = key;
      000753 AE 58            [24] 1693 	mov	r6,_main_index_65538_43
      000755 AF 59            [24] 1694 	mov	r7,(_main_index_65538_43 + 1)
      000757 05 58            [12] 1695 	inc	_main_index_65538_43
      000759 E4               [12] 1696 	clr	a
      00075A B5 58 02         [24] 1697 	cjne	a,_main_index_65538_43,00266$
      00075D 05 59            [12] 1698 	inc	(_main_index_65538_43 + 1)
      00075F                       1699 00266$:
      00075F EE               [12] 1700 	mov	a,r6
      000760 2E               [12] 1701 	add	a,r6
      000761 FE               [12] 1702 	mov	r6,a
      000762 EF               [12] 1703 	mov	a,r7
      000763 33               [12] 1704 	rlc	a
      000764 FF               [12] 1705 	mov	r7,a
      000765 EE               [12] 1706 	mov	a,r6
      000766 24 3A            [12] 1707 	add	a,#_main_num_bi_65537_42
      000768 F8               [12] 1708 	mov	r0,a
      000769 A6 02            [24] 1709 	mov	@r0,ar2
      00076B 08               [12] 1710 	inc	r0
      00076C A6 03            [24] 1711 	mov	@r0,ar3
      00076E                       1712 00123$:
                                   1713 ;	main.c:197: if (index == 4) index = 0;
      00076E 74 04            [12] 1714 	mov	a,#0x04
      000770 B5 58 06         [24] 1715 	cjne	a,_main_index_65538_43,00267$
      000773 E4               [12] 1716 	clr	a
      000774 B5 59 02         [24] 1717 	cjne	a,(_main_index_65538_43 + 1),00267$
      000777 80 02            [24] 1718 	sjmp	00268$
      000779                       1719 00267$:
      000779 80 05            [24] 1720 	sjmp	00130$
      00077B                       1721 00268$:
      00077B E4               [12] 1722 	clr	a
      00077C F5 58            [12] 1723 	mov	_main_index_65538_43,a
      00077E F5 59            [12] 1724 	mov	(_main_index_65538_43 + 1),a
      000780                       1725 00130$:
                                   1726 ;	main.c:201: if (!isSetting && !setting_bi_time) {
      000780 ED               [12] 1727 	mov	a,r5
      000781 70 14            [24] 1728 	jnz	00133$
      000783 EC               [12] 1729 	mov	a,r4
      000784 70 11            [24] 1730 	jnz	00133$
                                   1731 ;	main.c:202: run_clock(num);
      000786 90 00 32         [24] 1732 	mov	dptr,#_main_num_65537_42
      000789 75 F0 40         [24] 1733 	mov	b,#0x40
      00078C C0 05            [24] 1734 	push	ar5
      00078E C0 04            [24] 1735 	push	ar4
      000790 12 00 B4         [24] 1736 	lcall	_run_clock
      000793 D0 04            [24] 1737 	pop	ar4
      000795 D0 05            [24] 1738 	pop	ar5
      000797                       1739 00133$:
                                   1740 ;	main.c:204: row++;
      000797 05 2E            [12] 1741 	inc	_main_row_65537_42
      000799 E4               [12] 1742 	clr	a
      00079A B5 2E 02         [24] 1743 	cjne	a,_main_row_65537_42,00271$
      00079D 05 2F            [12] 1744 	inc	(_main_row_65537_42 + 1)
      00079F                       1745 00271$:
                                   1746 ;	main.c:205: if (count == 0x10) {	//用count從上往下掃 
      00079F 74 10            [12] 1747 	mov	a,#0x10
      0007A1 B5 30 06         [24] 1748 	cjne	a,_main_count_65537_42,00272$
      0007A4 E4               [12] 1749 	clr	a
      0007A5 B5 31 02         [24] 1750 	cjne	a,(_main_count_65537_42 + 1),00272$
      0007A8 80 02            [24] 1751 	sjmp	00273$
      0007AA                       1752 00272$:
      0007AA 80 0A            [24] 1753 	sjmp	00136$
      0007AC                       1754 00273$:
                                   1755 ;	main.c:206: count = 1;
      0007AC 75 30 01         [24] 1756 	mov	_main_count_65537_42,#0x01
                                   1757 ;	main.c:207: row   = 0;
      0007AF E4               [12] 1758 	clr	a
      0007B0 F5 31            [12] 1759 	mov	(_main_count_65537_42 + 1),a
      0007B2 F5 2E            [12] 1760 	mov	_main_row_65537_42,a
      0007B4 F5 2F            [12] 1761 	mov	(_main_row_65537_42 + 1),a
      0007B6                       1762 00136$:
                                   1763 ;	main.c:210: P1_0 = 1;
                                   1764 ;	assignBit
      0007B6 D2 90            [12] 1765 	setb	_P1_0
                                   1766 ;	main.c:211: P1_1 = 1;
                                   1767 ;	assignBit
      0007B8 D2 91            [12] 1768 	setb	_P1_1
                                   1769 ;	main.c:212: P1_2 = 1;
                                   1770 ;	assignBit
      0007BA D2 92            [12] 1771 	setb	_P1_2
                                   1772 ;	main.c:213: P1_3 = 1;
                                   1773 ;	assignBit
      0007BC D2 93            [12] 1774 	setb	_P1_3
                                   1775 ;	main.c:215: if (setting_bi_time || isSetting)
      0007BE EC               [12] 1776 	mov	a,r4
      0007BF 70 03            [24] 1777 	jnz	00140$
      0007C1 ED               [12] 1778 	mov	a,r5
      0007C2 60 59            [24] 1779 	jz	00141$
      0007C4                       1780 00140$:
                                   1781 ;	main.c:216: if (isSetting)
      0007C4 ED               [12] 1782 	mov	a,r5
      0007C5 60 2B            [24] 1783 	jz	00138$
                                   1784 ;	main.c:217: display(alpha, num, 1, flash_flag);
      0007C7 75 5E 32         [24] 1785 	mov	_display_PARM_2,#_main_num_65537_42
      0007CA 75 5F 00         [24] 1786 	mov	(_display_PARM_2 + 1),#0x00
      0007CD 75 60 40         [24] 1787 	mov	(_display_PARM_2 + 2),#0x40
      0007D0 75 61 01         [24] 1788 	mov	_display_PARM_3,#0x01
      0007D3 85 5A 62         [24] 1789 	mov	_display_PARM_4,_main_flash_flag_65538_43
      0007D6 85 5B 63         [24] 1790 	mov	(_display_PARM_4 + 1),(_main_flash_flag_65538_43 + 1)
      0007D9 85 5C 64         [24] 1791 	mov	(_display_PARM_4 + 2),(_main_flash_flag_65538_43 + 2)
      0007DC 85 5D 65         [24] 1792 	mov	(_display_PARM_4 + 3),(_main_flash_flag_65538_43 + 3)
      0007DF 90 00 42         [24] 1793 	mov	dptr,#_main_alpha_65537_42
      0007E2 75 F0 40         [24] 1794 	mov	b,#0x40
      0007E5 C0 05            [24] 1795 	push	ar5
      0007E7 C0 04            [24] 1796 	push	ar4
      0007E9 12 02 E3         [24] 1797 	lcall	_display
      0007EC D0 04            [24] 1798 	pop	ar4
      0007EE D0 05            [24] 1799 	pop	ar5
      0007F0 80 54            [24] 1800 	sjmp	00142$
      0007F2                       1801 00138$:
                                   1802 ;	main.c:219: display(alpha, num_bi, 1, flash_flag);
      0007F2 75 5E 3A         [24] 1803 	mov	_display_PARM_2,#_main_num_bi_65537_42
      0007F5 75 5F 00         [24] 1804 	mov	(_display_PARM_2 + 1),#0x00
      0007F8 75 60 40         [24] 1805 	mov	(_display_PARM_2 + 2),#0x40
      0007FB 75 61 01         [24] 1806 	mov	_display_PARM_3,#0x01
      0007FE 85 5A 62         [24] 1807 	mov	_display_PARM_4,_main_flash_flag_65538_43
      000801 85 5B 63         [24] 1808 	mov	(_display_PARM_4 + 1),(_main_flash_flag_65538_43 + 1)
      000804 85 5C 64         [24] 1809 	mov	(_display_PARM_4 + 2),(_main_flash_flag_65538_43 + 2)
      000807 85 5D 65         [24] 1810 	mov	(_display_PARM_4 + 3),(_main_flash_flag_65538_43 + 3)
      00080A 90 00 42         [24] 1811 	mov	dptr,#_main_alpha_65537_42
      00080D 75 F0 40         [24] 1812 	mov	b,#0x40
      000810 C0 05            [24] 1813 	push	ar5
      000812 C0 04            [24] 1814 	push	ar4
      000814 12 02 E3         [24] 1815 	lcall	_display
      000817 D0 04            [24] 1816 	pop	ar4
      000819 D0 05            [24] 1817 	pop	ar5
      00081B 80 29            [24] 1818 	sjmp	00142$
      00081D                       1819 00141$:
                                   1820 ;	main.c:221: display(alpha, num, 0, flash_flag);
      00081D 75 5E 32         [24] 1821 	mov	_display_PARM_2,#_main_num_65537_42
      000820 75 5F 00         [24] 1822 	mov	(_display_PARM_2 + 1),#0x00
      000823 75 60 40         [24] 1823 	mov	(_display_PARM_2 + 2),#0x40
      000826 75 61 00         [24] 1824 	mov	_display_PARM_3,#0x00
      000829 85 5A 62         [24] 1825 	mov	_display_PARM_4,_main_flash_flag_65538_43
      00082C 85 5B 63         [24] 1826 	mov	(_display_PARM_4 + 1),(_main_flash_flag_65538_43 + 1)
      00082F 85 5C 64         [24] 1827 	mov	(_display_PARM_4 + 2),(_main_flash_flag_65538_43 + 2)
      000832 85 5D 65         [24] 1828 	mov	(_display_PARM_4 + 3),(_main_flash_flag_65538_43 + 3)
      000835 90 00 42         [24] 1829 	mov	dptr,#_main_alpha_65537_42
      000838 75 F0 40         [24] 1830 	mov	b,#0x40
      00083B C0 05            [24] 1831 	push	ar5
      00083D C0 04            [24] 1832 	push	ar4
      00083F 12 02 E3         [24] 1833 	lcall	_display
      000842 D0 04            [24] 1834 	pop	ar4
      000844 D0 05            [24] 1835 	pop	ar5
      000846                       1836 00142$:
                                   1837 ;	main.c:222: check_sound_trigger(num, num_bi);
      000846 75 5E 3A         [24] 1838 	mov	_check_sound_trigger_PARM_2,#_main_num_bi_65537_42
      000849 75 5F 00         [24] 1839 	mov	(_check_sound_trigger_PARM_2 + 1),#0x00
      00084C 75 60 40         [24] 1840 	mov	(_check_sound_trigger_PARM_2 + 2),#0x40
      00084F 90 00 32         [24] 1841 	mov	dptr,#_main_num_65537_42
      000852 75 F0 40         [24] 1842 	mov	b,#0x40
      000855 C0 05            [24] 1843 	push	ar5
      000857 C0 04            [24] 1844 	push	ar4
      000859 12 04 91         [24] 1845 	lcall	_check_sound_trigger
      00085C D0 04            [24] 1846 	pop	ar4
      00085E D0 05            [24] 1847 	pop	ar5
                                   1848 ;	main.c:224: }
      000860 02 06 51         [24] 1849 	ljmp	00145$
                                   1850 	.area CSEG    (CODE)
                                   1851 	.area CONST   (CODE)
      000BD2                       1852 _table_LED:
      000BD2 01 00                 1853 	.byte #0x01, #0x00	;  1
      000BD4 01 00                 1854 	.byte #0x01, #0x00	;  1
      000BD6 01 00                 1855 	.byte #0x01, #0x00	;  1
      000BD8 00 00                 1856 	.byte #0x00, #0x00	;  0
      000BDA 01 00                 1857 	.byte #0x01, #0x00	;  1
      000BDC 01 00                 1858 	.byte #0x01, #0x00	;  1
      000BDE 00 00                 1859 	.byte #0x00, #0x00	;  0
      000BE0 01 00                 1860 	.byte #0x01, #0x00	;  1
      000BE2 01 00                 1861 	.byte #0x01, #0x00	;  1
      000BE4 00 00                 1862 	.byte #0x00, #0x00	;  0
      000BE6 01 00                 1863 	.byte #0x01, #0x00	;  1
      000BE8 01 00                 1864 	.byte #0x01, #0x00	;  1
      000BEA 00 00                 1865 	.byte #0x00, #0x00	;  0
      000BEC 01 00                 1866 	.byte #0x01, #0x00	;  1
      000BEE 01 00                 1867 	.byte #0x01, #0x00	;  1
      000BF0 01 00                 1868 	.byte #0x01, #0x00	;  1
      000BF2                       1869 _music:
      000BF2 01 00                 1870 	.byte #0x01, #0x00	;  1
      000BF4 01 00                 1871 	.byte #0x01, #0x00	;  1
      000BF6 05 00                 1872 	.byte #0x05, #0x00	;  5
      000BF8 05 00                 1873 	.byte #0x05, #0x00	;  5
      000BFA 06 00                 1874 	.byte #0x06, #0x00	;  6
      000BFC 06 00                 1875 	.byte #0x06, #0x00	;  6
      000BFE 05 00                 1876 	.byte #0x05, #0x00	;  5
      000C00 04 00                 1877 	.byte #0x04, #0x00	;  4
      000C02 04 00                 1878 	.byte #0x04, #0x00	;  4
      000C04 03 00                 1879 	.byte #0x03, #0x00	;  3
      000C06 03 00                 1880 	.byte #0x03, #0x00	;  3
      000C08 02 00                 1881 	.byte #0x02, #0x00	;  2
      000C0A 02 00                 1882 	.byte #0x02, #0x00	;  2
      000C0C 01 00                 1883 	.byte #0x01, #0x00	;  1
      000C0E 05 00                 1884 	.byte #0x05, #0x00	;  5
      000C10 05 00                 1885 	.byte #0x05, #0x00	;  5
      000C12 04 00                 1886 	.byte #0x04, #0x00	;  4
      000C14 04 00                 1887 	.byte #0x04, #0x00	;  4
      000C16 03 00                 1888 	.byte #0x03, #0x00	;  3
      000C18 03 00                 1889 	.byte #0x03, #0x00	;  3
      000C1A 02 00                 1890 	.byte #0x02, #0x00	;  2
      000C1C 05 00                 1891 	.byte #0x05, #0x00	;  5
      000C1E 05 00                 1892 	.byte #0x05, #0x00	;  5
      000C20 04 00                 1893 	.byte #0x04, #0x00	;  4
      000C22 04 00                 1894 	.byte #0x04, #0x00	;  4
      000C24 03 00                 1895 	.byte #0x03, #0x00	;  3
      000C26 03 00                 1896 	.byte #0x03, #0x00	;  3
      000C28 02 00                 1897 	.byte #0x02, #0x00	;  2
      000C2A 01 00                 1898 	.byte #0x01, #0x00	;  1
      000C2C 01 00                 1899 	.byte #0x01, #0x00	;  1
      000C2E 05 00                 1900 	.byte #0x05, #0x00	;  5
      000C30 05 00                 1901 	.byte #0x05, #0x00	;  5
      000C32 06 00                 1902 	.byte #0x06, #0x00	;  6
      000C34 06 00                 1903 	.byte #0x06, #0x00	;  6
      000C36 05 00                 1904 	.byte #0x05, #0x00	;  5
      000C38 04 00                 1905 	.byte #0x04, #0x00	;  4
      000C3A 04 00                 1906 	.byte #0x04, #0x00	;  4
      000C3C 03 00                 1907 	.byte #0x03, #0x00	;  3
      000C3E 03 00                 1908 	.byte #0x03, #0x00	;  3
      000C40 02 00                 1909 	.byte #0x02, #0x00	;  2
      000C42 02 00                 1910 	.byte #0x02, #0x00	;  2
      000C44 01 00                 1911 	.byte #0x01, #0x00	;  1
                                   1912 	.area XINIT   (CODE)
                                   1913 	.area CABS    (ABS,CODE)
