def calculatefactorial(n):
    factorial=1
    for i in range(n,1,-1):
        factorial*=i
    return factorial    

def main():
    n=int(input("enter a number:"))
    result=calculatefactorial(n)
    print("factorial of number is:",result)
    
    

if __name__=="__main__" : 
    main()   