#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#include <pthread.h>
#define numOfThreads 25 
#define size 10000000 
int arrayPartialSum[numOfThreads] = {0};
int valueofI = 0;

void * calculatePartialPi( void * arg){
    int * i = (int *) arg;
    srand((unsigned int)time(NULL));
    int partialSize = size/ numOfThreads;
    int acum = 0;    

    for (int j=0;j<partialSize; j++){
        float distx = (float)rand()/RAND_MAX; // x distance
        float rotation = (float)rand()/RAND_MAX;  // angle

        float diff = distx - 0.75 * cosf(rotation);
        if (diff <=0){
            acum +=1;
        }
    }

    arrayPartialSum[valueofI] = acum;    
    printf("%d \n", valueofI);
}

float calculatePI( ){
    
    int arrayPartialSum[numOfThreads] = {0};
    int asserts = 0;

    //Defining Threads
    pthread_t thread[numOfThreads];
            
    for(int i = 0; i < numOfThreads; i++){
        //Create Thread for each partial sum, to calculate Proportion
        int status = pthread_create(&thread[i], NULL, calculatePartialPi, (void *)&i);
        valueofI = i;
        
        //Check For Error
        if(status!=0){
            printf("Error In Threads");
            exit(0);
        }
        pthread_join(thread[i], NULL);
    }

    for(int i = 0; i < numOfThreads; i++){
        asserts += arrayPartialSum[i];
    }   
    

    float proportion = (float)asserts/ (float)size;
    float calculatedPi = 2 / proportion;
    
    return calculatedPi;
}


int main(int argc, char *argv[])
{
    clock_t start, end;

    start = clock();
    double calculatedPi = calculatePI();
    end = clock();

    double totalTime = (double)(end - start) / CLOCKS_PER_SEC;
    printf("Valor calculado de pi %f en  %f  s", calculatedPi, totalTime); 
    printf(" %f ", totalTime); 
    return 0;    
}