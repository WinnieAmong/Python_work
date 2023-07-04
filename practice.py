def my_function():
  print("Hello from a function")
  #a function is defined using "def" keyword
  def my_function():
      print("Hello from a function")

my_function()

def my_function(fname):
   print(fname + " Refnes")
my_function("Email")
my_function("Tobius")
my_function("Linus")

def my_family(fname, lname):
  print(fname + " " + lname)

my_family("Emil", "Refsnes")

def exercise2():
    fruits = ("Apple","banana","cherry")
    for fruit in fruits:
       print(fruit)

exercise2()


#getting characters at the given position
a = "Hello, World!"
print(a[1])

#determining the length of the string
a = "Hello, World!"
print(len(a))