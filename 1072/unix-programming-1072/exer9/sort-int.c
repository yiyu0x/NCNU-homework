#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>

int cmpfunc(const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}
int four_byteToInt(int fd) {
	char buffer[4];
	read(fd, buffer+3, 1); // big-endian
	read(fd, buffer+2, 1);
	read(fd, buffer+1, 1);
	read(fd, buffer+0, 1);
	int *pInt = (int*)buffer;
	return *pInt;
}
char* intTo_FourBytes(int num) {
	static char bytes[4];
	bytes[0] = (num >> 24) & 0xFF; // big-endian
	bytes[1] = (num >> 16) & 0xFF;
	bytes[2] = (num >>  8) & 0xFF;
	bytes[3] = (num >>  0) & 0xFF;
	return bytes;
}
int main(int argc, char *argv[]) {
	
	int fd_src = open(argv[1], O_RDONLY);
	int size = four_byteToInt(fd_src);
	int array[size];
	for (int i = 0; i < size; i++)
		array[i] = four_byteToInt(fd_src);
	close(fd_src);
	qsort(array, size, sizeof(int), cmpfunc);
	int fd_dst = open(argv[2], O_WRONLY | O_TRUNC | O_CREAT, 0666);
	char *bytes = intTo_FourBytes(size);
	write(fd_dst, bytes, 4);

	for (int i = 0; i < size; i++) {
		char *bytes = intTo_FourBytes(array[i]);
		write(fd_dst, bytes, 4);
	}
	close(fd_dst);
	// char *bytes = intTo_FourBytes(1);
	// write(fd_dst, bytes, 4);
	// qsort(array, size, sizeof(int), cmpfunc);
	
	// for (int i = 0; i < size; i++)
		// printf("%d ", array[i]);

	// read(fd, buffer+0, 1);
	// read(fd, buffer+1, 1);
	// read(fd, buffer+2, 1);
	// read(fd, buffer+3, 1);
	// num = byteToInt(buffer);
	// printf("%d\n", buffer[0]);
	// printf("%d\n", buffer[1]);
	// printf("%d\n", buffer[2]);
	// printf("%d\n", buffer[3]);
	// int* pInt = (int*)buffer;
	// (int*)buffer
	// printf("%d\n", size);
	// printf("%d\n", buffer[1]);

}
	
