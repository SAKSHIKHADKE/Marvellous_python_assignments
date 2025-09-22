class employee:

    def __init__(self,a,b,c):
        self.name=a
        self.emp_id=b
        self.salary=c

    def displayinfo(self):
        print("name:"+self.name)
        print("emp_id:"+self.emp_id)
        print("salary:"+self.salary)

def main():
        name=input("enter the name:")
        emp_id=int(input("enter the id:"))
        salary=int(input("enter the salary:"))

        obj=employee(name,emp_id,salary)

        obj.displayinfo()

        obj.name()
        obj.emp_id()
        obj.salary()
       

if __name__=="__main__":
    main()            