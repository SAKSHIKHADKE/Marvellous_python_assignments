def largest(no):
    max = 0
    for i in no:
        if max < i :
            max = i
    return i
       

def main():
     numbers=[]
     for n in range(5) :
         
        no=int(input("enter numbers:"))
        numbers.append(no)

     result=largest(numbers)
     print("largest number is:",result)

if __name__=="__main__":
    main()     