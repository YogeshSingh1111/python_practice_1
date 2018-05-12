'''

while True:
    try:
        number = int(input("Please enter number between 1 and 10 : "))
        break

    except ValueError:
        print("You didn't enter a number")

    except:
        print("An unknown error occured")


if (number >= 1) and (number <=10):
    print ("Your number is {}".format(number))
else :
    print ("Entered number is not between 1 and 10")
'''

# A - Z : 65 - 90
# a - z : 97 - 122

'''
print("A = ",ord("A"))
print("65 = ",chr(65))
'''

secret_string = input("Enter a secret string : ")
length = len(secret_string)
holder_string = ""
holder_string_2 = ""

for i in range(length):
    holder_string = holder_string + str(ord(secret_string[i])+91)
print (holder_string)

# Why add by 91?
# coz,unicode for "space" is 9, adding by 91 will gurantee that every converted ubicode will be 3 digit

for i in range(0, len(holder_string)-1,3):
    holder_string_2 += chr(int(holder_string[i] + holder_string[i+1] + holder_string[i+2])-91)
print (holder_string_2)
