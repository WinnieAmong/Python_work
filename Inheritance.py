"""
The peiece of code below demonstrates inheritance ,
where class dog and snake are taking on the properties of a class Animal
The class dog and snake are not related to each other but are related by class Animal
Both the objects of  are instances of the class


"""
class Animal:
    name = ''
    family =''
    gender = ''

class Dog(Animal):# we have inheritated the class ie the dog is inherited in an animal accessing the properties of an animal
    sound = 'bark'
    def investigate(self):
        print (f'{self.name} investigates by sniffing')
# let us instantiate objects of class dog

class Snake(Dog):# we have inheritated the class ie the dog is inherited in an animal accessing the properties of an animal
    sound = 'hissing'
    Snake_sound = sound
    def investigate(self):

        print (f'{self.name} hisses to investigate ')

jsp = Dog()
jsp.name = 'Fredy'
jsp.family = 'dog'
jsp.gender = 'male'
print(f"{jsp.sound}")

#lets us instantiate the in object  of class snake
Snake1 = Snake()
Snake1.name = 'python'
Snake1.family = 'Reptile'
Snake1.gender = 'female'
print(f"{Snake1.sound}")

#convert the first assignment into constractors
#instantiation is the process of instantiating an object