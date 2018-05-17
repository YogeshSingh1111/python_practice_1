
'''
import random
import math

# With lists we can refer to groups of data with 1 name

# Each item in the list corresponds to a number (index)
# just like how people have identification numbers.
# By default the 1st item in a list has the index 0

# [0 : "string"] [1 : 1.234] [2 : 28] [3 : "c"]

# Python lists can grow in size and can contain data
# of any type

randList = ["string", 1.234, 28]

# Create a list with range
oneToTen = list(range(10))

# An awesome thing about lists is that you can use many
# of the same functions with them that you used with strings

# Combine lists
randList = randList + oneToTen

# Get the 1st item with an index
print(randList[0])

# Get the length
print("List Length :", len(randList))

# Slice a list to get 1st 3 items
first3 = randList[0:3]

# Cycle through the list and print the index
for i in first3:
    print("{} : {}".format(first3.index(i), i))

# You can repeat a list item with *
print(first3[0] * 3)

# You can see if a list contains an item
print("string" in first3)

# You can get the index of a matching item
print("Index of string :", first3.index("string"))

# Find out how many times an item is in the list
print("How many strings :", first3.count("string"))

# You can change a list item
first3[0] = "New String"

for i in first3:
    print("{} : {}".format(first3.index(i), i))

# Append a value to the end of a list
first3.append("Another")
'''
'''
import random
random_list = []

for i in range(5):
    random_list.append(random.randrange(1,10))
    print (random_list[i])
'''
#---------------------------------------------------------------------
#Bubble Sort
'''
import random


random_list = []

for i in range(5):
    random_list.append(random.randrange(1,10))
    print (random_list[i])


random_list = [4,4,2,2,1]
for i in range(5):
    print (random_list[i])

length = len(random_list) - 1
value = length

while length > 0:
    j = 0
    while j < length:

        # Tracks the comparison of index values
        print("\nIs {} > {}".format(random_list[j], random_list[j+1]))


        temp_num = random_list[j]
        if random_list[j] > random_list[j+1]:
            print ("\nswitch")
            random_list[j] = random_list[j+1]
            random_list[j+1] = temp_num
        else:
            print("\nDont Switch")

        j += 1
        # Track changes to the list
        for k in random_list:
            print(k, end=", ")
        print()

    print("END OF ROUND")
    length -= 1

#Reverse Bubble
initial = 0
while length > 0:
    j = value

    while j > initial:

        # Tracks the comparison of index values
        print("\nIs {} > {}".format(random_list[j], random_list[j-1]))
        print()

        temp_num = random_list[j]
        if random_list[j] > random_list[j-1]:
            random_list[j] = random_list[j-1]
            random_list[j-1] = temp_num
        else:
            print()

        j -= 1
        # Track changes to the list
        for k in random_list:
            print(k, end=", ")
        print()

    print("END OF ROUND")
    initial += 1
    length -= 1


for k in range(len(random_list)):
    print (random_list[k])
'''
#--------------------------------------------------------------------
'''
num_list = [i*2 for i in range(10)]

for i in num_list:
    print(i)
'''
'''
import math

num_list = [1,2,3,4,5]

list_of_values = [[math.pow(m,2),math.pow(m,3),math.pow(m,4)]
                    for m in num_list]

for i in list_of_values:
    print (i)
'''
'''
list_in_list = [[0]*10 for i in range(6)]

for j in range(6):
    for k in range(6):
        list_in_list[j][k] = "{}:{}".format(j,k)

for j in range(6):
    for k in range(6):
        print (list_in_list[j][k], end="|")
    print()
'''
list_in_list = [[0]*10 for i in range(10)]

for j in range(1,10):
    for k in range(1,10):
        list_in_list[j][k] = j * k
for j in range(1,10):
    for k in range(1,10):
        print (list_in_list[j][k], end=",")
    print()
