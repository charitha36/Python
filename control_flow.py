name=input("Please enter your name:")
age=int(input("How old are you,{0}? ".format(name)))
print(f"Hello {name},your age is {age}")

if 18<=age<100:
    print("You are eligible to vote")
elif age>=100:
    print("Sorry,you enter the wrong age")
else:
    print(f"you are eligible to vote after {18-age} years")