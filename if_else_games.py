import random
answer=random.randint(1,10)
guess=0
print("Please guess a number in between 1 and 10:")
guess=int(input())
while(guess!=answer): 
    if guess<answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess=int(input())
if guess==answer:
    print("Well done,you guessed it")