import sys

def display(value):

    obj=open(value,"r")
    data=obj.read()

    print(data)

def main():
    if len(sys.argv)==2:
        name=sys.argv[1]

    elif len(sys.argv)==1:
        name=input("enter file name:") 

    display(name)

if __name__=="__main__":
    main()
