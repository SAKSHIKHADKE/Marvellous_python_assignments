def main():
    obj=open("input.txt","r")
    data=obj.read()

    obj2=open("destination.txt","w")
    obj2.write(data)


if __name__=="__main__":
    main()    