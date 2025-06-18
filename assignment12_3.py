class arithmatic:
    def __init__(self,a,b):
        self.value1=a
        self.value2=b

    def addition(self):
        result=0
        result=self.value1+self.value2    
        return result
    
    def subtraction(self):
        result=0
        result=self.value1-self.value2
        return result

    def multiplication(self):
        result=0
        result=self.value1*self.value2
        return result
    
    def division(self):
        result=0
        result=self.value1/self.value2
        return result
    
def main():
    print("enter first number:")
    value1=int(input())

    print("enter second number:")
    value2=int(input())

    obj1=arithmatic(value1, value2) 
   

    p=obj1.addition()
    print(p)
    q=obj1.subtraction()
    print(q)
    r=obj1.multiplication()
    print(r)   
    s=obj1.division()
    print(s)

   

if __name__=="__main__":
    main()