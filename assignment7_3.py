even=lambda no:no%2==0

def main():
    data=[]
    size = int(input("enter the element you want to enter : "))
    for n in range(size) :
        a = int(input("enter the number :"))
        data.append(a)

    Fdata=list(filter(even,data))
    print("even numbers:",Fdata)

if __name__=="__main__":
    main()    