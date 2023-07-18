students = [] #initialise an empty list to store pupils information
def register_students ():

    num_students = ("please enter the number of pupils you want to register: ")
    
print ("Your Welcome to Auntie Esther'Nursery School!!!")
print("//////////////////////////")
amount = 400000
print("fees: ",amount)
name = raw_input("Please input your name here: ")
Date_Of_birth =raw_input("Please enter your date of birth: ")
Class_registered_for = raw_input ("please enter your class here: ")
location =raw_input ("Please enter your location here: ")
parents_name =raw_input("please enter your parents name here: ")
status_of_payment=raw_input("Please enter your status of payment? (yes/no) ")
print("--------------------------")

student ={
    "name":name,
    "Date_Of_birth":Date_Of_birth,
    "class_registered_for":Date_Of_birth,
    "location":location,
    "Parents_name":parents_name,
    "state_of_payment":status_of_payment

}

students.append(student)#append the students to the list of registered student
print("Registration complete!!")


register_students()

def display_registered_pupils():
    print("")
    print("--------------------------")













   



    
    











