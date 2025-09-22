class rectangle:
   
    def __init__(self,a,b):
      self.length=a
      self.width=b

    def arearectangle(self):
       ans=0.0
       ans=self.length*self.width
       return ans
        

    def perimeterrectangle(self):
       ans=0.0
       ans=2*(self.length+self.width)
       return ans

def main():
      obj=rectangle()
      ret=obj.arearectangle()
      print("area of rectangle:",ret)

      ret2=obj.perimeterrectangle()
      print("perimeter of rectangle:",ret2)


if __name__=="__main__":
    main()
    