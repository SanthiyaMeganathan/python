try:
    value=10/0
    number=int(input("Enter the input:  "))
    print(number)
except ZeroDivisionError:
    print("number cannto be divide by zerror")
except ValueError:    
    print("Invalid input. Please enter a valid number")