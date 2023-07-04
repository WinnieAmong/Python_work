def sum():
    num1,num2 = 3,8
    num3= num1 + num2
    print (num3)

sum()

#the functions can dynamically add values
def add(num1,num2):
    num3 = num1 + num2
    print (num3)
add(3,8)
add(4,6)

def sub(num1,num2):
    num3 = num1 - num2
    print (num3)

sub(10,4)


def div(num1,num2):
    num3 =num1 / num2
    print (num3)

div(100,50)

def modulous(num1,num2):
    num3 =num1 % num2
    print (num3)

modulous(100,30)

def prod(num1,num2):
    num3 =num1 * num2
    print (num3)

prod(50,4)
"""
 A function is self contained
"""
#The above are called static functions