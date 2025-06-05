def sum(no):
    sum=0
    while(no>=1):
        sum=sum+no
    return sum

def main():
    no=int(input("enter a number:"))
    ret=sum(no)
    print(ret)
if __name__=="__main__":
    main()    
