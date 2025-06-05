def main():
    no1=int(input("enter a number:"))
    no2=int(input("enter a number:"))
      
    multiplication=lambda x,y:x*y

    print("result is:",multiplication(no1, no2))

if __name__=="__main__":
    main()