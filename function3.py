def add (num1,num2):
    num3 = num1 + num2
    print (num3)

def sub (num1,num2):
    num3 = num1 - num2
    print (num3)

#forcing the function to communicate

def add2 (num1,num2):#num1 and num2 are called parameters
    num3 = num1 + num2
    return num3
    print (num3)
#the word return stops the whole process of the code
#no output will be shown after return

def sub2(num1):
    num3 = add2(4,12) - num1
    print (num3)
sub2(5)   # 5 is an argument or actual parameter or formal parameters

#the above functions are called dynamic functions or parametalised functions
add2(2,3)
ans = add2 (3,6)
print (ans)
#a function that calls a returned value from another function
#is called a "calling function"