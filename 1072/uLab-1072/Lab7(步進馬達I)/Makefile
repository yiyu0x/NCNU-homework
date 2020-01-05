main.hex: main.ihx
	packihx main.ihx > main.hex
main.rel: main.c
	sdcc -c main.c
main.ihx: main.rel
	sdcc main.c
clean:
	del main.asm main.hex main.ihx main.lk main.lst main.map main.mem main.rel main.sym main.rst