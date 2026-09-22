string="Alright,but apart from the Sanitation,the Medicine,Education,Wine,Public Order,Irrigation,Roads,the Fresh-Water System,and Public Health,what have the Romans ever done for us?"
for char in string:
    if char in "QWERTYUIOPASDFGHJKLZXCVBNM":
        print(char)

#another method

string="Alright,but apart from the Sanitation,the Medicine,Education,Wine,Public Order,Irrigation,Roads,the Fresh-Water System,and Public Health,what have the Romans ever done for us?"
for char in string:
    if char.isupper():
        print(char)