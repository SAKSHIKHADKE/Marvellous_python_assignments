def pattern(n):
    for i in range(n):
        print( "*" *n)

def main():
    n=int(input("enter a number"))

    pattern(n)

if __name__=="__main__":
    main()    
