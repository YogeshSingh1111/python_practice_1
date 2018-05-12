'''
# find odd number

for i in range(21):
    if not(i % 2 == 0) :
        print (i)

# for j in range(21)
'''
'''
# Compound interest

money = input ("how much to invest : ")
interest_rate = input ("how much interest rate : ")

money = float(money)
interest_rate = float(interest_rate) * 0.01

for i in range(10):
    money = money + (money * interest_rate)

print ("Investment after ",i+1," years is {:.2f}".format(money))
'''



# Christmas Tree

Tree_height = eval(input("How tall is tree : "))
Tip_stub = Tree_height - int(1)

space = Tip_stub
Hash = int(1)

while (Tree_height != 0 ):

    # Space loop
    for i in range(space):
        print(' ', end="")

    # hash loop
    for i in range(Hash):
        print ('#', end="")

    print ()

    Hash += 2
    space -= 1
    Tree_height -= 1


for i in range(Tip_stub):
    print (' ', end="")
print ('#', end="")
