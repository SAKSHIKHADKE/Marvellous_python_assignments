def check(no):
    if no%2==0:
        print("no is even")
    else:
        print("no is odd")

def main():
    no=int(input("enter a number:"))     
    check(no)       

if __name__=="__main__":
    main()    