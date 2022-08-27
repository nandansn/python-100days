## How to create the class?

> class Car:
>   pass # paas is used to temporary todo comment,

### Naming in python
- PascalCase => CarModel, starting letter of the word is caps, used for class naming
- camelCase => starting letter of the first word is small, camelCase, 
- snake_case => words are seperated by _

### how to build an object?

> tata = Car()

### Attributes

- instance variables in the class
- adding attributes without the constructor

> tata.model = 'nexon'
> tata.price = 1000000

### Constructor

- is a intializer, to set the starting values at the beginng of the program

- __init__(self) function to create the object, **self** is like **this**, we need to pass self to constructor and other methods
- how to add attibutes?
> def __init__(self,seats):
    > self.seats = seats

### Adding methods to a class

> def carMove(self)
