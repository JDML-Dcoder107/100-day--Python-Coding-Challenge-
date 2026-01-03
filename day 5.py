#Day 5 Removing duplicates from sets
print(" Welcome to your order list manager with duplicate removal! ".center(60, "="))
order_list = {"eggs", "milk", "bread", "apples", "bananas", "milk", "bread"}
print("Your current order list (duplicates removed): ", order_list)
ask = input("Would you like to add an item to your order list? (yes/no): ")
while ask.lower() == "yes":
    new_item = input("Enter the item you want to add: ")

    if new_item in order_list:
        print(f"Item {new_item} is already in the order list. Duplicates are not allowed.")
    
    else:
        order_list.add(new_item)
        print(f"Item {new_item} has been added to the order list.")

    ask = input("Would you like to add another item? (yes/no): ")
    if ask.lower() == "no":
        print("=" * 60)
        print("Final order list (duplicates removed): ", order_list)
        break