import random
num=random.randint(1,12)
tries=0
while True:
    guess=int(input("enter any number"))
    tries+=1
    if guess==num:
     print("you win")
     print("number of tries:", tries)
     print(f"the number was {num}and you guessed it in {tries} tries")
     break
    else:
     print("you lose") 
     print("number of tries:", tries)
                  