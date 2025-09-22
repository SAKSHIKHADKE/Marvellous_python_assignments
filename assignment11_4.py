def power(a,b):
    c=0
    d=1
    while c<b:
        d=d*a
        c=c+1

        power=(a,b)
    return d

def main():
    no1=int(input("enter the base:"))
    no2=int(input("enter the power:"))

    ret=power(no1,no2)

    print("result is: ",ret)

if __name__=="__main__":
    main()    
          