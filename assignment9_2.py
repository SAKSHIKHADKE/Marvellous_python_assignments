from multiprocessing import Process

def square(numbers):
    result=[]
    for i in numbers:
        a = i ** 2
        result.append(a)
    return result
    
def main():
    data=[1,2,3,4,5]
   
    p=Process(target=square,args=(data,))
    ret=p.start()
    print(ret)

if __name__=="__main__":
   main()    
