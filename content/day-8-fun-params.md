## function params and args
- we can pass args to function params
> def greet(message):
	> print(f"{message}"")
> greet("good morning")

### Positional args vs Keyword args
- postional args no control on the order of the args passed to params, like
> def add(a,b,c):
	> a+b+c
> add(1,2,3) , here a is 1, b is 2 c is 3
- to have a control we  can choose keyword args

> def add(a,b,)
	> a+b+c
> add(c=3,b=2,a=1)