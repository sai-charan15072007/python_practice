stack = []

while True:
    print("\n--- STACK MENU ---")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Size")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter element to push: ")
        stack.append(item)
        print(item, "pushed into stack.")

    elif choice == 2:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            item = stack.pop()
            print(item, "popped from stack.")

    elif choice == 3:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Top element:", stack[-1])

    elif choice == 4:
        if len(stack) == 0:
            print("Stack is empty.")
        else:
            print("Stack:", stack)

    elif choice == 5:
        print("Stack size:", len(stack))

    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")