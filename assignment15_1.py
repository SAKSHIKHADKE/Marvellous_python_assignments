import os
import sys

def check(value):
    ret=os.path.exists(value)

    if ret==True:
        print("dictionary is present")
    else:
        print("dictionary is not present")

def main():
    if len(sys.argv)==2:
        name=sys.argv[1]

    elif len(sys.argv)==1:
        name=input("enter directory name:")

    check(name) 

if __name__=="__main__":
    main()               