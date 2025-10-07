import sys

def frequency(filename,word):
    count=0
    obj=open(filename,"r")
    data=open(word,"r")

    for n in data:
        count=count+1

    print("frequency",count)

def main():
    if len(sys.argv)==3:
        filename=sys.argv[1] 
        word=sys.argv[2]

    elif len(sys.argv)==1:
        filename=input("enter the filename:")
        word=input("enter the word you want to frequency:")

        frequency(filename,word)

if __name__=="__main__":
    main()