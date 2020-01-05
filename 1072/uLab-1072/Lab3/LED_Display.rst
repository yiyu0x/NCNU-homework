                                      1 ;--------------------------------------------------------
                                      2 ; File Created by SDCC : free open source ANSI-C Compiler
                                      3 ; Version 3.8.0 #10562 (MINGW64)
                                      4 ;--------------------------------------------------------
                                      5 	.module LED_Display
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
                                    107 	.globl _num
                                    108 	.globl _table
                                    109 	.globl _LED_Display
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
      000008                        225 _table::
      000008                        226 	.ds 8
      000010                        227 _num::
      000010                        228 	.ds 8
                                    229 ;--------------------------------------------------------
                                    230 ; overlayable items in internal ram 
                                    231 ;--------------------------------------------------------
                                    232 	.area	OSEG    (OVR,DATA)
                                    233 ;--------------------------------------------------------
                                    234 ; indirectly addressable internal ram data
                                    235 ;--------------------------------------------------------
                                    236 	.area ISEG    (DATA)
                                    237 ;--------------------------------------------------------
                                    238 ; absolute internal ram data
                                    239 ;--------------------------------------------------------
                                    240 	.area IABS    (ABS,DATA)
                                    241 	.area IABS    (ABS,DATA)
                                    242 ;--------------------------------------------------------
                                    243 ; bit data
                                    244 ;--------------------------------------------------------
                                    245 	.area BSEG    (BIT)
                                    246 ;--------------------------------------------------------
                                    247 ; paged external ram data
                                    248 ;--------------------------------------------------------
                                    249 	.area PSEG    (PAG,XDATA)
                                    250 ;--------------------------------------------------------
                                    251 ; external ram data
                                    252 ;--------------------------------------------------------
                                    253 	.area XSEG    (XDATA)
                                    254 ;--------------------------------------------------------
                                    255 ; absolute external ram data
                                    256 ;--------------------------------------------------------
                                    257 	.area XABS    (ABS,XDATA)
                                    258 ;--------------------------------------------------------
                                    259 ; external initialized ram data
                                    260 ;--------------------------------------------------------
                                    261 	.area XISEG   (XDATA)
                                    262 	.area HOME    (CODE)
                                    263 	.area GSINIT0 (CODE)
                                    264 	.area GSINIT1 (CODE)
                                    265 	.area GSINIT2 (CODE)
                                    266 	.area GSINIT3 (CODE)
                                    267 	.area GSINIT4 (CODE)
                                    268 	.area GSINIT5 (CODE)
                                    269 	.area GSINIT  (CODE)
                                    270 	.area GSFINAL (CODE)
                                    271 	.area CSEG    (CODE)
                                    272 ;--------------------------------------------------------
                                    273 ; global & static initialisations
                                    274 ;--------------------------------------------------------
                                    275 	.area HOME    (CODE)
                                    276 	.area GSINIT  (CODE)
                                    277 	.area GSFINAL (CODE)
                                    278 	.area GSINIT  (CODE)
                                    279 ;--------------------------------------------------------
                                    280 ; Home
                                    281 ;--------------------------------------------------------
                                    282 	.area HOME    (CODE)
                                    283 	.area HOME    (CODE)
                                    284 ;--------------------------------------------------------
                                    285 ; code
                                    286 ;--------------------------------------------------------
                                    287 	.area CSEG    (CODE)
                                    288 ;------------------------------------------------------------
                                    289 ;Allocation info for local variables in function 'LED_Display'
                                    290 ;------------------------------------------------------------
                                    291 ;i                         Allocated to registers r6 r7 
                                    292 ;j                         Allocated to registers r4 r5 
                                    293 ;------------------------------------------------------------
                                    294 ;	LED_Display.c:4: void LED_Display() {
                                    295 ;	-----------------------------------------
                                    296 ;	 function LED_Display
                                    297 ;	-----------------------------------------
      000000                        298 _LED_Display:
                           000007   299 	ar7 = 0x07
                           000006   300 	ar6 = 0x06
                           000005   301 	ar5 = 0x05
                           000004   302 	ar4 = 0x04
                           000003   303 	ar3 = 0x03
                           000002   304 	ar2 = 0x02
                           000001   305 	ar1 = 0x01
                           000000   306 	ar0 = 0x00
                                    307 ;	LED_Display.c:5: for(short i = 0; i < 4; i++) {
      000000 7E 00            [12]  308 	mov	r6,#0x00
      000002 7F 00            [12]  309 	mov	r7,#0x00
      000004                        310 00107$:
      000004 C3               [12]  311 	clr	c
      000005 EE               [12]  312 	mov	a,r6
      000006 94 04            [12]  313 	subb	a,#0x04
      000008 EF               [12]  314 	mov	a,r7
      000009 64 80            [12]  315 	xrl	a,#0x80
      00000B 94 80            [12]  316 	subb	a,#0x80
      00000D 50 30            [24]  317 	jnc	00109$
                                    318 ;	LED_Display.c:6: P1  = table[i] + num[i];
      00000F EE               [12]  319 	mov	a,r6
      000010 2E               [12]  320 	add	a,r6
      000011 FC               [12]  321 	mov	r4,a
      000012 EF               [12]  322 	mov	a,r7
      000013 33               [12]  323 	rlc	a
      000014 EC               [12]  324 	mov	a,r4
      000015 24 08            [12]  325 	add	a,#_table
      000017 F9               [12]  326 	mov	r1,a
      000018 87 03            [24]  327 	mov	ar3,@r1
      00001A EC               [12]  328 	mov	a,r4
      00001B 24 10            [12]  329 	add	a,#_num
      00001D F9               [12]  330 	mov	r1,a
      00001E E7               [12]  331 	mov	a,@r1
      00001F 2B               [12]  332 	add	a,r3
      000020 F5 90            [12]  333 	mov	_P1,a
                                    334 ;	LED_Display.c:7: for(int j = 0; j < 1000; j++){}
      000022 7C 00            [12]  335 	mov	r4,#0x00
      000024 7D 00            [12]  336 	mov	r5,#0x00
      000026                        337 00104$:
      000026 C3               [12]  338 	clr	c
      000027 EC               [12]  339 	mov	a,r4
      000028 94 E8            [12]  340 	subb	a,#0xe8
      00002A ED               [12]  341 	mov	a,r5
      00002B 64 80            [12]  342 	xrl	a,#0x80
      00002D 94 83            [12]  343 	subb	a,#0x83
      00002F 50 07            [24]  344 	jnc	00108$
      000031 0C               [12]  345 	inc	r4
      000032 BC 00 F1         [24]  346 	cjne	r4,#0x00,00104$
      000035 0D               [12]  347 	inc	r5
      000036 80 EE            [24]  348 	sjmp	00104$
      000038                        349 00108$:
                                    350 ;	LED_Display.c:5: for(short i = 0; i < 4; i++) {
      000038 0E               [12]  351 	inc	r6
      000039 BE 00 C8         [24]  352 	cjne	r6,#0x00,00107$
      00003C 0F               [12]  353 	inc	r7
      00003D 80 C5            [24]  354 	sjmp	00107$
      00003F                        355 00109$:
                                    356 ;	LED_Display.c:9: }
      00003F 22               [24]  357 	ret
                                    358 	.area CSEG    (CODE)
                                    359 	.area CONST   (CODE)
                                    360 	.area XINIT   (CODE)
                                    361 	.area CABS    (ABS,CODE)
