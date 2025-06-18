from functools import reduce
def prime(no):
    if no<2:
        return False 
    for i in range(2,no+1):
        if no%i==0:
            return False
        return True


def maximum(a,b):
     if b>a:
         a=b
     return a 

def main():
    data=[]
    n=int(input("enter the number of elements you want to enter:"))
    for i in range(n):
        num=int(input("enter the number of element:"))
        data.append(num)

    fdata=list(filter(prime,data))    
    print("fdata")

    mdata=list(map(lambda no:no*2,fdata))
    print(mdata)

    rdata=reduce(maximum,mdata)
    print(rdata)

if __name__=="__main__":
    main()    
        
