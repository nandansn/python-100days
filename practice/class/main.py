class MyClass:
  pass


user = MyClass()
user.name = 'nanda'
user.age = 42

print(user.name)


class Car:
   def __init__(self, color, model):
    self.color = color
    self.model = model

   def displayDetails(self):
    print(self.color, self.model)




tata = Car('Red','Nexon')

tata.displayDetails()

print(tata.color)