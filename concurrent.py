from sys import argv
import random, time
from resource import getrusage as resource_usage, RUSAGE_SELF
from threading import Thread
NUM_OF_THREADS = 4
serialTime = []
concTime = []

def multiplyParallelMatrix(start, end):
    # iterate through rows of matrix1 int that were assigned o that thread
    for i in range(start, end):
        # iterate through columns of matrix2
        for j in range(n):
            # iterate through rows of matrix2
            for k in range(n):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

#Create matrix
def createMatrix(n):
    a =[]
    b =[]
    r= []
    matrix1 =[]
    matrix2 =[]
    result = []

    for i in range(n):
        for i in range(n):
            number = random.randrange(10)
            number2 = random.randrange(10)
            a.append(number)
            b.append(number2)
            r.append(0)
        matrix1.append(a)
        matrix2.append(b)
        result.append(r)
        a = []
        b = []
        r = []
    return matrix1, matrix2, result

    
# Average Function
def average(list): 
    return sum(list) / len(list)

def averageTime(list1, list2, list3, list4, list5,list6, list7, list8):
    return [average(list1), average(list2), average(list3), average(list4), average(list5), average(list6), average(list7), average(list8) ]

def threadFunction():
    arrayThreads=[]
    global n
    # Number of threads: 2,3 & 4
    for NUM_OF_THREADS in range(2,5):

        thread_handle = []
        row_range = int(n/NUM_OF_THREADS)
        # Calculating the offset
        offset = n % NUM_OF_THREADS
        # Start time counting

        start_resources = resource_usage(RUSAGE_SELF)
        for j in range(0, NUM_OF_THREADS):

            # If the number if rows can be divided by the number of threads
            if offset == 0:
                t = Thread(target=multiplyParallelMatrix, args=(
                    int((row_range) * j), int((row_range) * (j+1))))
            else:
                # if there are remaining rows
                if j == NUM_OF_THREADS - 1:
                    t = Thread(target=multiplyParallelMatrix, args=(
                        int((row_range) * j), int(((row_range) * (j+1))+offset)))
                else:
                    t = Thread(target=multiplyParallelMatrix, args=(
                        int((row_range) * j), int((row_range) * (j+1))))

            thread_handle.append(t)
            t.start()

        for j in range(0, NUM_OF_THREADS):
            thread_handle[j].join()

        # End time counting

        end_resources = resource_usage(RUSAGE_SELF)
        timeCPU = end_resources.ru_utime - start_resources.ru_utime
        arrayThreads.append(timeCPU)

    return arrayThreads

# Main function:
if __name__ == "__main__":
    # Values for n
    matrixSizeN = [100,120,140,160,180,200,220,240]

    #concurrent arrays
    size100With2Threads = []
    size100With3Threads = []
    size100With4Threads = []

    size120With2Threads = []
    size120With3Threads = []
    size120With4Threads = []
    
    size140With2Threads = []
    size140With3Threads = []
    size140With4Threads = []
    
    size160With2Threads = []
    size160With3Threads = []
    size160With4Threads = []
    
    size180With2Threads = []
    size180With3Threads = []
    size180With4Threads = []
    
    size200With2Threads = []
    size200With3Threads = []
    size200With4Threads = []
    
    size220With2Threads = []
    size220With3Threads = []
    size220With4Threads = []
    
    size240With2Threads = []
    size240With3Threads = []
    size240With4Threads = []

    for i in range (10):
        for n in matrixSizeN:

            #Execution for concurrent matrixMult
            matrix1, matrix2, result = createMatrix(n)
            concTime = threadFunction()

            # print('Multi matrix size: {} . Loop: {} .Time: {}'.format(n,i, concTime))

            if n== 100:
                
                size100With2Threads.append(concTime[0])
                size100With3Threads.append(concTime[1])
                size100With4Threads.append(concTime[2])
            elif n == 120:
                
                size120With2Threads.append(concTime[0])
                size120With3Threads.append(concTime[1])
                size120With4Threads.append(concTime[2])
            elif n == 140:
                
                size140With2Threads.append(concTime[0])
                size140With3Threads.append(concTime[1])
                size140With4Threads.append(concTime[2])
            elif n == 160:
                
                size160With2Threads.append(concTime[0])
                size160With3Threads.append(concTime[1])
                size160With4Threads.append(concTime[2])
            elif n == 180:
                
                size180With2Threads.append(concTime[0])
                size180With3Threads.append(concTime[1])
                size180With4Threads.append(concTime[2])
            elif n == 200:
                
                size200With2Threads.append(concTime[0])
                size200With3Threads.append(concTime[1])
                size200With4Threads.append(concTime[2])
            elif n == 220:
                
                size220With2Threads.append(concTime[0])
                size220With3Threads.append(concTime[1])
                size220With4Threads.append(concTime[2])
            elif n == 240:
                
                size240With2Threads.append(concTime[0])
                size240With3Threads.append(concTime[1])
                size240With4Threads.append(concTime[2])
            else: 
                print('Error')


    averageWith2Threads = averageTime(size100With2Threads, size120With2Threads, size140With2Threads, size160With2Threads,size180With2Threads,size200With2Threads,size220With2Threads,size240With2Threads)
    
    averageWith3Threads = averageTime(size100With3Threads, size120With3Threads, size140With3Threads, size160With3Threads,size180With3Threads,size200With3Threads,size220With3Threads,size240With3Threads)
    
    averageWith4Threads = averageTime(size100With4Threads, size120With4Threads, size140With4Threads, size160With4Threads,size180With4Threads,size200With4Threads,size220With4Threads,size240With4Threads)
    print(averageWith2Threads)
    print(averageWith3Threads)
    print(averageWith4Threads)