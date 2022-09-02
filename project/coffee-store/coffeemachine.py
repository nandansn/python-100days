from resources import Resources

class CoffeeMachine:
    def __init__(self):
      self.resources = Resources(400, 400, 300, 10)
      self.coffee_mix = {
        'espresso': {
          'water' : 200,
          'milk' : 100,
          'coffee' : 40
        },
        'cappuccino': {
          'water' : 200,
          'milk' : 200,
          'coffee' : 50
        },
        'latte': {
          'water' : 200,
          'milk' : 150,
          'coffee' : 60
        }
      }
      self.coffee_menu = { 'latte' : '$10' , 'cappuccino' : '$15' , 'espresso' : '$17' }
      
    def make_cofee(self, user_input):
        coffee_type = self.coffee_mix[user_input]
        if self.resources.check_resources(coffee_type["water"],coffee_type["milk"],coffee_type["coffee"]):
            print("Resources available")
