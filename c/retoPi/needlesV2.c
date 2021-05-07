#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

void calculatePi(int size){
    srand((unsigned int)time(NULL));
    int acum = 0;    
    for (int i=0;i<size;i++){
        float distx = (float)rand()/RAND_MAX; // x distance
        float rotation = (float)rand()/RAND_MAX;  // angle

        float diff = distx - 0.75 * cosf(rotation);
        if (diff <=0){
            acum +=1;
        }
    }    
    float proportion = (float)acum/ (float)size;
    float calculatedPi = 2 / proportion;
}

double main(int argc, char *argv[])
{
    int size = 100000 ;    
    clock_t start, end;

    start = clock();
    calculatePi(size);
    end = clock();

    double totalTime = (double)(end - start) / CLOCKS_PER_SEC;
    // printf("Valor calculado de pi %f en  %f  s", calculatedPi, totalTime); 
    printf(" %f ", totalTime); 
    return totalTime;
}