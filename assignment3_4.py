def frequency(value1,value2):
    a=0
    for n in value1:
        if n==value2:
            a+=1
    return a   
def main():     
     elements=[]
     
     n=int(input("enter the number you want to find frequency of:"))
     size=int(input("entered number of elements:"))


     for i in range(size):
        b=int(input("enter the element:"))
        elements.append(b)

     result=frequency(elements,n)
     print("the frequency of search_num is:",result)

if __name__=="__main__":
    main() 
        