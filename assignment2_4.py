def sumfactors(n):
    sumfactor=0
    for i in range(1,n+1):
        if n%2==0:
          sumfactors +=i
          return sumfactors
    
    def main():
        num=int(input("enter a number:"))
        sumfactors(num)
        print("sum of factors :",sumfactors(num))

    if __name__=="__main__":
     main()     
