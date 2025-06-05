import threading
def even_factors(n):
    sum=0
    for i in range(2,n):
        if n%i==0:
            sum=sum+i
    print("sum of even factors:",sum)

def odd_factors(n):
    sum=0
    for i in range(1,n):
        if n%i!=0:
            sum=sum+i
    print("sum of odd factors:",sum) 

def main():
    num=int(input("enter a number:"))                          

    t1=threading.Thread(target=even_factors,args=(num,))
    t2=threading.Thread(target=odd_factors,args=(num,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("exit from the main")

if __name__=="__main__":
    main()    



