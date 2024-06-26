import random  

class ATM:
    def create_account(user, accounts):
        user_id = random.randint(1000, 9999)
        pin = input("Enter your 3-digit PIN: ")

        while not (pin.isdigit() and len(pin) == 3):
            print("Error: PIN must be a 3-digit number.")
            pin = input("Enter your 3-digit PIN: ")

        pin = int(pin)  
        accounts[user_id] = {
            'balance': 0,
            'pin': pin
        }
        print(f"Your Account has been Created Successfully. User ID is: {user_id}")

    def balance(user, accounts, user_id, pin):
        if user_id in accounts and accounts[user_id]['pin'] == pin:
            print(f"Balance for User ID {user_id}: ₱{accounts[user_id]['balance']:.2f}")
        else:
            print("Error: Invalid User ID or PIN.")

    def deposit(user, accounts, user_id, pin, amount):
        amount = float(amount)  
        if user_id in accounts and accounts[user_id]['pin'] == pin and amount > 0:
            accounts[user_id]['balance'] += amount  
            print(f"Deposited ₱{amount:.2f} successfully.")
            user.balance(accounts, user_id, pin)  
        else:
            print("Error: Invalid User ID, PIN, or deposit amount must be greater than zero.")

    def withdraw(user, accounts, user_id, pin, amount):
        amount = float(amount) 
        if user_id in accounts and accounts[user_id]['pin'] == pin and amount > 0:
            if accounts[user_id]['balance'] >= amount: 
                accounts[user_id]['balance'] -= amount  
                print(f"Withdrawn ₱{amount:.2f} successfully.")
                user.balance(accounts, user_id, pin)  
            else:
                print("Error: Insufficient balance.")
        else:
            print("Error: Invalid User ID, PIN, or withdrawal amount must be greater than zero.")

    def delete_account(user, accounts, user_id, pin):
        if user_id in accounts and accounts[user_id]['pin'] == pin:
            del accounts[user_id]  
            print(f"Account with User ID {user_id} deleted successfully.")
        else:
            print("Error: Invalid User ID or PIN.")


def atm_interaction():
    accounts = {} 
    atm = ATM()  

    while True:
        print("\nScam Machine :)")
        print("1. Create Account")
        print("2. Check Balance")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Delete Account")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1' or choice == "create":
            atm.create_account(accounts)
        elif choice in ['2', '3', '4', '5']:
            try:
                user_id = int(input("Enter User ID: "))
                pin = input("Enter 3-digit PIN: ")

                if pin.isdigit() and len(pin) == 3:
                    pin = int(pin)
                    if choice == '2' or choice == "balance":
                        atm.balance(accounts, user_id, pin)
                    elif choice == '3' or choice == "deposit":
                        amount = float(input("Enter deposit amount: "))
                        atm.deposit(accounts, user_id, pin, amount)
                    elif choice == '4' or choice == "withdraw":
                        amount = float(input("Enter withdrawal amount: "))
                        atm.withdraw(accounts, user_id, pin, amount)
                    elif choice == '5' or choice == "delete":
                        atm.delete_account(accounts, user_id, pin)
                else:
                    print("Error: PIN must be a 3-digit number.")
            except ValueError:
                print("Error: User ID must be an integer.")
        elif choice == '6':
            print("Exiting the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Make sure you enter a number from 1 to 6.")

atm_interaction()
