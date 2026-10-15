
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

order = []

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

def discount(subtotal, is_member):
     if is_member.lower() == "yes":
        return subtotal 

def add_item(order,item):
     item = input("What would you like today? ")
     if item in menu:
          order.append(item)
          print(f"{item} is added to your order.")
     else:
          print(f"We don't have {item}. ")

#def print_receipt(name, order, menu, is_member):
#     subtotal = sum(menu[item] for item in order)
#     print(f"Subtotal: ${subtotal}")
#     if is_member.lower() == "yes":
#          dicount_amount = subtotal * 0.1
#          subtotal - dicount_amout = total
#          print(f"Discount: -${dicount_amount}")




item = ""



while True:
    options = input("""Choose one of the following:  
          1. View menu. 
          2. Add an item. 
          3. Remove an item. 
          4. View my order. 
          5. Checkout.
          
          
          """ 
          )  
    
    if options == "1":
         show_menu(menu)
    elif options == "2":
         add_item(order, item)
    elif options == "3":
         item = input("Which item do you want to remove? ")
         if item in order:
              order.remove(item)
              print(f"{item} was removed from your order.")
         else: 
              print(f"{item} is not in your order.")
    elif options == "4":
         if order:
              print("Your order is: ")
              for item in order:
                   print(f"{item}: ${menu[item]}")
#    elif options == "5":
         
         