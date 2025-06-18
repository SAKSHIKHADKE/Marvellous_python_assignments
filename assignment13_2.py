class bankaccount:
    ROI=10.5

    def __init__(self,a,b,c,d):
        self.name=a
        self.amount=b
        self.amount1=c
        self.amount2=d

    def display(self):
        print("name:",self.name) 
        print("amount:",self.amount)

    def deposite(self):
        return self.amount+self.amount1       
    
    def withdrawl(self):
        return self.amount-self.amount2
    
    def calculateintrest(self):
        rate= bankaccount.ROI/100
        intrest= self.amount*rate*1
        return intrest
    
def main():
    name=input("enter the name:")
    amount=int(input("enter the amonut:"))
    de=int(input("enter the amount:"))
    wit=int(input("enter the amount:")) 

    obj=bankaccount(name,amount,de,wit)

    obj.display()

    ret=obj.deposite()
    print("total amount:",ret)

    
    ret1=obj.withdrawl()
    print("total amount:",ret1)

    
    ret2=obj.calculateintrest()
    print("total amount:",ret2)

if __name__=="__main__":
    main()    