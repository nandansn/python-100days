## functions
- user defined functions
- built-in functions

### defining and calling the function

- defining

> def my_function():
	> print('welcome')
- calling
  > my_function()
  >

## Indentation

- shifted to 4 spaces
- official python guide says to use spaces

[Ref] (https://peps.python.org/pep-0008/#indentation)

## while loop

> while (condition) :
> 
	> statement


### Note

- Python does not have built-in functionality to explicitly create a do while loop like other languages. But it is possible to emulate a do while loop in Python.

**How to emulate a do while loop in Python?**

> secret_word = "python"
> counter = 0

> while True:
>    word = input("Enter the secret word: ").lower()
>    counter = counter + 1
>    if word == secret_word:
>        break
>    if word != secret_word and counter > 7: 
>        break