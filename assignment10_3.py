from functools import reduce

def main():

    data=[]
    size = int(input("enter the number of element you want to enter : "))

    for n in range(size) :
        a = (int(input("enter the element : ")))
        data.append(a)
        
    print("input data:",data)

    Fdata=list(filter(lambda x:70 <= x and x<=90, data))
    print("Filter output:",Fdata)

    Mdata=list(map(lambda x:x+10,Fdata))
    print("Map output:",Mdata)

    Rdata=reduce(lambda x,y:x+y,Mdata)
    print("Reduce output:",Rdata)

if __name__=="__main__":
    main()