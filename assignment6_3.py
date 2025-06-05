def multiplication(no):
    for i in range(1,11):
        print(no,"*",i,"=",no*i)

def main():
    no=int(input("enter a number:"))
    result=multiplication(no)
    print("multiplication table:",result)

if __name__=="__main__":
    main()