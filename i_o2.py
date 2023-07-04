def paye(salary,name):
    rate = 0.3
    if salary >= 300000:
      tax = rate*salary
      net_pay = salary-tax
      print ("**********************")
      print ("Dear:  ",name)
      print ("Your tax payable is: ",tax)
      print ("And your take home salary is: ",net_pay)
      print ("......................")
    else:
       print ("Dear: ",name)
       print ("Your salary is non_taxable")





print ("Your welcome! ")
name = raw_input ("please input your name here: ")
salary = input ("Please input your salary here: ")
age = input ("Please input your age here: ")
location = raw_input ("Please input your location: ")
occupation = raw_input ("Please input your work type: ")

paye (salary,name)