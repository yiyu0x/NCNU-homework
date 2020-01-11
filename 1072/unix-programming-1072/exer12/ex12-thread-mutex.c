#include <stdio.h>
#include <stdlib.h> 
#include <pthread.h>
#include <time.h> 
#include <signal.h>
#define N 49
int finish;
pthread_mutex_t mutex = PTHREAD_MUTEX_INITIALIZER;
pthread_cond_t flag = PTHREAD_COND_INITIALIZER;
pthread_cond_t ack = PTHREAD_COND_INITIALIZER;

void swap(int *a, int *b) { 
    int temp = *a; 
    *a = *b; 
    *b = temp; 
} 
void* ran_array(void* args) {
    while (1) {
    	pthread_mutex_lock(&mutex);
    	pthread_cond_wait(&flag, &mutex);
    	pthread_mutex_unlock(&mutex);
		int i;
		int* arr = (int*)args;
		int id = arr[N];
		// debug
		// printf("my id is %d!\n", id);
		unsigned short seed[] = {id, 123, 222};
		// short seed = arr[N];
		// srand(time(NULL)); 
	    for (i = N-1; i > 0; i--) { 
	        int j = nrand48(&seed[0]) % (i+1); 
	        swap(&arr[i], &arr[j]); 
	    }
    	pthread_mutex_lock(&mutex);
	    finish++;
	    pthread_cond_signal(&ack);
    	pthread_mutex_unlock(&mutex);
	}
	return NULL;
}

void print_array(int *arr) {
	int i;
	for(i = 0; i < N; i++) 
		printf("%2d ", arr[i]);
	printf("\n");
}

void init_balls(int* arr, int n) {
	int i;
	unsigned short s[] = {12, 34, 56};
    for (i = n-1; i > 0; i--) { 
        int j = nrand48(&s[0]) % (i+1);
        swap(&arr[i], &arr[j]); 
    }
}

int main() {
	int i, j;
	int balls[] = {0 ,1, 2, 3, 4, 5};
	init_balls(balls, 6);

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

//
	if (pthread_mutex_init(&mutex, NULL) != 0) printf("mutex init error\n");
	if (pthread_cond_init(&flag, NULL) != 0) printf("cond init error\n");
	
	for (i = 0; i < 6; i++)
		pthread_create(threads+i, NULL, ran_array, (void*)perm[i]); // 建立子執行緒

	char chr;
	while (1) {
		scanf("%c", &chr);
		if (chr == 'l') {
			finish = 0;
			pthread_mutex_lock(&mutex);
			pthread_cond_broadcast(&flag);
			pthread_mutex_unlock(&mutex);

			for (j = 0; j < 6; j++) {
				int index = perm[0][balls[j]];
				for (i = 1; i < 7; i++) {
					if (i == 6) balls[j] = index;
					index = perm[i][index];
				}
			}
			
			pthread_mutex_lock(&mutex);
			while (finish != 6)
				pthread_cond_wait(&ack, &mutex);
			pthread_mutex_unlock(&mutex);

			printf("the balls are:  %2d %2d %2d %2d %2d %2d\n", balls[0]+1,
																balls[1]+1,
																balls[2]+1,
																balls[3]+1,
																balls[4]+1,
																balls[5]+1);
		} else if (chr == 'q') {
			break;
		}
	}
	return 0;
}