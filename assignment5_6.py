def celsius_to_fahrenheit(celsius):
   fahrenheit=((celsius*9)/5)+32
   return fahrenheit   

def main():
   celsius=float(input("enter a temperature in celsius:"))

   result=celsius_to_fahrenheit(celsius)
   print("temperature in fahrenheit:",result)

if __name__=="__main__":
   main()   
