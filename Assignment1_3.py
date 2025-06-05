def Addition(value1,value2) :
    result=value1+value2
    return result
def main() :
    print("Enter first number:")
    no1=int(input())

    print("Enter second number:")
    no2=int(input())
    ans=Addition(no1, no2)
    print("Addition of two numbers :",ans)
if __name__=="__main__" :
    main()    