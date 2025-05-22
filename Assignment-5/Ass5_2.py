def Vowel():

    char = str(input("Enter the Character: "))

    if (char == 'a' or char == 'e' or
        char == 'i' or char == 'o' or char == 'u'):
        
        print(char,"is a Vowel")
        
    else:
        print(char,"is a Consonant")
       

Vowel()