def add(no1,no2):
    return no1+no2

def sub(no1,no2):
    return no1-no2

def mult(no1,no2):
    return no1*no2

def div(no1,no2):
   if no2 !=0 :
       return no1 /no2
   else:
       return "division by zero is not allowed"
   
def main():

    value1=10
    value2=11

    value1=float(input("enter the first number :"))
    value2=float(input("enter the second number :"))

    result=add(value1,value2)
    result=sub(value1,value2)
    result=mult(value1,value2)
    result=div(value1,value2)

    print("addition is:",result)
    print("subtraction is:",result)
    print("multiplication is:",result)
    print("division is:",result)

if __name__=="__main__":
    main()
    

