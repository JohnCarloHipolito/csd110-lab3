def display_prompt():
    print("WELCOME TO THE AMANDO SHOPPING SITE\n")
    print("1. Add product to the cart.")
    print("2. Search the product.")
    print("3. Delete the product from the cart.")
    print("4. Quit.")


def enter_choice():
    return input("\nEnter your choice: ")


def add_product(p):
    count = int(input("Enter the number of items to be added to stationary shop: "))
    new_items = {}

    for _ in range(count):
        if len(p) + len(new_items) == 5:
            print("Cart is full")
            break
        else:
            k = input("Enter an item: ")
            v = input("Enter the brand name: ")
            new_items.update({k: v})

    p.update(new_items)

    print("You added the following items to the cart:")
    for k, v in new_items.items():
        print(f"{k}: {v}")


def search_product(p):
    item = input("Enter the item to be search: ")
    if item in p:
        print(f"{item}: {p[item]}")
    else:
        print("No product exists with this name")


def delete_product(p):
    if len(p) > 0:
        k, v = p.popitem()
        print("You deleted the following item on the cart:")
        print(f"{k}: {v}")
    else:
        print("Cart is empty, no item is found")


# Main flow
display_prompt()
quit_app = False
product = {}
while not quit_app:
    choice = enter_choice()
    if choice == '1':
        add_product(product)
    elif choice == '2':
        search_product(product)
    elif choice == '3':
        delete_product(product)
    elif choice == '4':
        quit_app = True
    else:
        print("Wrong Option Entered.")
