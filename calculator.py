import random as random
keepGo=True
dino=True
newnum=1
while keepGo == True:
    nums={}
    signs={}
    key=1
    dino=False
    while dino==True:
        newnum=int(input("input new number"))
        nums[key] =newnum
        signsnew=input("input + _ * or / for addition subtraction multiplication or divition")
        signs[key]=signsnew        
        key+=1
        dino=(input("you will keep going T for true or f for false"))
        if dino == "f":
            dino=False
        elif dino == "t":
            dino=True
    for range key    
      
