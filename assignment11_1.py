a=0
def value(n):
    global a
    while a<=n:
        print(a)
        a=a+1
        value(n)
          
def main():
    no=int(input("enter a number:"))
    value(no)
if __name__=="__main__":           
    main()