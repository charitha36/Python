# i=0
# while i<10:
#     print(i)
#     i+=1

directions=["north","south","east","west"]

chosen=""
while chosen not in directions:
    chosen=input("Please choose a direction:")

    if chosen.casefold()=="quit":
        print("Game over")
        break
else:
    print("aren't you glad you out of there")