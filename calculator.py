import random as random
keepGo=True
dino=True
newnum=1
while keepGo == True:
    nums=()
    signs=()
    while dino==True:
        newnum=int(input("input new number"))
        nums.append(newnum)
        signsnew=input("input + _ X or / for addition subtraction multiplication or divition")
        signs.append(signsnew)
