def minimum(numbers):
    min=numbers[0]
    for n in numbers:
        if n<min:
            min=n
    return min        

def main():
    n=int(input("enter the number of elemenst:"))
    numbers=[]
    for i in range(n):
        num=int(input("entered elements :"))
        numbers.append(num)
        
    min_number = minimum(numbers)   
    print("minimum number is:",min_number)


if __name__=="__main__":
    main()