def reduceX(task,values):
   result=0
   for no in values:
     result=task(result,no)
     return result
   
addition = lambda x,y:x+y

def main():
    data=[]
    size = int(input("enter the number of element you want to enter : "))

    for n in range(size) :
        a = int(input("enter the element : "))
        data.append(a)
        
    print("input data:",data)

    Fdata=list(filter(lambda x: x >= 70 and x <= 90, data))
    print("Filter output:",Fdata)

    Mdata=list(map(lambda x:x+10,Fdata))
    print("Map output:",Mdata)

    Rdata=reduceX(addition,Mdata)
    print("Reduce output:",Rdata)

if __name__=="__main__":
    main()