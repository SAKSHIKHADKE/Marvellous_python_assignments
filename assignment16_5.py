def main():
    obj=open("error.txt","r")
    data=obj.readlines()

    for lines in data:
        line=lines.split()

        if len(line)>5:
            print(line)



if __name__=="__main__":
    main()    