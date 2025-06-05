import threading
def even(no):
    j=[]
    sum=0
    for i in no:
        if i%2==0:
            sum=sum+i
            j.append(i)
    print(j)
    print("addition of even numbers:",sum)

def odd(no):
    i=[]
    sum=0
    for a in no:
        if a%2!=0:
            sum=sum+a
            i.append(a)
    print(i)

    print("addition of odd numbers:",sum)

def main():
    number=[]
    a=int(input("enter a list of numbers:"))
    for i in range(a):
        b=int(input("enter number you want:"))
        number.append(b)
    t1=threading.Thread(target=even,args=(number,))
    t2=threading.Thread(target=odd,args=(number,))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
if __name__=="__main__":
    main()                

