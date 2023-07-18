'''
Polymorphism is the ability of an object  to take  differents forms or behaviours depending on the the context
It  shows child classes exhibiting polymorphism by overiding the common method
In this code the 'make_sound' is overidden by the cat and the dog
'''
#class representing cat with attributes and methods
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")# calls the sound method of the cat
#cat1 = Cat('Ben',3)
#cat1.make_sound()

#class representing attributes and methods of dog
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")# outputs the sound of the class Dog


#
cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)
#prints the output of the method and behaviur of the cat and dog
# Iterates through a collection of animals, invokes their sound, info, and sound methods

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()
