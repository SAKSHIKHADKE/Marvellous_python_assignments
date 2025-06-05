def vowel(n):
    char=n.lower()
    vowels=['a','e','i','o','u']

    if char in vowels:
        print("the char is a vowel")
    else:
        print("the char is a consonant")  

def main():
    char=input("enter a character:")
    vowel(char)



if __name__=="__main__":
    main()    

