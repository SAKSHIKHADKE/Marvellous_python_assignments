def ChkNUM(no) :
    if no > 0 :
        print("positive number")
    elif  no == 0 :
        print("zero")

    else :
        print("Negative number")
  

def main():
    print("Enter a number : ")
    num=int(input())
    ChkNUM(num)

if __name__=="__main__" :
    main()            
