import multiprocessing
import time
import os

def square(numbers):
    print("pid of square process is",os.getpid())
    result=[]
    for i in range(1,11):
        print(i)
   
def main():
    start_time=time.time()
    data=[1,2,3,4,5,6,7,8,9,10]
    p=multiprocessing.pool()
    result=p.map(square,data)

    p.close()
    p.join()
    print(result)

    end_time=time.time()
    print("execution time is",end_time-start_time)

if __name__=="__main__":
   main()    
