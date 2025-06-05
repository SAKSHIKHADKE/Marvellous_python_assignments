from marvellous_assignment import chkprime
    
def main():
    n=int(input("enter the number of elements:"))
    elements=[]
    for _ in range(n):
        num=(int(input("enter elements:")))
        elements.append(num)

    result=chkprime(elements)
    
    print("addition of prime number is:",result)
if __name__=="__main__":
   main()    
