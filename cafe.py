


cafe_name = "Sammy's Cafe"
tax_rate = 0.08

menu = {
    "coffee": 10.00,
    "tea": 7.50,
    "sandwich": 20.00,
    "bacon, egg, and cheese": 15.00,
    "t-shirt": 60.00,
    "mug": 17.50,


}



def show_menu(menu):
        print("Here is Sammy's Cafe's menu:")
        for product, price in menu.items():
            print(f"{product}: ${price:.2f}")







def greet(name):
    print(f"Hello, {name}. Welcome to {cafe_name}.")

name = input("What is your name? ")
greet(name)

is_member = input("Are you a member? ")
if is_member.lower() == "yes":
    print("Thank you for being a member.")

while True:
    options = input("""Choose one of the following:  
          1. View menu. 
          2. Add an item. 
          3. Remove an item. 
          4. View my order. 
          5. Checkout.""" 
          )  
    
    if options == "1":
         show_menu(menu)
    elif options == "2":
         