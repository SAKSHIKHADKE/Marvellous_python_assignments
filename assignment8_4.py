import threading
import os

def characters(a):
    count=0
    
    print("thread id of current_thread is",os.getpid())
    print("thread name of current_thread is :",threading.current_thread().name)
    print("small characters :",count)
    a=[]
    for i in a:
         if i.islower():
              count=count+1
    print("small",count)          
    
def capital(a):
    count=0
   
    print("thread id of current_thread is",os.getpid())
    print("thread name of current_thread is :",threading.current_thread().name)
    print("capital characters :",count)
    a=[]
    for i in a:
         if i.isupper():
              count=count+1
    print("small",count)          
    

def digits(a):
    count=0
    
    print("thread id of current_thread is",os.getpid())
    print("thread name of current_thread is :",threading.current_thread().name)
    a=[]
    for i in a:
         if i.isdigit():
              count=count+1
    print("small",count)          
    

def main():
        a=input("enter a string:")

        t1=threading.Thread(target=characters,args=(a,))   
        t2=threading.Thread(target=capital,args=(a,))        
        t3=threading.Thread(target=digits,args=(a,))       

        t1.start()
        t2.start()
        t3.start()

        t1.join()
        t2.join()
        t3.join()

if __name__=="__main__":
     main()        

