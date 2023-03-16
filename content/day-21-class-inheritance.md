## class inheritance

- we can inherit parent attributes and methods
- The call to super() in the initialiser is recommended, but not strictly required.
> class Dog(Animal):
>   def __init__():
>       super().__init__()

- we can override the parent methods by the child class methods

## Notes:
- there is no interface concept in python
- we can declare the abstract method using the decorator
- refer this (https://www.godaddy.com/engineering/2018/12/20/python-metaclasses/#:~:text=Unfortunately%2C%20Python%20doesn't%20have,in%20order%20to%20be%20initialized.)

## Slice Lists

- names = ['a','b','c','d']
- names[2:5:1]

[Ref] (https://www.geeksforgeeks.org/python-lists/)

## Slice tuples

    - tup1 = ('physics', 'chemistry', 1997, 2000);
    - tup2 = (1, 2, 3, 4, 5, 6, 7 );
    - print "tup1[0]: ", tup1[0];
    - print "tup2[1:5]: ", tup2[1:5];

    - output:
        tup1[0]:  physics
        tup2[1:5]:  [2, 3, 4, 5]

    - delete tuple:
    del tup;


    [Ref] (https://www.tutorialspoint.com/python/python_tuples.htm)
