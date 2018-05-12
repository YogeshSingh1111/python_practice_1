
'''
miles = input('Enter Miles : ')

Miles = int(miles)

Kilo = Miles * 1.60934
print ("{} Miles is equal to {} Kilometers".format(Miles, Kilo))
'''

Age = eval(input("Enter your age : "))

if Age < 5:
    print ("Too  young for studies")
elif Age == 5:
    print ("Go to Kindergarten")
elif (Age >= 6) and (Age <= 17):
    print ("Go to grade {}".format(Age-5))
elif (Age > 17) and (Age <= 60):
    print ("Go to college")
else:
    print  ("retire please")
