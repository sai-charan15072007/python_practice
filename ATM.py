print("Welcome! Swipe your card")
print()

balance = 5000

security_pin = input("Set security pin: ")
pin = input("Enter pin: ")

if security_pin == pin:
    while True:
        print("\n1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        num = input("Enter the number from the above services: ")

        if num == "1":
            print("Balance:", balance)

        elif num == "2":
            deposit = float(input("Enter deposit amount: "))

            if deposit > 0:
                balance += deposit
                print("The total balance is:", balance)
            else:
                print("Invalid amount")

        elif num == "3":
            withdraw = float(input("Enter withdrawal amount: "))

            if withdraw <= 0:
                print("Invalid amount")
            elif withdraw > balance:
                print("Insufficient balance")
            else:
                balance -= withdraw
                print("The total balance is:", balance)

        elif num == "4":
            old_pin = input("Enter your current PIN: ")

            if old_pin == pin:
                new_pin = input("Enter the new PIN: ")
                pin = new_pin
                print("PIN changed successfully")
            else:
                print("Incorrect current PIN")

        elif num == "5":
            print("Thank you for using the ATM!")
            break

        else:
            print("Enter a correct number")

else:
    print("Incorrect PIN")
