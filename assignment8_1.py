import threading

def even(no):
        for i in range(1,no):
            if i%2==0:
                print("even:",i)

def odd(no):
        for a in range(1,no):
           if a%2!=0:
                print("odd:",a)

def main():
    print("inside main")
    t1=threading.Thread(target=even,args=(10,))
    t2=threading.Thread(target=odd,args=(10,))
    print("end of main")

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__=="__main__":
    main()                  


