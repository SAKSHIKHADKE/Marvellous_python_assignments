def largest(no1,no2,no3):
  a = 0
  if no1>=no3:
    if no1>=no2:
      a=no1
    else:
      a=no3
  else:
    if no2>=no3:
      a=no2
    else:
      a=no3    
  return a

def main():
  no1=int(input("enter first number:"))
  no2=int(input("enter second number:"))
  no3=int(input("enter third number:"))
  result=largest(no1,no2,no3)
  print("largest no is:",result)

if __name__=="__main__":
  main()    
