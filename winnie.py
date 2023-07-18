'''
This code represents the usage of functions
Functions are reusable blocks of code that perform a set of relted set of tasks
'''

#The function performs tests on given inputs
def tests(test1, test2):
	#check if test1 is equal to test2
	if test1 == test2:
		#check if test1 is not equal to test2
        # perform someother actions or return a different value
		return test1
	else:
		#return the value of test2 to the caller
		return test2
	
	## This code takes input from the user for test1 and test2 marks and stores them as integers.
test1 = int(input('Please enter Marks for test one: '))
test2 = int(input('Please enter Marks for test two: '))

'''
Ask the user to enter marks for test1 and test2
The input function is used to capture input,which is then converted to an integer
using the int()function
the entered marks will be stored in the variables test1 and test2 respectively

'''
#the function handles the course work for a given input parameter
def courseWrk(cswork):
	# Calculate the overall tests mark using the 'tests' function 
    # and assign it to the variable 'testsMark'
	testsMark = tests(test1,test2)
	#calculate the average of cswork and testsMark and assign it to avgtestsCswork
	avgtestsCswork = (cswork + testsMark)/2
	#Calculate the final tests and coursework mark by multiplying the average by 40%
	fnltestsCswork = avgtestsCswork * (40/100)
	#print a visual separator or divider consisting of a series of dots
	print('..............................')
	#print the final coursework mark
	print('your final coursework marks is: ', fnltestsCswork)
	print('..............................')
# Ask the user to enter their course work marks and store the value in the variable 'cswork'
cswork = int(input('Please enter your course work Marks: '))
#the function cswork is called 
courseWrk(cswork)
"""
The function tests to give test1 and test2
>checks if test1 is equal to test2 and return test1 if not equal or else return test2 to the caller
>Takes in the input from users for test1 and test2 and stores them as intgers
The function handles the coursework for a given input in the parameter
>calculate the overall testmark and assign it to the testsMark
>find the average of the cswork and testMark
>the final cswork is got bymultiplying average cswork by 40%
the final coursework is then called as an arguement

"""