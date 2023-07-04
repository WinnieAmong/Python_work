#function is a group of codes that relates to give a name
#functions to create a value
# num1 = 50
# num2 =100
# num3 =num1 + num2
# print (num3)
#multi-line comments

#
"""

"""
def sum():
    num1,num2 = 30,57
    num3 =num1 + num2
    print(num3)
sum()

#subtraction


def sub():
    num1, num2 = 400,9
    num3 =num1-num2
    print(num3)

sub()


#gets a remainder of 2 variables

def rem():
    num1,num2 = 9,5
    num3 =num1 % num2
    print (num3)


rem() #this is calling the function above for execution

#division
def div():
    num1,num2 = 9,2
    num3 =num1/num2
    print (num3)

div()
#a named group of statements is refered to as function

#list of members
def my_list():
    list1 = [1,2,3,4,10]
    print (list1)


my_list()
"""
Declaring comments on osman
"""

def osman():
    osman =[100,[200]]
    osman2 =[1000,[[2000,3000]]]
    print (osman[1][0])
    print (osman2[1][0][1])
osman()
"""
Declaring comments on zebra
"""

def zebra():
    zebra = {"name":"tongs","legs":4,"color":"black and white","sex":"male"}
    print(zebra.keys())
    print(zebra)
    zebra.__delitem__('sex')
    print(zebra)

zebra()
"""
Fruit
"""

def fruits():
    fruits =["orange","pineapple"]
    fruits. append("apple")
    fruits.pop()
    print(fruits)
    print(fruits)
fruits()

def list():
    myList = [0,1,2,3,4,5,6,7,8,9]
    myList2 = [10,20,30,40,50]
    print (myList[3])
    print (myList2[4])
    print (myList2[-1])
list()

def tupel():
    myTupel =(10,20,30,40,50)
    print (myTupel)

tupel() 