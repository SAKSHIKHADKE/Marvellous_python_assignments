def prime(num):
    if num<=1:
         False
    for i in range(2,num):
        if num%i==0:
            return False
    else: 
        return True

def main():
    numbers=[]

    num=int(input("enter numbers of list:"))
    for a in range(num):
        b=int(input("enter the number:"))
        numbers.append(b)
    ret=list(filter(prime,numbers))  
    print("prime numbers:",ret)

if __name__=="__main__":
    main()    