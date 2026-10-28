import random
num= random.randint(1,10)
guess=int(input("please guess your number"))
if num==guess:
    print(" you are right")
else:
    print(" sorry you are wrong")
