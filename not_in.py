activity=input("What would you like to do today?")

if "cinema" not in activity.casefold():#casefold() is used to make it case insensitive
    print("But i want to go to cinema")

#capitalize()=>return a copy of string with its first character capitalized and the rest lowercased
#casefold()=>return a casefolded copy of the string.Casefolded strings may be used for caseless matching