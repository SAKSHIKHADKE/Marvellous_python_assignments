class circle:
    pi=3.14

    def __init__(self,a):
        print("inside circle constructor")
        self.radius=a

    def calculatearea(self):
        ans=0.0
        ans=circle.pi * self.radius * self.radius
        return ans 

class circleX(circle):
    def __init__(self,b):
        print("inside circlex constructor")
        super().__init__(b)

    def calculatecircumference(self):
        ans=0.0
        ans=2*circle.pi*self.radius
        return ans

def main():
    obj=circleX(10.5)
    ret=obj.calculatearea()
    print("area of circle is:,ret")
    ret=obj.calculatecircumference()
    print("circumference of circel:",ret)

if __name__=="__main__":
    main()
        