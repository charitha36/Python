low=1
high=1000
print(f"Please think of a number between {low} ,{high} ")
input("Press ENTER to start")

guesses=1
while low!=high:
    #print(f"\t Guessing in the range of {low} to {high}")
    guess=low+(high-low)//2
    high_low=input(f"My guess is {guess}.should I guess higher or lower?Enter h or l,or c if my guess was correct.").casefold()

    if high_low=="h":
        #Guess higher.The low end of the range becomes 1 greater than the guess.
        low=guess+1
        #pass   #make code syntactically correct if we didn't write anything after if statement
    elif high_low=="l":
        #Guess lower.The high end of the range becomes one less than the guess.
        #pass
        high=guess-1
    elif high_low=="c":
        print(f"I got in {guesses} guesses")
        break
    else:
        print("Please enter h,l or c")
    guesses=guesses+1
    #in augmented assignment we write this in guesses+=1 and it means assigning the variables in a shortcut way

else:
    print(f"You thought the number{low}")
    print(f"I got it in {guesses} guesses")