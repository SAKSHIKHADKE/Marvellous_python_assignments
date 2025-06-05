def fact(num):
   fact=1
   for i in range(num,1,-1):
      fact*=i
   return fact 
def main():
   num=int(input("enter a number:"))
   result=fact(num)
   print("factorial of:",result)    

if __name__=="__main__":
   main()    