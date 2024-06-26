class student:

    def __init__(self , name , department , gpa ,age): 
        # here the self referes to the onject all other things are 
        # attributes combining all these things only make the student data type

        self.name = name
        self.department = department
        self.gpa = gpa
        self.age = age

        # here we are passing the name and that name is assigned  to the objects name
        # here we are passing the department and that department is assigned  to the objects department
        # here we are passing the gpa and gpa that  is assigned  to the objects gpa
        # Now we have created the student data type and we can use this data type any where, the int() is considerd as a data type  and anything which we put into that int function will be converted into the integer when it statisfy the rule that it should be the whole number
        #like that any anything which put into the student() will be converted into the student data type when it satisfy the rule it should have name,department, and gpa that it it should have 3 values
        #we can import this calss to any other python file using the syntax :     from filename import class name  eg:object.py