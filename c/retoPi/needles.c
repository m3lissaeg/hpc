//to run, you must exec gcc needles.c -lm to avoid math lib problems
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{
    srand((unsigned int)time(NULL));
    int size = 100000 ;
    int acum = 0;    

    clock_t start, end;
    start = clock();
    for (int i=0;i<size;i++){
        float distx = (float)rand()/RAND_MAX; // x distance
        float rotation = (float)rand()/RAND_MAX;  // angle

        float diff = distx - 0.75 * cosf(rotation);
        if (diff <=0){
            acum +=1;
        }
        // printf("x = %f ,  angle = %f ", distx, rotation);        
    }    
    float proportion = (float)acum/ (float)size;
    float calculatedPi = 2 / proportion;
    end = clock();

    double totalTime = (double)(end - start) / CLOCKS_PER_SEC;
    // printf("Valor calculado de pi %f en  %f  s", calculatedPi, totalTime); 
    printf("%f ", totalTime); 
    return acum;
}