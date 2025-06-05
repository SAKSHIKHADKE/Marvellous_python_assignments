def ChkNUM(no):
     if no % 5 == 0 :
        print(True)

     else :
        print(False)
def main():
    print("Enter a number : ")
    num=int(input())
    result=ChkNUM(num)
    print(result)

if __name__=="__main__"  :
    main()     