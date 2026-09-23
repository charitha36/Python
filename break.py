shopping_list=["milk","pasta","eggs","spam","bread","rice"]

for item in shopping_list:
    if item=="bread":
        break
    print("buy "+item)

#search
item_to_found="spam"
found_at=None

for index in range(len(shopping_list)):
    if shopping_list[index]==item_to_found:
        found_at=index
print(f"Item is found at position {found_at}")