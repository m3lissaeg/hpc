#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char *argv[])
{
    srand((unsigned int)time(NULL));
    int size = 100000 ;
    int acum = 0;    

    for (int i=0;i<size;i++){
        float distx = (float)rand()/RAND_MAX; // x distance
        float rotation = (float)rand()/RAND_MAX;  // angle

        float diff = distx - 0.75 * cosf(rotation);
        if (diff <=0){
            acum +=1;
        }
        // printf("x = %f ,  angle = %f ", distx, rotation);        
    }
    // printf("total de aciertos: %d", acum); 
    
    float proportion = (float)acum/ (float)size;
    float calculatedPi = 2 / proportion;
    printf("Valor calculado de pi %f", calculatedPi); 
    return acum;
}