Flashing.hex: Flashing.ihx
	packihx Flashing.ihx > Flashing.hex
Flashing.rel: Flashing.c
	sdcc -c Flashing.c
Flashing.ihx: Flashing.rel
	sdcc Flashing.c
clean:
	del Flashing.asm Flashing.hex Flashing.ihx Flashing.lk Flashing.lst Flashing.map Flashing.mem Flashing.rel Flashing.sym Flashing.rst