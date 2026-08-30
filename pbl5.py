print("*** Online Shopping Cart ***")
print()

cart = []
items = ((101, "Chips", 20.00),
         (102, "Ice cream", 50.00),
         (103, "Pizza", 200.00),
         (104, "Burger", 80.00))

while True:
    print("*** Menu ***")
    print("1. View available products")
    print("2. Add item")
    print("3. Remove item")
    print("4. View cart")
    print("5. Checkout")
    print("6. Exit \n")

    choice = int(input("Enter your choice: \n"))

    if choice == 1:
        print("--- Available Products ---")
        print()
        for i in range(len(items)):
            print("Item ID: ", items[i][0], "Name: ", items[i][1],
                  "Price: ", items[i][2], "\n")

    elif choice == 2:
        for i in range(len(items)):
            print(i+1, ".", items[i][1], "Price:", items[i][2])

        num = int(input("Enter item number to add: "))
        if num >= 1 and num <= len(items):
            cart.append(items[num-1])
            print(items[num-1], "added successfully! \n")

        else:
            print("Invalid item number\n")

    elif choice == 3:
        print("--- Cart items --- \n\n")
        for i in range(len(cart)):
            print(i+1, "-", cart[i])

        num = int(input("\nEnter item number to remove: "))

        if num >= 1 and num <= len(cart):
            remove = cart.pop(num-1)
            print("Removed item: ", remove[0], "\n")

        else:
            print("Invalid item number\n")

    elif choice == 4:
        print("--- Cart --- \n")
        if len(cart) == 0:
            print("Cart is empty \n")

        else:
            for i in range(len(cart)):
                print(i+1, ":", cart[i])

    elif choice == 5:
        print("--- Checkout --- \n")
        if len(cart) == 0:
            print("Cart is empty \n")

        else:
            for i in range(len(cart)):
                print(i+1, ":", cart[i])

            total = 0
            for i in range(len(cart)):
                total += cart[i][2]

            print("Total amount = ", total, "\n")
            ch = input("Do you want to proceed? : yes/no - ")
            if ch == "yes":
                print("Order confirmed \n")
                cart.clear()
            elif ch == "no":
                print("Order cancelled\n")

    elif choice == 6:
        print("Exiting \n")
        break

    else:
        print("Invalid option \n")