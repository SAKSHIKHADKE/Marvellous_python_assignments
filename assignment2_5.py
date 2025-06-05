def check(no):
   if no <=1:
      return False
      for i in range(2,no+1):
         if no %i==0 :
             return False
         return True
      
def main():
        num=int(input("enter a number:"))
        
        if check(num):
            print("it is prime number")
        else:
            print("it is not prime number")    


if __name__=="__main__":
    main()       
         