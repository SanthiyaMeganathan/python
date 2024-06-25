employee_name = open("readable/textfile.txt","r+")
#print(employee_name.readlines())
#print(employee_name.readline())  the readlines will artticulate all the value and return as the array.
#print(employee_name.readable())
#print(employee_name.readlines()[1])
#print(employee_name.read())

for employee in employee_name.readlines():
    print(employee)

employee_name.close()