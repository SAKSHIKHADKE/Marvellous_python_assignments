def palindrome(word):
    rword=""
    for char in word:
        rword=char+rword

    if word==rword:
        print("the word is palindrome")
    else:
        print("the word is  not palindrome")

def main():
    word=input("enter the word:")
    print(word)
    palindrome(word)

if __name__=="__main__":
    main()
