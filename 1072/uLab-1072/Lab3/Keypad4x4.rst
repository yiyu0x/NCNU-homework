                                      1 ;--------------------------------------------------------
                                      2 ; File Created by SDCC : free open source ANSI-C Compiler
                                      3 ; Version 3.8.0 #10562 (MINGW64)
                                      4 ;--------------------------------------------------------
                                      5 	.module Keypad4x4
                                      6 	.optsdcc -mmcs51 --model-small
                                      7 	
                                      8 ;--------------------------------------------------------
                                      9 ; Public variables in this module
                                     10 ;--------------------------------------------------------
                                     11 	.globl _CY
                                     12 	.globl _AC
                                     13 	.globl _F0
                                     14 	.globl _RS1
                                     15 	.globl _RS0
                                     16 	.globl _OV
                                     17 	.globl _F1
                                     18 	.globl _P
                                     19 	.globl _PS
                                     20 	.globl _PT1
                                     21 	.globl _PX1
                                     22 	.globl _PT0
                                     23 	.globl _PX0
                                     24 	.globl _RD
                                     25 	.globl _WR
                                     26 	.globl _T1
                                     27 	.globl _T0
                                     28 	.globl _INT1
                                     29 	.globl _INT0
                                     30 	.globl _TXD
                                     31 	.globl _RXD
                                     32 	.globl _P3_7
                                     33 	.globl _P3_6
                                     34 	.globl _P3_5
                                     35 	.globl _P3_4
                                     36 	.globl _P3_3
                                     37 	.globl _P3_2
                                     38 	.globl _P3_1
                                     39 	.globl _P3_0
                                     40 	.globl _EA
                                     41 	.globl _ES
                                     42 	.globl _ET1
                                     43 	.globl _EX1
                                     44 	.globl _ET0
                                     45 	.globl _EX0
                                     46 	.globl _P2_7
                                     47 	.globl _P2_6
                                     48 	.globl _P2_5
                                     49 	.globl _P2_4
                                     50 	.globl _P2_3
                                     51 	.globl _P2_2
                                     52 	.globl _P2_1
                                     53 	.globl _P2_0
                                     54 	.globl _SM0
                                     55 	.globl _SM1
                                     56 	.globl _SM2
                                     57 	.globl _REN
                                     58 	.globl _TB8
                                     59 	.globl _RB8
                                     60 	.globl _TI
                                     61 	.globl _RI
                                     62 	.globl _P1_7
                                     63 	.globl _P1_6
                                     64 	.globl _P1_5
                                     65 	.globl _P1_4
                                     66 	.globl _P1_3
                                     67 	.globl _P1_2
                                     68 	.globl _P1_1
                                     69 	.globl _P1_0
                                     70 	.globl _TF1
                                     71 	.globl _TR1
                                     72 	.globl _TF0
                                     73 	.globl _TR0
                                     74 	.globl _IE1
                                     75 	.globl _IT1
                                     76 	.globl _IE0
                                     77 	.globl _IT0
                                     78 	.globl _P0_7
                                     79 	.globl _P0_6
                                     80 	.globl _P0_5
                                     81 	.globl _P0_4
                                     82 	.globl _P0_3
                                     83 	.globl _P0_2
                                     84 	.globl _P0_1
                                     85 	.globl _P0_0
                                     86 	.globl _B
                                     87 	.globl _ACC
                                     88 	.globl _PSW
                                     89 	.globl _IP
                                     90 	.globl _P3
                                     91 	.globl _IE
                                     92 	.globl _P2
                                     93 	.globl _SBUF
                                     94 	.globl _SCON
                                     95 	.globl _P1
                                     96 	.globl _TH1
                                     97 	.globl _TH0
                                     98 	.globl _TL1
                                     99 	.globl _TL0
                                    100 	.globl _TMOD
                                    101 	.globl _TCON
                                    102 	.globl _PCON
                                    103 	.globl _DPH
                                    104 	.globl _DPL
                                    105 	.globl _SP
                                    106 	.globl _P0
                                    107 	.globl _row
                                    108 	.globl _keyPressed
                                    109 ;--------------------------------------------------------
                                    110 ; special function registers
                                    111 ;--------------------------------------------------------
                                    112 	.area RSEG    (ABS,DATA)
      000000                        113 	.org 0x0000
                           000080   114 _P0	=	0x0080
                           000081   115 _SP	=	0x0081
                           000082   116 _DPL	=	0x0082
                           000083   117 _DPH	=	0x0083
                           000087   118 _PCON	=	0x0087
                           000088   119 _TCON	=	0x0088
                           000089   120 _TMOD	=	0x0089
                           00008A   121 _TL0	=	0x008a
                           00008B   122 _TL1	=	0x008b
                           00008C   123 _TH0	=	0x008c
                           00008D   124 _TH1	=	0x008d
                           000090   125 _P1	=	0x0090
                           000098   126 _SCON	=	0x0098
                           000099   127 _SBUF	=	0x0099
                           0000A0   128 _P2	=	0x00a0
                           0000A8   129 _IE	=	0x00a8
                           0000B0   130 _P3	=	0x00b0
                           0000B8   131 _IP	=	0x00b8
                           0000D0   132 _PSW	=	0x00d0
                           0000E0   133 _ACC	=	0x00e0
                           0000F0   134 _B	=	0x00f0
                                    135 ;--------------------------------------------------------
                                    136 ; special function bits
                                    137 ;--------------------------------------------------------
                                    138 	.area RSEG    (ABS,DATA)
      000000                        139 	.org 0x0000
                           000080   140 _P0_0	=	0x0080
                           000081   141 _P0_1	=	0x0081
                           000082   142 _P0_2	=	0x0082
                           000083   143 _P0_3	=	0x0083
                           000084   144 _P0_4	=	0x0084
                           000085   145 _P0_5	=	0x0085
                           000086   146 _P0_6	=	0x0086
                           000087   147 _P0_7	=	0x0087
                           000088   148 _IT0	=	0x0088
                           000089   149 _IE0	=	0x0089
                           00008A   150 _IT1	=	0x008a
                           00008B   151 _IE1	=	0x008b
                           00008C   152 _TR0	=	0x008c
                           00008D   153 _TF0	=	0x008d
                           00008E   154 _TR1	=	0x008e
                           00008F   155 _TF1	=	0x008f
                           000090   156 _P1_0	=	0x0090
                           000091   157 _P1_1	=	0x0091
                           000092   158 _P1_2	=	0x0092
                           000093   159 _P1_3	=	0x0093
                           000094   160 _P1_4	=	0x0094
                           000095   161 _P1_5	=	0x0095
                           000096   162 _P1_6	=	0x0096
                           000097   163 _P1_7	=	0x0097
                           000098   164 _RI	=	0x0098
                           000099   165 _TI	=	0x0099
                           00009A   166 _RB8	=	0x009a
                           00009B   167 _TB8	=	0x009b
                           00009C   168 _REN	=	0x009c
                           00009D   169 _SM2	=	0x009d
                           00009E   170 _SM1	=	0x009e
                           00009F   171 _SM0	=	0x009f
                           0000A0   172 _P2_0	=	0x00a0
                           0000A1   173 _P2_1	=	0x00a1
                           0000A2   174 _P2_2	=	0x00a2
                           0000A3   175 _P2_3	=	0x00a3
                           0000A4   176 _P2_4	=	0x00a4
                           0000A5   177 _P2_5	=	0x00a5
                           0000A6   178 _P2_6	=	0x00a6
                           0000A7   179 _P2_7	=	0x00a7
                           0000A8   180 _EX0	=	0x00a8
                           0000A9   181 _ET0	=	0x00a9
                           0000AA   182 _EX1	=	0x00aa
                           0000AB   183 _ET1	=	0x00ab
                           0000AC   184 _ES	=	0x00ac
                           0000AF   185 _EA	=	0x00af
                           0000B0   186 _P3_0	=	0x00b0
                           0000B1   187 _P3_1	=	0x00b1
                           0000B2   188 _P3_2	=	0x00b2
                           0000B3   189 _P3_3	=	0x00b3
                           0000B4   190 _P3_4	=	0x00b4
                           0000B5   191 _P3_5	=	0x00b5
                           0000B6   192 _P3_6	=	0x00b6
                           0000B7   193 _P3_7	=	0x00b7
                           0000B0   194 _RXD	=	0x00b0
                           0000B1   195 _TXD	=	0x00b1
                           0000B2   196 _INT0	=	0x00b2
                           0000B3   197 _INT1	=	0x00b3
                           0000B4   198 _T0	=	0x00b4
                           0000B5   199 _T1	=	0x00b5
                           0000B6   200 _WR	=	0x00b6
                           0000B7   201 _RD	=	0x00b7
                           0000B8   202 _PX0	=	0x00b8
                           0000B9   203 _PT0	=	0x00b9
                           0000BA   204 _PX1	=	0x00ba
                           0000BB   205 _PT1	=	0x00bb
                           0000BC   206 _PS	=	0x00bc
                           0000D0   207 _P	=	0x00d0
                           0000D1   208 _F1	=	0x00d1
                           0000D2   209 _OV	=	0x00d2
                           0000D3   210 _RS0	=	0x00d3
                           0000D4   211 _RS1	=	0x00d4
                           0000D5   212 _F0	=	0x00d5
                           0000D6   213 _AC	=	0x00d6
                           0000D7   214 _CY	=	0x00d7
                                    215 ;--------------------------------------------------------
                                    216 ; overlayable register banks
                                    217 ;--------------------------------------------------------
                                    218 	.area REG_BANK_0	(REL,OVR,DATA)
      000000                        219 	.ds 8
                                    220 ;--------------------------------------------------------
                                    221 ; internal ram data
                                    222 ;--------------------------------------------------------
                                    223 	.area DSEG    (DATA)
      000018                        224 _row::
      000018                        225 	.ds 2
                                    226 ;--------------------------------------------------------
                                    227 ; overlayable items in internal ram 
                                    228 ;--------------------------------------------------------
                                    229 	.area	OSEG    (OVR,DATA)
                                    230 ;--------------------------------------------------------
                                    231 ; indirectly addressable internal ram data
                                    232 ;--------------------------------------------------------
                                    233 	.area ISEG    (DATA)
                                    234 ;--------------------------------------------------------
                                    235 ; absolute internal ram data
                                    236 ;--------------------------------------------------------
                                    237 	.area IABS    (ABS,DATA)
                                    238 	.area IABS    (ABS,DATA)
                                    239 ;--------------------------------------------------------
                                    240 ; bit data
                                    241 ;--------------------------------------------------------
                                    242 	.area BSEG    (BIT)
                                    243 ;--------------------------------------------------------
                                    244 ; paged external ram data
                                    245 ;--------------------------------------------------------
                                    246 	.area PSEG    (PAG,XDATA)
                                    247 ;--------------------------------------------------------
                                    248 ; external ram data
                                    249 ;--------------------------------------------------------
                                    250 	.area XSEG    (XDATA)
                                    251 ;--------------------------------------------------------
                                    252 ; absolute external ram data
                                    253 ;--------------------------------------------------------
                                    254 	.area XABS    (ABS,XDATA)
                                    255 ;--------------------------------------------------------
                                    256 ; external initialized ram data
                                    257 ;--------------------------------------------------------
                                    258 	.area XISEG   (XDATA)
                                    259 	.area HOME    (CODE)
                                    260 	.area GSINIT0 (CODE)
                                    261 	.area GSINIT1 (CODE)
                                    262 	.area GSINIT2 (CODE)
                                    263 	.area GSINIT3 (CODE)
                                    264 	.area GSINIT4 (CODE)
                                    265 	.area GSINIT5 (CODE)
                                    266 	.area GSINIT  (CODE)
                                    267 	.area GSFINAL (CODE)
                                    268 	.area CSEG    (CODE)
                                    269 ;--------------------------------------------------------
                                    270 ; global & static initialisations
                                    271 ;--------------------------------------------------------
                                    272 	.area HOME    (CODE)
                                    273 	.area GSINIT  (CODE)
                                    274 	.area GSFINAL (CODE)
                                    275 	.area GSINIT  (CODE)
                                    276 ;--------------------------------------------------------
                                    277 ; Home
                                    278 ;--------------------------------------------------------
                                    279 	.area HOME    (CODE)
                                    280 	.area HOME    (CODE)
                                    281 ;--------------------------------------------------------
                                    282 ; code
                                    283 ;--------------------------------------------------------
                                    284 	.area CSEG    (CODE)
                                    285 ;------------------------------------------------------------
                                    286 ;Allocation info for local variables in function 'keyPressed'
                                    287 ;------------------------------------------------------------
                                    288 ;c                         Allocated to registers r6 r7 
                                    289 ;col                       Allocated to registers r4 r5 
                                    290 ;magic                     Allocated to registers r0 r1 
                                    291 ;------------------------------------------------------------
                                    292 ;	Keypad4x4.c:3: short keyPressed() {
                                    293 ;	-----------------------------------------
                                    294 ;	 function keyPressed
                                    295 ;	-----------------------------------------
      000040                        296 _keyPressed:
                           000007   297 	ar7 = 0x07
                           000006   298 	ar6 = 0x06
                           000005   299 	ar5 = 0x05
                           000004   300 	ar4 = 0x04
                           000003   301 	ar3 = 0x03
                           000002   302 	ar2 = 0x02
                           000001   303 	ar1 = 0x01
                           000000   304 	ar0 = 0x00
                                    305 ;	Keypad4x4.c:4: if((P2 & 0b11110000) != 0b11110000){
      000040 AE A0            [24]  306 	mov	r6,_P2
      000042 53 06 F0         [24]  307 	anl	ar6,#0xf0
      000045 7F 00            [12]  308 	mov	r7,#0x00
      000047 BE F0 05         [24]  309 	cjne	r6,#0xf0,00127$
      00004A BF 00 02         [24]  310 	cjne	r7,#0x00,00127$
      00004D 80 55            [24]  311 	sjmp	00105$
      00004F                        312 00127$:
                                    313 ;	Keypad4x4.c:5: for (short c = 1, col = 0; col < 4; c *= 2, col++) {
      00004F 7E 01            [12]  314 	mov	r6,#0x01
      000051 7F 00            [12]  315 	mov	r7,#0x00
      000053 7C 00            [12]  316 	mov	r4,#0x00
      000055 7D 00            [12]  317 	mov	r5,#0x00
      000057 7A 00            [12]  318 	mov	r2,#0x00
      000059 7B 00            [12]  319 	mov	r3,#0x00
      00005B                        320 00107$:
      00005B C3               [12]  321 	clr	c
      00005C EA               [12]  322 	mov	a,r2
      00005D 94 04            [12]  323 	subb	a,#0x04
      00005F EB               [12]  324 	mov	a,r3
      000060 64 80            [12]  325 	xrl	a,#0x80
      000062 94 80            [12]  326 	subb	a,#0x80
      000064 50 3E            [24]  327 	jnc	00105$
                                    328 ;	Keypad4x4.c:6: `			short magic = ((P2 >> 4) ^ 0b11111111) & 0b00001111;
      000066 E5 A0            [12]  329 	mov	a,_P2
      000068 C4               [12]  330 	swap	a
      000069 54 0F            [12]  331 	anl	a,#0x0f
      00006B F8               [12]  332 	mov	r0,a
      00006C 63 00 FF         [24]  333 	xrl	ar0,#0xff
      00006F 53 00 0F         [24]  334 	anl	ar0,#0x0f
      000072 79 00            [12]  335 	mov	r1,#0x00
                                    336 ;	Keypad4x4.c:7: if (magic == c) {
      000074 E8               [12]  337 	mov	a,r0
      000075 B5 06 1B         [24]  338 	cjne	a,ar6,00108$
      000078 E9               [12]  339 	mov	a,r1
      000079 B5 07 17         [24]  340 	cjne	a,ar7,00108$
                                    341 ;	Keypad4x4.c:8: return col * 4 + row;
      00007C EC               [12]  342 	mov	a,r4
      00007D 2C               [12]  343 	add	a,r4
      00007E F8               [12]  344 	mov	r0,a
      00007F ED               [12]  345 	mov	a,r5
      000080 33               [12]  346 	rlc	a
      000081 F9               [12]  347 	mov	r1,a
      000082 E8               [12]  348 	mov	a,r0
      000083 28               [12]  349 	add	a,r0
      000084 F8               [12]  350 	mov	r0,a
      000085 E9               [12]  351 	mov	a,r1
      000086 33               [12]  352 	rlc	a
      000087 F9               [12]  353 	mov	r1,a
      000088 E5 18            [12]  354 	mov	a,_row
      00008A 28               [12]  355 	add	a,r0
      00008B F5 82            [12]  356 	mov	dpl,a
      00008D E5 19            [12]  357 	mov	a,(_row + 1)
      00008F 39               [12]  358 	addc	a,r1
      000090 F5 83            [12]  359 	mov	dph,a
      000092 22               [24]  360 	ret
      000093                        361 00108$:
                                    362 ;	Keypad4x4.c:5: for (short c = 1, col = 0; col < 4; c *= 2, col++) {
      000093 EE               [12]  363 	mov	a,r6
      000094 2E               [12]  364 	add	a,r6
      000095 FE               [12]  365 	mov	r6,a
      000096 EF               [12]  366 	mov	a,r7
      000097 33               [12]  367 	rlc	a
      000098 FF               [12]  368 	mov	r7,a
      000099 0A               [12]  369 	inc	r2
      00009A BA 00 01         [24]  370 	cjne	r2,#0x00,00131$
      00009D 0B               [12]  371 	inc	r3
      00009E                        372 00131$:
      00009E 8A 04            [24]  373 	mov	ar4,r2
      0000A0 8B 05            [24]  374 	mov	ar5,r3
      0000A2 80 B7            [24]  375 	sjmp	00107$
      0000A4                        376 00105$:
                                    377 ;	Keypad4x4.c:12: return -1;
      0000A4 90 FF FF         [24]  378 	mov	dptr,#0xffff
                                    379 ;	Keypad4x4.c:13: }
      0000A7 22               [24]  380 	ret
                                    381 	.area CSEG    (CODE)
                                    382 	.area CONST   (CODE)
                                    383 	.area XINIT   (CODE)
                                    384 	.area CABS    (ABS,CODE)
