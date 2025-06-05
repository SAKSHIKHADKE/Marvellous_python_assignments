def pattern(no) :
    for i in range(1, no + 1) :
        for j in range(i) :
            print("*", end= " ")

def main() :
    no = int(input("enter the number : "))
    pattern(no)

if __name__ == "__main__" :
    main()
