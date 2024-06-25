def sayhi(name , age):
    print("Hello, user!  you are " + name  +  str(age))
sayhi("mike" , 2)  
#sayhi() #this will give an error because the function is expecting an argument
sayhi("nicola" ,"3" )
# if you have entered the number in double quote then you don't need to convert 
# the age into the str but suppose if you eneterd as number without
#  the double quote then it number so, you will nit be able to concatenate
#  the string and number so that you need to convert it to stringby using the
#  function str(parameter)