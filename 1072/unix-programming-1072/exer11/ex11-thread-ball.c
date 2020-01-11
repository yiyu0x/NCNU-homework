#include <stdio.h>
#include <stdlib.h> 
#include <pthread.h>
#include <time.h> 
#define N 49
// unsigned short seed[6] = {0, 1, 2, 3, 4, 5};
void print_array(int *arr) {
	int i;
	for(i = 0; i < N; i++) 
		printf("%2d ", arr[i]);
	printf("\n");
}
void swap(int *a, int *b) { 
    int temp = *a; 
    *a = *b; 
    *b = temp; 
} 

void* ran_array(void* args) {
	int i;
	int* arr = (int*)args;
	int id = arr[N];
	unsigned short seed[] = {id, 34, 56};
	// short seed = arr[N];
	// srand(time(NULL)); 
    for (i = N-1; i > 0; i--) { 
        int j = nrand48(&seed[0]) % (i+1); 
        swap(&arr[i], &arr[j]); 
    }
	return NULL;
}
void init_balls(int* arr, int n) {
	int i;
	unsigned short s[] = {12, 34, 56};
    for (i = n-1; i > 0; i--) { 
        // int j = rand() % (i+1); 
        int j = nrand48(&s[0]) % (i+1);
        swap(&arr[i], &arr[j]); 
    }
}
void printInfo(int *balls) {
	int i, j;
	printf("The ball's initial setting:   %d  %d  %d  %d  %d  %d\n\n", balls[0], 
		 															balls[1],
		 															balls[2],
		 															balls[3],
		 															balls[4],
		 															balls[5]);
	printf("The permuations for balls:\n");
	for (i = 0; i < N; i++) {
		printf("%2d ", i);
	}
	printf("\n");
	for (i = 0; i < N; i++) {
		printf("---");
	}
	printf("\n");
}
int main() {
	// srand(time(NULL)); 
	int i, j;
	int balls[] = {0 ,1, 2, 3, 4, 5};
	init_balls(balls, 6);
	printInfo(balls);

	int perm[6][N+1];// 3-seed
	for (i = 0; i < N; i++) {
		perm[0][i] = i;
		perm[1][i] = i;
		perm[2][i] = i;
		perm[3][i] = i;
		perm[4][i] = i;
		perm[5][i] = i;
	}
	for (i = 0; i < 6; i++)
		perm[i][N] = i;// id

	perm[0][N] = 0;
	pthread_t threads[6]; // 宣告 pthread 變數
	for (i = 0; i < 6; i++)
		pthread_create(threads+i, NULL, ran_array, (void*)perm[i]); // 建立子執行緒
	for (i = 0; i < 6; i++)
		pthread_join(threads[i], NULL); // 等待子執行緒執行完成
	for (i = 0; i < 6; i++) {
		print_array(perm[i]);
	}
	for (i = 0; i < N; i++) {
		printf("---");
	}
	printf("\n");
	// get ans
	for (j = 0; j < 6; j++) {
		int index = perm[0][balls[j]];
		for (i = 1; i < 7; i++) {
			if (i == 6) balls[j] = index;
			index = perm[i][index];
		}
	}

	printf("After permutations applied, balls are:  %2d %2d %2d %2d %2d %2d\n", balls[0],
																				balls[1],
																				balls[2],
																				balls[3],
																				balls[4],
																				balls[5]);
	printf("So the answer is:                       %2d %2d %2d %2d %2d %2d\n", balls[0]+1,
																				balls[1]+1,
																				balls[2]+1,
																				balls[3]+1,
																				balls[4]+1,
																				balls[5]+1);

	// safe-rand
	return 0;
}