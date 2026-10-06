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











def greet(name):
    print(f"Hello, {name}. Welcome to {cafe_name}.")

name = input("What is your name? ")
greet(name)

def show_menu(menu):
    print("")