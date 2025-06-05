def addition(n):
   a=0
   for i in n:
      a=a+i

   return a
def main():
   n=int(input("enter the number of elements:"))
   numbers=[]
   for i in range(n):
      num=int(input("enter a number :"))
      numbers.append(num)
   result=addition(numbers)
   print("sum of elements:",result)

if __name__=="__main__":
    main()       