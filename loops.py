#loops is an instruction that tell a computer to repeatedly perform a specific function
def my_count ():
    for item in range (10):
        print (item)
my_count()
#for is a keyword for loop

#acessing list elements using a loop
def example2():
    languages = ["python","javascript","c++","rubby","c#"]
    for language in languages:
        print (language)

example2 ()

def example3(num):
    for number in range (num):
        print (number)
example3 (5)
example3 (10)
#if is a condition in python
def my_lang():
    languages = ["python","javascript","c++","rubby","c#"]
    for language in languages:
        if language == "python":
            print("you are currently in python class")
my_lang()

def even (num):
    for number in range (num):
        if number % 2 == 0:
            print (number)

even(10)


def odd (num):
    for number in range (num):
        if number % 2 != 0:
            print (number)
odd(10)
    
def power(p):
    my_po = p**2
    if my_po % 2 ==0:
        print("The power is an even number")
    else:
        print("The power is an odd number")
power
