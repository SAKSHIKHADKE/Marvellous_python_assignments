class bookstore:
    classname="noofbooks"

    def __init__(self,a,b):
        self.name=a
        self.author=b

    def __del__(self):    
        print("inside destructor")

    def displayinfo(self):
        print("inside instance method displayinfo")
        print("name :"+self.name)
        print("author:"+self.author)

 
def main():
   
    obj1=bookstore("linux system programming","robert love")
    obj1.displayinfo()

    obj2=bookstore("c programming","dennis richi")
    obj2.displayinfo()

   

    del obj1
    del obj2

if __name__=="__main__":
    main()    