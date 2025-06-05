def add(value):
   result = 0
   for no in value:
        result+=int(no)
   return result

def main():
    value=input("enter a number:")
    n=add(value) 

    print("sum of digits :",n)
if __name__=="__main__":
    main()
       

