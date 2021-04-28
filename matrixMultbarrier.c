#include <stdlib.h>
#include <time.h>
#include <stdio.h>
#include <omp.h>

#define N 3000

void print(int arr[N][N])
{
    int i, j;
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            printf("%d ", arr[i][j]);
}

void multiplyMatrix(int first[N][N], int second[N][N], int mult[N][N])
{

#pragma omp parallel num_threads(10)
    for (int i = 0; i < N; ++i)
    {
        // printf("Thread# %d:", omp_get_num_threads());
        for (int j = 0; j < N; ++j)
        {
            for (int k = 0; k < N; k++)
            {
                mult[i][j] += first[i][k] * second[k][j];
            }
        }
    }
}

int main()
{
    // Declaring the matrices
    static int first[N][N], second[N][N], mult[N][N];

    // Use current time as seed for random generator
    srand(time(0));

    //Filling the two matrices
    for (int i = 0; i < N; ++i)
    {
        for (int j = 0; j < N; ++j)
        {
            first[i][j] = rand() % 100;
            second[i][j] = rand() % 100;
            mult[i][j] = 0;
        }
    }

    // Start measuring time
    struct timespec begin, end;
    clock_gettime(CLOCK_REALTIME, &begin);
    multiplyMatrix(first, second, mult);

    // Stop measuring time and calculate the elapsed time
    clock_gettime(CLOCK_REALTIME, &end);
    long seconds = end.tv_sec - begin.tv_sec;
    long nanoseconds = end.tv_nsec - begin.tv_nsec;
    double elapsed = seconds + nanoseconds * 1e-9;
    
    printf("%lf\n", elapsed); 
    return 0;
}