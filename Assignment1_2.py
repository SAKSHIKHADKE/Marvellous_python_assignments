def ChkNUM(no) :
    if no % 2 == 0:
        print("Even number")
    else :
        print("odd number")
        return
def main() :
        print ("Enter a number : ")
        no = int(input())
        ChkNUM(no)
if __name__=="__main__":

         main()    