C = sdcc
F = Lab3-main
F2 = LED_Display
F3 = Keypad4x4

$(F).hex : $(F).ihx
	packihx $(F).ihx > $(F).hex
$(F).ihx : $(F).rel myIO.lib
	$(C) -l myIO.lib $(F).rel

myIO.lib : $(F2).rel $(F3).rel
	sdar -rc myIO.lib $(F2).rel $(F3).rel

$(F).rel : $(F).c
	$(C) -c $(F).c
$(F2).rel : $(F2).c $(F2).h
	$(C) -c $(F2).c
$(F3).rel : $(F3).c $(F3).h
	$(C) -c $(F3).c