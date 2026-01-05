#Day 6 Contact Book with dictionaries
print(" Welcome to your contact book manager! ".center(60, "="))

def display_contacts():
    if contact_book:
        print("Your current contacts:")
        for name, phone in contact_book.items():
            print(f"{name}: {phone}")
    else:
        print("Your contact book is empty.")

contact_book = dict()
ask = input("Would you like to add a contact to your contact book? (yes/no): ")
while ask.lower() == "yes":
    name = input("Enter the contact: ")
    phone_number = input("Enter the 11 digit phone number: ")
    if len(phone_number) != 11 or not phone_number.isdigit():
        print("Invalid phone number. Please enter an 11 digit number.")
    else:
        if name in contact_book:
            print(f"Contact {name} already exists with phone number {contact_book[name]}.")
        else:
            contact_book[name] = phone_number
            print(f"Contact {name} with phone number {phone_number} has been added.")
    ask = input("Would you like to add another contact? (yes/no): ")

    if ask.lower() == "no":
        print("=" * 60)
        print("Final contact book:")
        display_contacts()
        break
