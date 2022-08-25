

# local scope

def local_scope():
	name = 'nanda'
	print(name)

local_scope()

# cant access the name variable, wil get
# NameError: name 'name' is not defined
# print(name)

# global scope

c_name = 'oracle' # global scope accessed from anywhere

print(c_name)

if True:
	print(c_name)
	r_name = 'happy' # this is considered as global because there is no block scope

print(r_name)

# how to modify the global 
# 1. using global key_word
# 2. using the return
# Note: don't try to modify the global variables in the function, that is not good practice

count = 0

def incr_count():
	global count
	count += 1

incr_count()

print(count)

# modifyng the global variables using return statement

friends = 0

def incr_friends():
	print(friends)
	return friends + 1

friends = incr_friends()

print(friends)


# global constants
STOCK_NAME = 'APPLE'

def display():
	print(STOCK_NAME+'nanda')

display()

# Note: In reality, we don't use constants in Python. Naming them in all capital letters is a convention to separate them from variables, however, it does not actually prevent reassignment.