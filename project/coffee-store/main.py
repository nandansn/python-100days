from coffeemachine import CoffeeMachine 

cm = CoffeeMachine()

print("===== Menu ======")

for (k,v) in cm.coffee_menu.items():
    print("{} {}".format(k,v))


user_input = input("​What would you like? (espresso/latte/cappuccino/): ")

cm.make_cofee(user_input)
