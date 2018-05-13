
'''
def substrat(num1,num2):
    return num2 - num1


equation = input ("Enter the equation : ")


split_equation = equation.split()

num1 = split_equation[2]
num2 = split_equation[4]

print ("the value of X is :", substrat(int(num1),int(num2)))
'''
'''
# finding prime numbers

def check_if_prime(number):
    for i in range(2,number):
        if (number % i) == 0:
            return False
    return True


def get_the_max(max_mumber):
    list_of_primes = []
    for i in range(2,int(max_mumber)+1):
        if check_if_prime(i):
            list_of_primes.append(i)
    return list_of_primes


max_num = int(input("enter the number upto which u want prime numbers for : "))
print ("list of primes is as follows")
for i in get_the_max(max_num):
    print (i)
'''
import math

def shape(type):
    shape_type_capital = type.upper()
    return shape_type_capital

def area(A):
    if A == "CIRCLE":
        circle_area()
    elif A == "RECTANGLE":
        rectangle_area()
    elif A == "SQUARE":
        square_area()
    elif A == "TRIANGLE":
        triangle_area()
    else:
        print ("Please enter basic shapes(Square, Rectangle, Triangle and Circle) with correct spelling")

def  circle_area():
    radius = float(input("please enter the radius : "))
    area = math.pi * (math.pow(radius,2))
    print ("Area of circle is : {:.2f}".format(area))

def  rectangle_area():
    length = float(input("please enter the length : "))
    breath = float(input("please enter the breath : "))
    area = length * breath
    print ("Area of rectangle is : {:.2f}".format(area))

def  square_area():
    length = float(input("please enter the length of side: "))
    area = math.pow(length,2)
    print ("Area of Square is : {:.2f}".format(area))

def  triangle_area():
    base = float(input("please enter the base : "))
    height = float(input("please enter the height : "))
    area = 0.5 * (base * height)
    print ("Area of Triangle is : {:.2f}".format(area))

shape_type = input ("type the shape u want to find the area of ?  ")
print ("You have selected ", shape(shape_type))
area(shape(shape_type))
