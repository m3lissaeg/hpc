#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

int calculatePartialPi(int size){
    srand((unsigned int)time(NULL));
    int acum = 0;    
    for (int i=0;i<size;i++){
        float distx = (float)rand()/RAND_MAX; // x distance
        float rotation = (float)rand()/RAND_MAX;  // angle

        float diff = distx - 0.75 * cosf(rotation);
        if (diff <=0){
            acum +=1;
        }
    return acum;
    }    
    return acum;
}

int calculatePI(int size){
    
    int threads = 10; 
    int arrayPartialSum[threads];
    int asserts = 0;

    for(int i = 0; i < threads; i++){
        int partialSize = size/ threads;
        int partialAsserts = calculatePartialPi(partialSize); 
        asserts += partialAsserts;
        arrayPartialSum[i]= partialAsserts;
    }

    float proportion = (float)asserts/ (float)size;
    float calculatedPi = 2 / proportion;
}

int main(int argc, char *argv[])
{
    int size = 10000000 ;    
    clock_t start, end;

    start = clock();
    calculatePI(size);
    end = clock();

    double totalTime = (double)(end - start) / CLOCKS_PER_SEC;
    // printf("Valor calculado de pi %f en  %f  s", calculatedPi, totalTime); 
    printf(" %f ", totalTime); 
    return 0;    
}