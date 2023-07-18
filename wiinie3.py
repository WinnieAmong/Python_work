def paye(salary,name,age,location,work_type):
   
    #age=current_year- year_of_birth
    rate = 0.3
    if salary >= 300000:
       tax = rate*salary
       net_pay = salary-tax
       print ("**********************")
       print ("Dear:  ",name)
       print ("Your tax payable is: ",tax)
       print ("And your take home salary is: ",net_pay)
       #print ("Please enter your age here: ",age)
       #print ("Please enter your location here: ",location)
       #print ("Please enter your occupation: ",work_type)
       print ("......................")
       print ("Thank you!")
    else:
       print ("Dear: ",name)
       print ("Your salary is non_taxable")





print ("Your welcome! ")
name = raw_input ("please input your name here: ")
salary = input ("Please input your salary here: ")
age= input ("please enter  your age: ")
location = raw_input ("Please input your location: ")
occupation = raw_input ("Please input your work type: ")

paye (salary,name,age,location,occupation)








