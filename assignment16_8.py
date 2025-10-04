def main():
    obj=open("demo.txt","r")
    data=obj.readlines()

    obj.close()

    obj1=open("abc.txt","w")

    for line in data:
        if len(line)>2:
            obj1.write(line)


if __name__=="__main__":
    main()            