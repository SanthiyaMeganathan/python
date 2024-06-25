def translator (phraes):
    transalated=""
    for letter in phraes:
        if letter.lower() in "aeiou":
            if letter.isupper():
                transalated=transalated+"G"
            else:
                transalated=transalated+"g"
        else:
            transalated= transalated + letter
    return transalated

print(translator(input("Enter the pharse :  ")))        
