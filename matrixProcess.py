import random, time
from resource import getrusage as resource_usage, RUSAGE_SELF
import matplotlib.pyplot as plt
import pandas as pd
from os import fork


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


#Multiply Matrix
def multiplyMatrix(matrix1, matrix2, result):
    start_resources = resource_usage(RUSAGE_SELF)
    #iterate through rows of matrix1
    for i in range(n):
       # iterate through columns of matrix2
       for j in range(n):
           # iterate through rows of matrix2
           for k in range(n):
               result[i][j] += matrix1[i][k] * matrix2[k][j]
    end_resources = resource_usage(RUSAGE_SELF)
    timeCPU = end_resources.ru_utime - start_resources.ru_utime
    # print("Matrix multiplication in {0:.10f} seconds".format(timeCPU))
    return timeCPU

# Average Function
def average(list): 
    return sum(list) / len(list)

def averageTime(list1, list2, list3, list4,list5,list6,list7,list8):
    return [average(list1), average(list2), average(list3),average(list4),average(list5),average(list6),average(list7),average(list8) ]

def makeChart(xAxis,yAxis):
    plt.bar(xAxis,yAxis, width=3)
    plt.plot(xAxis, yAxis, color='red')
    plt.title('Matrix Size Vs Average CPU User time')
    plt.xlabel('Matrix Size (N)')
    plt.ylabel('Time (in s)')
    plt.grid(alpha=.7)
    plt.show()

# Main function:
if __name__ == "__main__":
    # Values for n
    matrixSizeN = [100,120,140,160,180,200,220,240]
    #Serial arrays
    size100 = []
    size120 = []
    size140 = []
    size160 = []
    size180 = []
    size200 = []
    size220 = []
    size240 = []

    for i in range (10):
        for n in matrixSizeN:
            #Execution for serial matrixMult
            matrix1, matrix2, result = createMatrix(n)
            # Create the fork, associated to process ID
            pid = os.fork()
            
            if pid > 0:
               print("PID of Parent process is : ", os.getpid())

            else:
               print("PID of Child process is : ", os.getpid())


            time = multiplyMatrix(matrix1, matrix2, result)

            # print('Multi matrix size: {} . Loop: {} .Time: {}'.format(n,i, concTime))

            if n== 100:
                size100.append(time)
            elif n == 120:
                size120.append(time)
            elif n == 140:
                size140.append(time)
            elif n == 160:
                size160.append(time)
            elif n == 180:
                size180.append(time)
            elif n == 200:
                size200.append(time)
            elif n == 220:
                size220.append(time)
            elif n == 240:
                size240.append(time)
            else: 
                print('Error')

     # xAxis = averageTime    yAxis = matrixSize
    averageSerialTimeList = averageTime(size100, size120, size140, size160, size180,size200,size220,size240)

    
    