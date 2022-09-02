class Resources:
    def __init__(self, water, milk, coffee, money):
      self.water = water
      self.milk = milk
      self.coffee = coffee
      self.money = money
    
    def set_resource(self, water, milk, coffee, money):
        self.water = water
        self.milk = milk
        self.coffee = coffee
        self.money = money

    def check_resources(self, water, milk, coffee):
        if self.water < water:
            print("​Sorry there is not enough water.")
            return False
        if self.milk < milk:
            print("Sorry there is not enough milk.")
            return False
        if self.coffee < coffee:
            print("Sorry there is not enough coffee.")
            return False
        return True

        
        
