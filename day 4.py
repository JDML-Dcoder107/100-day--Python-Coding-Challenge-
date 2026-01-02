#Day 4 Shopping list using list
print(" Welcome to your shopping list manager! ".center(50, "="))
shopping_list = ["eggs", "milk", "bread", "apples", "bananas"]
print("Your current shopping list: ", shopping_list)
ask = input("Would you like to add an item to your shopping list? (yes/no): ")

while ask.lower() == "yes":
    shopping_list.append(input("Enter the item you want to add: "))
    print(f"Item {shopping_list[-1]} has been added to the shopping list.")
    ask = input("Would you like to add another item? (yes/no): ")
    if ask.lower() == "no":
        print("=" * 50)
        print("Final shopping list: ", shopping_list)
        break
