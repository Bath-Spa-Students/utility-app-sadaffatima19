import time

print()
print ("Welcome to Sadaf's Wending Machine!")
print("What would you like to buy today?")
print()

time.sleep(2) #Delaying the menu by 2 seconds

# define a dictionary of product information
items = {

    "Chocolates" : {
        "A" : {"name" : "KitKat", "price": 1.50, "stock" : 20},
        "B" : {"name" : "Galaxy", "price": 2.00, "stock" : 20},
        "C" : {"name" : "Diary Milk", "price": 2.50, "stock" : 20},
        "D" : {"name" : "Twix", "price": 2.00, "stock" : 20},
        "E" : {"name" : "Snickers", "price": 2.00, "Stock" : 20}
    },

    "Fizzy Drinks" : {
        "F" : {"name" : "Pepsi", "price": 7.00, "stock" : 20},
        "G" : {"name" : "Coca Cola", "price": 8.00, "stock" : 20},
        "H" : {"name" : "Sprite", "price": 6.00, "stock" : 20},
        "I" : {"name" : "Fanta", "price": 5.50, "stock" : 20},
        "J" : {"name" : "Diet Cola", "price": 8.50, "stock" : 20}
    },

    "Juices" : {
        "K" : {"name" : "Mango Juice", "price": 2.00, "stock" : 20},
        "L" : {"name" : "Orange Juice", "price": 2.00, "stock" : 20},
        "M" : {"name" : "Chocolate Milk", "price": 2.50, "stock" : 20},
        "N" : {"name" : "Fruit Cocktail Juice", "price": 2.00, "stock" : 20},
        "O" : {"name" : "Apple Juice", "price": 2.00, "stock" : 20}
    },

    "Chips" : {
        "P" : {"name" : "Chilli Lays", "price": 2.00, "stock" : 20},
        "Q" : {"name" : "Dorritos", "price": 2.00, "stock" : 20},
        "R" : {"name" : "Original Pringles", "price": 5.00, "stock" : 20},
        "S" : {"name" : "Salad Chips", "price": 2.00, "stock" : 20},
        "T" : {"name" : "Cheetos", "price": 2.00, "stock" : 20}
    },

    "Snacks" : {
        "U" : {"name" : "Cheese Croissant", "price": 10.00, "stock" : 20},
        "V" : {"name" : "Chocolate Croissant", "price": 10.00, "stock" : 20},
        "W" : {"name" : "Chicken Sandwich", "price": 14.00, "stock" : 20},
        "X" : {"name" : "Vegetable Sandwich", "price": 13.50, "stock" : 1},
        "Y" : {"name" : "Tuna Sandwich", "price": 10.00, "stock" : 20},
        "Z" : {"name" : "Egg Sandwich", "price": 12.00, "stock" : 20}
    },

    "Cakes" : {
        "A1" : {"name" : "Chocolate Cake", "price": 5.00, "stock" : 20},
        "B1" : {"name" : "Brownie", "price": 5.00, "stock" : 20},
        "C1" : {"name" : "Vanilla Cake", "price": 5.00, "stock" : 20},
        "D1" : {"name" : "Fruit Cake", "price": 5.00, "stock" : 20},
        "E1" : {"name" : "Red Velvet Cake", "price": 6.00, "stock" : 20}
    }
}

# defining a function to print the menu
def print_menu(items):
    print("CHECK OUT OUR MENU:\n")
    for category, category_items in items.items():
        print(category + ":")
        for code, item in category_items.items():
            print(f'{code}: {item["name"]} ({item["price"]:.2f} dhs)')
        print()
        print("\n-------------------------------------------------")
        print()

#function to get item code from user
def get_code(items):
    while True:
        code = input("Enter the item code: ").upper() #This converts the item into uppercase
        for category, category_items in items.items():
            if code in category_items:
                return code
        print("Invalid Code! Please try again with a different code.")

#function to get purchase money from the userd
def get_money(items, code):
    for category, category_items in items.items():
        if code in category_items:
            item = category_items[code]
            break
    else:
        print(f"Invalid Code! '{code}'.")
        return
    while True:
        money = float(input("Enter the amount of money: "))
        if money >= item["price"]:
            return money
        print(f"The money is not enough. Please insert {item["price"] - money:.2f} dhs more.")

#function to dispense the product and count change
def dispense_item(items, code, money):
    for category, category_items in items.items():
        if code in category_items:
            item = category_items[code]
            break
    else:
        print(f"Invalid code '{code}'.")
        return
    
    if item["stock"] > 0:
        print(f"\nDispensing {item['name']}...")
        change = money - item["price"]
        item["stock"]-=1
        print(f"Returning {change:.2f}dhs change...\n")
    else:
        print(f"\nError: {item["name"]} is out of stock.")

#function to suggest another purchase
def additional_purchase(items, code):
    if code in items["Fizzy Drinks"]:
        print("You might also like: ")
        for code, item in items["Snacks"].items():
            print(f"{code}: {item["name"]} ({item["price"]:.2f}dhs)")
    elif code in items["Snacks"]:
        print("You might also like:")
        for code, item in items["Fizzy Drinks"].items():
            print(f"{code}: {item["name"]} ({item["price"]:.2f}dhs)")

#Code that displays the Vending machine 
while True:
    print_menu(items)
    code = get_code(items)
    money = get_money(items, code)
    dispense_item(items, code, money)
    additional_purchase(items, code)
    while True:
        option = input("\nDo you want to make another purchase? (yes/no): ")
        if option.lower() == "yes":
            break
        elif option.lower() == "no":
            print("-------------------------------------------------")
            print("Thank You for using Sadaf's vending machine!")
            print("-------------------------------------------------")
            exit()
        else:
            print("You have entered an invalid option. Please try again!")
