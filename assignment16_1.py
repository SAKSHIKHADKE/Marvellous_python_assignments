def main():
    obj=open("student.txt","w")

    name1=input("enter first name :")
    obj.write(name1+"\n")

    name2=input("enter second name :")
    obj.write(name2+"\n")

    name3=input("enter third name :")
    obj.write(name3+"\n")

    name4=input("enter fourth name :")
    obj.write(name4+"\n")

    name5=input("enter fifth name :")
    obj.write(name5+"\n")

    obj.close()

if __name__=="__main__":
    main()    

