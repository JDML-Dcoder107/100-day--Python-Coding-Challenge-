#Day 9 ATM Simulator
print(" Welcome to the ATM Simulator ".center(60, "="))
balance = 1000  # Initial balance
while True:
    print("\nSelect an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")
    
    match choice:
        case '1':
            print(f"Your current balance is: Php{balance}")
        case '2':
            amount = float(input("Enter the amount to deposit: Php "))
            if amount > 0:
                balance += amount
                print(f"Successfully deposited Php {amount}. New balance is Php {balance}.")
            else:
                print("Invalid amount. Please enter a positive number.")
        case '3':
            amount = float(input("Enter the amount to withdraw: Php"))
            if 0 < amount <= balance:
                balance -= amount
                print(f"Successfully withdrew Php {amount}. New balance is Php {balance}.")
            else:
                print("Invalid amount. Please check your balance and try again.")
        case '4':
            print("Thank you for using the ATM Simulator. Goodbye!")
            break  
        case _:
            print("Invalid choice. Please select a valid option (1-4).\n")
