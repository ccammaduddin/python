#  🍕 Pizza Builder — Challenge Steps
#
# 1. Define a Pizza class that stores:
#    - size, crust type, and a list of toppings
# 2. Add a method to add a new topping
# 3. Add a method to remove a topping if it exists
# 4. Add a method to print pizza details:
#    - size, crust, and all toppings (or “No toppings yet!”)
# 5. Create a pizza object, customize it, and print the summary

class Pizza:
    def __init__(self, size, crust, toppings=None):
        self.size = size
        self.crust = crust
        self.toppings = toppings if toppings else []
        
    def add_topping(self, topping):
        self.toppings.append(topping)
        
    def remove_topping(self, topping):
        if topping in self.toppings:
            self.toppings.remove(topping)
        else:
            print(f"{topping} isn't on your pizza.")
            
    def describe_pizza(self):
        print("\n🍕 ===== Your Pizza ===== 🍕")
        print(f"Size: {self.size.title()}")
        print(f"Crust: {self.crust.title()}")
        if self.toppings:
            print("Toppings: ")
            for topping in self.toppings:
                print(f"  - {topping.title()}")
        else:
            print("No toppings added yet!")
                
                
my_pizza = Pizza("large", "thin")
my_pizza.add_topping("pepperoni")
my_pizza.add_topping("mushrooms")
my_pizza.add_topping("onions")
my_pizza.remove_topping("onions")
my_pizza.describe_pizza()

## second pizza
friend_pizza = Pizza("medium", "deep dish", ["bacon", "extra cheese"])
friend_pizza.add_topping("olives")
friend_pizza.describe_pizza()