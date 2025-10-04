def main():
    obj=open("demo.txt","r")
    data=obj.read()

    line=0
    character=0
    word=0

    for n in data :
        character+=1

        if n=="\n":
            line+=1

        if n==" ":
            word+=1

    print("character in the file :",character )
    print("line in the file:",line)
    print("word in the file :",word)

if __name__=="__main__":
    main()
