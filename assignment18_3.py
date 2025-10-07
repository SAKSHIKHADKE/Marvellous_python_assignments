import sys

def display(value):

    obj=open(value,"r")
    data=obj.read()

    obj2=open("demo.txt","w")
    obj2.write(data)

    obj.close()
    obj2.close()

def main():
    if len(sys.argv)==2:
        filename=sys.argv[1]

    elif len(sys.argv)==1:
        filename=input("enter the filename:")

    display(filename)

if __name__=="__main__":
    main()            