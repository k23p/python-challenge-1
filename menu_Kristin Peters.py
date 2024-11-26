# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

order_list = []

# this is where the orders will be placed

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    
    # Ask the customer from which menu category they want to order
    print("\nFrom which menu would you like to order? ")
    menu_items = {}
    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
   

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
         # 2. Ask customer to input menu item number
        while True:
            try:
                item_number = int(input("\nWhich item do you want? Enter the number here: "))
               
                if item_number in menu_items:
                    picked_item_number = menu_items[item_number]
                    picked_item_name = picked_item_number["Item name"] #stores the item name
                    picked_item_price = picked_item_number["Price"] #stores the item price
                    print(f"You selected {picked_item_name}. That sounds great.")

                    break
                else: 
                    print("Please enter a valid number.")
            except ValueError:
                print("You've entered an incorrect answer. Please enter a number.")

            # 3. Check if the customer typed a number


                # Convert the menu selection to an integer
        # try:
         #   number = int(picked_item_number)
        #except ValueError:
        #    print("You've made an invalid selection. Please enter a number.")

                # 4. Check if the menu selection is in the menu items
        if item_number in menu_items:
            print("You've entered this correctly!")
        else:
            print(f"You didn't select a valid menu option, please select again.")


                    # Store the item name as a variable
                    #did in line 129

                    # Ask the customer for the quantity of the menu item

        try:
            quantity = int(input(f"How many {picked_item_name}s do you want to order? "))
            
            if quantity <= 0:
                print("Invalid quantity, so we'll default to 1.")
                quantity = 1
        except ValueError:
            print("You've entered an invalid quantity, so we'll default to 1. ")
            quantity = 1
                    # Check if the quantity is a number, default to 1 if not


                    # Add the item name, price, and quantity to the order list
        order_list.append({
            "Item name": picked_item_name,   # The name of the item
            "Price": picked_item_price,      # The price of the item
            "Quantity": quantity             # The quantity ordered
        })

# Confirm the addition to the customer
        print(f"Added {quantity} x {picked_item_name} to your order.")
        break
    else: 
        print("Invalid item number - please select a valid menu option.")



                    # Tell the customer that their input isn't valid


                # Tell the customer they didn't select a menu option
            # Tell the customer they didn't select a menu option
#if menu_category not in menu_items:
   # print(f"{menu_category} was not a menu option.")
#else:
#    try:
#       number = int(input("Please enter a number:"))
#       if number not in menu_items:
#           print("You've made an invalid selection. Please enter a number.")
        # Tell the customer they didn't select a number
#    except ValueError:  
 #       print("You didn't select a number. Please enter a valid number.")


        # Ask the customer if they would like to order anything else
keep_ordering = input("\nWould you like to keep ordering? (Y)es or (N)o ").strip().lower() 
if keep_ordering  in ["n", "no"]:
    place_order = False
elif keep_ordering not in ['y', 'yes', 'Y', 'Yes']:
    print("Your input is not valid. Please enter (y)es or (n)o.")
else: 
    print("You've entered an invalid input. Please enter (y)es or (n)o.")



        # 5. Check the customer's input

                # Keep ordering

                # Exit the keep ordering question loop

                # Complete the order
print("\nHere is a summary of your order:/n")
total_price = 0
for order_item in order_list:
        picked_item_name = order_item["Item name"]
        picked_item_price = order_item["Price"]
        quantity = order_item["Quantity"]

        item_total = picked_item_price * quantity
        total_price += item_total


        print(f"{order_item['Quantity']} x {order_item['Item name']} at ${order_item['Price']:.2f} each")
    

print(f"\nTotal Price: ${total_price:.2f}")

print("Thanks so much for your order. We hope you enjoy!")






                # Since the customer decided to stop ordering, thank them for
                # their order

                # Exit the keep ordering question loop


                # Tell the customer to try again


# Print out the customer's order

print("This is what we are preparing for you.\n")

# Uncomment the following line to check the structure of the order
print(order_item)

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order

    # 7. Store the dictionary items as variables


    # 8. Calculate the number of spaces for formatted printing
name_column_width = 24  # Fixed width for item name column
price_column_width = 8  # Fixed width for price column
quantity_column_width = 8  # Fixed width for quantity column

    # 9. Create space strings

def create_spaces(text, column_width):
    return " " * (column_width - len(text))

    # 10. Print the item name, price, and quantity

print(f"{'Item Name':<{name_column_width}}{'Quantity':>{quantity_column_width}}{'Price':>{price_column_width}}{'Total':>10}")
print("-" * (name_column_width + quantity_column_width + price_column_width + 10))

for order_item in order_list:
    item_name = order_item["Item name"]
    item_price = order_item["Price"]
    item_quantity = order_item["Quantity"]
    item_total = item_price * item_quantity

item_name_spaces = create_spaces(item_name, name_column_width)
quantity_spaces = create_spaces(str(item_quantity), quantity_column_width)
price_spaces = create_spaces(f"${item_price:.2f}", price_column_width)

print(f"{item_name}{item_name_spaces}{item_quantity}{quantity_spaces}${item_price:.2f}{price_spaces}${item_total:.2f}")


# 11. Calculate the cost of the order using list comprehension
total_price = sum(order_item["Price"] * order_item["Quantity"] for order_item in order_list)

print("-" * (name_column_width + quantity_column_width + price_column_width + 10))
print(f"{'Total':<{name_column_width}}{'':>{quantity_column_width + price_column_width}}${total_price:.2f}")


# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.
