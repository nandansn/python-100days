



def add (a=1,b=2):
    print(a+b)

add()

add(10,20)

add(1,2)

def add(*args):
    print(args)

add(1,2,3,4) # add will refer immediate location, of the methods

def person(**attributes):
    print(attributes)

person(name="nanda")

class Car:
    def __init__(self, **attr):
      self.make = attr.get('make')
      self.model = attr.get('model')
      self.price = attr.get('price')

    def display(self):
        print(self.make, self.model, self.price)

maruti = Car(make='maruti',model='swift',price='6laks')
alto = Car(make='maruti',model='alto')

maruti.display()
alto.display()


