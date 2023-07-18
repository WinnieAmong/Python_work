"""
The method of a class __init__is called a constractor
A constractor is used to initialise an instantiated object
constractor is used to bridge for the paramenters and arguments(values of the object)
the __init__ helps us to give the actual values of the object
these values are assigned to the properties of the class ie motto,
'self' is the identifier
self is the reference that denotes the propertis/attributes of the class
self.name is a property the name is the value
the values of the method is
self is a reference of the object property
self is not counted as a property
the shish function is a method that we use to create value (__init__)
"""
class School():
    def __init__(self,name,motto,location, nu_of_students,nu_of_teachers,uneb_nu):
        self.name = name
        self.motto = motto
        self.location = location
        self.nu_of_students = nu_of_students
        self.nu_of_teachers = nu_of_teachers
        self.uneb_nu = uneb_nu
    def register(self):
        print(f"{self.name} is fully registered with UNEB.")

school1 = School('DOC','Fear Not The Truth','Lira',100,30,'u0072')
school1.register()
school2 = School('Kinyara ss','Success Through Education','Masindi',700,45,'u1921')
school2.register()#a method register is overloaded coz each object uses it differently
#This is called instanciation
#ie we instanciate an object
#Instanciation is the process of giving value to the object 
#A method of a class(__init__) is named a constructor


class Country:
    def __init__(self,A,B,C):
        self.name =A
        self.city = B
        self.pop = C
country1 = Country('Kenya','Nairobi',40000)


class Continent:
    def __init__(continent,A,B,C):
        continent.name = A
        continent.lakes = B
        continent.rivers = C
        