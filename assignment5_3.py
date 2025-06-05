def check(age):
    if age >=18:
        print("eligible to vote")
    else:
        print("not eligible to vote")

def main():
    age=int(input("enter age:"))    
    check(age)

if __name__=="__main__":
    main()    