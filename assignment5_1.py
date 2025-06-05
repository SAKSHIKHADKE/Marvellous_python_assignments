def add(no1,no2):
    return no1+no2

def sub(no1,no2):
    return no1-no2

def mult(no1,no2):
    return no1*no2

def div(no1,no2):
    return no1 /no2
   
def main():
    value1=int(input("enter the first number :"))
    value2=int(input("enter the second number :"))

    result1 =add(value1,value2)
    result2 =sub(value1,value2)
    result3 =mult(value1,value2)
    result4 =div(value1,value2)

    print("addition is:",result1)
    print("subtraction is:",result2)
    print("multiplication is:",result3)
    print("division is:",result4)

if __name__=="__main__":
    main()
    

