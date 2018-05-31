'''

def fibo(num):

    if num ==0:
        return 1
    elif num == 1:
        return 1

    else:

        result = fibo(num-1) + fibo(num-2)
        return result


fibo_value = int(input("enter the value till u want fibo series : "))
i = 0
while True:
    if fibo_value <= i:
        break
    else:
        result = fibo(i)
        print(result)
    i += 1
print ("Done")
'''
'''
import os

with open("myText.txt",mode = "w", encoding="utf-8") as myfile:
    myfile.write("very first line of message\nSecond line of message\nThird line of message")

with open("myText.txt", encoding="utf-8") as myfile:
    linenum = 1
    while True:
        line = myfile.readline()
        if not line:
            break

        split_string = line.split()
        string_length = len(split_string)
        total_char = 0

        for i in split_string:
            for j in i:
                total_char += 1

        average_char = total_char/string_length

        print ("line number = ", linenum,"\ntotal words in this line is ", string_length,"\nAvg words per line is {:.2f}".format(average_char))

        linenum +=1
'''
