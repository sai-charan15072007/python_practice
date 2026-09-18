contact = []


def add_contact(number):
    contact.append(number)


def search_contact(number):
    for i in range(len(contact)):
        if contact[i] == number:
            print("Number found at position", i)
            return

    print("Number not found")


def update_contact(idx, number):
    if 0 <= idx < len(contact):
        contact[idx] = number
        print("Contact updated successfully")
    else:
        print("Invalid index")


def delete_contact(number):
    if number in contact:
        contact.remove(number)
        print("Contact deleted successfully")
    else:
        print("Number not found")


def Display():
    if len(contact) == 0:
        print("No contacts found")
    else:
        for i in range(len(contact)):
            print(i, contact[i])


while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Update contact")
    print("4. Delete contact")
    print("5. Display all contacts")
    print("6. Exit")

    choice = int(input("Enter your choice from above list: "))

    if choice == 1:
        num = input("Enter number: ")
        add_contact(num)

    elif choice == 2:
        num = input("Enter number to search: ")
        search_contact(num)

    elif choice == 3:
        idx = int(input("Enter index: "))
        num = input("Enter new number: ")
        update_contact(idx, num)

    elif choice == 4:
        num = input("Enter number to delete: ")
        delete_contact(num)

    elif choice == 5:
        Display()

    elif choice == 6:
        print("Thank you")
        break

    else:
        print("Enter correct choice")