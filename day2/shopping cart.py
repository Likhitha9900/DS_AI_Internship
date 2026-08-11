cart = []

while True:
    print("\n***** SHOPPING CART *****")
    print("1. Add Fruit")
    print("2. View Cart")
    print("3. Update Fruit")
    print("4. Delete Fruit")
    print("5. Checkout")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        fruit = input("Enter fruit name: ")
        cart.append(fruit)
        print("Fruit added successfully.")

    elif choice == 2:
        print("Shopping Cart:", cart)

    elif choice == 3:
        old = input("Enter fruit to update: ")
        if old in cart:
            new = input("Enter new fruit name: ")
            i = cart.index(old)
            cart[i] = new
            print("Fruit updated successfully.")
        else:
            print("Fruit not found.")

    elif choice == 4:
        fruit = input("Enter fruit to delete: ")
        if fruit in cart:
            cart.remove(fruit)
            print("Fruit deleted successfully.")
        else:
            print("Fruit not found.")

    elif choice == 5:
        print("\nFruits added to cart:")
        for fruit in cart:
            print(fruit)

        print("Total items in shopping cart:", len(cart))

        cart = tuple(cart)
        print("Shopping cart after checkout:", cart)
        break

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")