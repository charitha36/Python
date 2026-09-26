choice="-"
while choice!=0:
    if choice in "12345":
        print(f"You chose {choice}")
    else:
        print("Please choose your option from the list below:")
        print("1:\t Python")
        print("2:\t Java")
        print("3:\t SQL")
        print("4:\t C")
        print("5:\t R")
        print("0:\t Exit")
    choice=input()
