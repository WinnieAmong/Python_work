"""
Below are characters,attributes or properties of class Girl
all the object under this class must fulfil these attributes
we have static and dynamic classes


"""
class Girl:
 # all the below are characters,attributes and property   
    name = "Winnie"
    age = 20
    gender ="Female"
    size = "small"
    family ="Olwa's family"
    size_of_bra ="small"
    def greet():
        print("Hello World! ")
        return ""#when you return from a method IT does not print until you call it to print
    #when you call a function it prints out something
    #
print(Girl.greet())
# a variable in a class is a property
print(Girl.name)# the . is used to access the property of the class

girl2 = Girl()
girl2.name = "Esther"
girl2.age = 23
girl2.gender ="Female"

print(f"{girl2.name} is {girl2.age} years old")

girl3 = Girl()
girl3.name = "Trinity"
girl3.age =18
girl3.gender="Female"
print(f"{girl3.name} is {girl3.age} years old")

#create atleast 10 classes corresponding with 5 objects 

#a method is a thing you do to yourself and others
"""
behaviours is a method of doing that very thing
a method defines what the object does to itself
behaviour is how you do it
A function is called a method in oop
The line within the function is refered to behaviours
All objects have a method 


"""

