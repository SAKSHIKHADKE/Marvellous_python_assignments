fact=1
b=1
def factorial(no):
    global fact, b
    while no>=b :
        fact=fact*b
        b=b+1
        factorial(no)
    return fact
    
def main():
    no=int(input("enter a number:"))
    ret=factorial(no)
    print(ret)
if __name__=="__main__":
    main()    