import threading

def numbers(no):
    for i in range(no):
        print(i)

def reverse(numbers):
    for i in range(numbers,0,-1):
        print(i)

def main():
    t1=threading.Thread(target=numbers,args=(50,))
    t2=threading.Thread(target=reverse,args=(50,))

    t1.start()

    t2.start()

    t1.join()
    t2.join()  

if __name__=="__main__":
    main()                  