def calculate_rectangle(length,width):
    area=length*width
    perimeter=2*(length*width)
    return area
    return perimeter 

def main():
    area=float(input("enter length"))
    perimeter=float(input("enter width"))
    result= calculate_rectangle(area,perimeter)
    print("area of rectangle:",result)
    print("area of perimeter:",result)

if __name__=="__main__":
    main()     
   