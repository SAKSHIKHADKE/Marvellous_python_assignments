def check(no):
    for i in range(2,no):
        if no % i == 0 :
            return False
        else :
             return True
      
def main():
        num=int(input("enter a number:"))

        result = check(num)
        
        if result:
            print("it is prime number")
        else:
            print("it is not prime number")    


if __name__=="__main__":
    main()       