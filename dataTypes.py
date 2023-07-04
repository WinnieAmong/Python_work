#numeric,string,sequence,mapping,boolean,set
#numerics(int,float,complex)
num1 = 1000
num2 =1000.0
num3 =0
num4 =1+5j
num5 ="1000"
name ='winnie'
print (type(num1))
print (type(num2))
print (type(num3))
print (type (num4))



#string(str)
print (type(num5))
print (type(name))

#sequence(list,tuple,range)
myList = [0,2,4,6]
myList2 = [0,2,4,6,"winnie",10.5]
myTuple = (0,2,4,6)
myDict ={"uganda" : "kampala","italy" :"Rome","france" :"paris","Tanzania": "Dodoma"}
print (type(myList))
print (type(myList2))
print (type(myTuple))

#mapping(dict)
print (type(myDict))

#boolean(True or False)

#set 
mySet  ={0, 5, 10, 15, 20}
mySet2 ={5,5,15,15,20,20}
print (mySet)
print (mySet2)
print (set(myDict))


