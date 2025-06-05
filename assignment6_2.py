def even():
    sum=0
    for i in range(1,101):
        if i % 2 == 0 :
            sum += i
    return sum
       

def main():

    result = even()
    print(" sum of even numbers between 1 to 100 is:",result)

if __name__=="__main__":
   main()   
