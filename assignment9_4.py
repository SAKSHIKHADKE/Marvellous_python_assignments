
import threading
import time
import multiprocessing

def sum_normal(no):
    sum=0
    for i in range(1,no+1):
        sum=sum+i
    return sum
    
def main():
    start_time1=time.time()
    result=sum_normal()
    print(result)
    end_time1=time.time()
    print("normal function time:",end_time1-start_time1)

    start_time2=time.time()
    thread=threading.Thread(target=sum_normal,args=(10000000))
    thread.start()
    thread.join()
    end_time2=time.time()
    print("threading time:",end_time2-start_time2)

    start_time3=time.time()
    p1=multiprocessing.Process(target=sum_normal,args=(10000000))
   
    p1.start()
    p1.join() 
    end_time3=time.time()
    print("execution time is:",end_time3-start_time3)       

if __name__=="__main__":
    main()       