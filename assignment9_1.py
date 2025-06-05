import threading
import time

def value(numbers):
    for  i in range(1,numbers+1):
    
        print("thread name:",i)

def main():
    start_time=time.time()
    t1=threading.Thread(target=value,args=(5,))        
    t2=threading.Thread(target=value,args=(5,))  
    time.sleep(1)      
    t3=threading.Thread(target=value,args=(5,))        
    time.sleep(1)
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    end_time=time.time()

if __name__=="__main__":
    main()    