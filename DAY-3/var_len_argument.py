#Write a Python function student_data () which will print the id of a student (student_id). If the user passes an argument student_name or student_class the function will print the student name and class.

#specifying default value for student_id variable 
def student_data(student_id=300, **kwargs):

    print(f'\nStudent ID: {student_id}')
    
    #below statement will be printed if only name is passed as keyword argument 
    if 'student_name' in kwargs:
        print(f"Student Name: $ {kwargs['student_name']}")
    


    #below statement will be printed if  name and class is passed as keyword argument 
    if 'student_name' and 'student_class' in kwargs:
            print(f"\nStudent Name: $ {kwargs['student_name']}")
            print(f"Student Class: $ {kwargs['student_class']}")

 

#passing id and name as argument
student_data(student_id='302', student_name='Rohan Verma')


#passing only name
student_data(student_name='pritam kumar')


#passing id, name and class
student_data(student_id='305', student_name='Paul william', student_class ='X')
