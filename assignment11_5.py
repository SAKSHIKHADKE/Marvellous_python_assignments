"""def zero(no) :
    a = 0
    for n in no:
        while int(n) == 0 :
            a = a + 1
            n = int(n) + 1
    return a"""
a = 0
def zero(no) :
    global a
    for n in no :
        while int(n) == 0:
            a = a + 1
            n = int(n) + 1
            zero(no)
    return a 

def main () :
    no = input("enter the number : ")

    ret = zero(no)

    print("zeros in givin number are :",ret)

if __name__ == "__main__" :
    main()

Count = 0

def CountZero(No):
    if(No != 0):
        Digit = No % 10
        if Digit == 0:
            Count+=1
        CountZero(No / 10)
    return Count