
'''
check_Y_N = input ("Want to add new employee, type Y or N " )
User_Input = check_Y_N.lower()
print(User_Input)
Employee = []


while User_Input == "y":
    fname, lname = input("Enter employee name : ").split()
    Employee.append({"fname": fname, "lname": lname})
    check_Y_N = input ("Want to add new employee, type Y or N " )
    User_Input = check_Y_N.lower()

for i in Employee:
    print(i["fname"], i["lname"])
'''

'''
customer = []

while True:
    entered_value = input ("Want to add new employee, type Y or N : " )
    entered_value = entered_value[0].lower()

    if  entered_value == "n":
        break
    elif entered_value == "y":
        fname, lname = input("Enter employee name : ").split()
        customer.append({"fname":fname,"lname":lname})
    else:
        break

for cust in customer:
    print (cust["fname"], cust["lname"])

'''

'''
#Factorial

def factorial(num):
    if num <= 1:
        return 1
    else:
        result = num * factorial(num -1)
        return result

print ("4! = ",factorial(4))
'''

#fibonachi
def fibo(num):
    if num <= 2:
#        result.append() = 1
        return 1
    else:
        result = fibo(num-1) + fibo(num-2)
        return result
print ("fibo at 11 ", fibo(11))
