from datetime import datetime
dob = input("Enter date of birth dd/mm/yyyy format: ")
dob = datetime.strptime(dob, '%d/%m/%Y')
print(datetime.today())
print ("Years %d"%((datetime.today() - dob).days/365))
print(dob)

'''o/p:
Enter date of birth dd/mm/yyyy format: 29/6/1999
2020-10-04 21:00:56.953783
Years 21
1999-06-29 00:00:00'''
