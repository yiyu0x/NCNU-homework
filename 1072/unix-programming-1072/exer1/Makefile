trans: main.o mylib.o
	gcc -o trans main.o mylib.o
main.o: main.c
	gcc -c main.c -std=c99
mylib.o: mylib.c
	gcc -c mylib.c -std=c99
clean:
	rm *.o trans
