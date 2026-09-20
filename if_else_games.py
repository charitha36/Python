answer=5

print("Please guess a number in between 1 and 10:")
guess=int(input())

if guess!=answer:
    if guess<answer:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guess=int(input())
    if guess==answer:
        print("Well done,you guessed it")
    else:
        print("sorry,you have not guessed correctly")
else:
    print("You got it first time")    

# if guess<answer:
#     print("Please guess higher")
#     guess=int(input())
#     if guess==answer:
#         print("Well done,you guessed it")
#     else:
#         print("please try later")
# elif guess>answer:
#     print("Please guess lower")
#     guess=int(input())
#     if guess==answer:
#         print("Well done,you guessed it")
#     else:
#         print("please try later")
# else:
#     print("You got it!!")