class numbers:

    def __init__(self,a):
        self.value=a

    def checkprime(self):
        if self.value<=2:
            return False
        for i in range(2,self.value):
            if self.value%i==0:  
                return False    
            else:
                return True
        
    def perfect(self):
        ans=0
        for i in range(1,self.value):
            if self.value%i==0:
                ans=ans+i
        if ans==self.value:
            return True
        else:
            return False  
            
    def factors(self):
        a=[]
        for i in range(1,self.value):
            if self.value%i==0:
                a.append(i)
        return a
              
    def sumfactors(self):
        sumfactor=0
        for i in range(1,self.value):
            if self.value%i==0:
                sumfactor=sumfactor+1
        return sumfactor
              
    
def main():
        print("enter a number:")
        a=int(input())

        obj1=numbers(a)

        ret1=obj1.checkprime()  
        if ret1:
             print("no is prime")
        else:
             print("no is not prime")

        ret2=obj1. perfect()
        if ret2:
             print("no is perfect")
        else:
             print("no is not perfect")

        ret3=obj1.factors()
        print("list of factors are",ret3)

        ret4=obj1.sumfactors()
        print("sum of factors is:",ret4)
      
if __name__=="__main__":
     main()


