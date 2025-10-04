def main():
    obj=open("marks.txt","r")
    data=obj.readlines()

    for line in data:
        name,marks=line.split("-")
        
        if int(marks)>75:
            print(line)

if __name__=="__main__":
    main()    