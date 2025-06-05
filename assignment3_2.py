def max(no):
    max=0
    for i in no:
        if i > max:
            max=i
    return max
    
    

def main():
    n=int(input("enter the number of elemets:"))
    numbers=[]
    for i in range(n):
        b=int(input("enter number:"))
        numbers.append(b)
    result=max(numbers)
    print("maximum number is:",result)

if __name__=="__main__":
    main()        
