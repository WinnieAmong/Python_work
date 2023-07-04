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
A function calculates the final coursework mark



"""