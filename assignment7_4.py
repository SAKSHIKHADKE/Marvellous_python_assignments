from functools import reduce
product=lambda x,y:x*y

def main():
    numbers=[]
    num=int(input("enter list of numbers:"))
    result=numbers.append(num)
    
    reduce=reduce(product,numbers)
    print("product of numbers is:",reduce())


if __name__=="__main__":
    main()