import random

print("Welcome to the password generator")
letters = input("How many letters you like in your password?\n")
symbols = input("How many symbols would you like?\n")
numbers = input("How many number would you like?\n")

letters_cnt = int(letters)
symbols_cnt = int(symbols)
numbers_cnt = int(numbers)

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
uppercase = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
symbols = ['!', '@', '#', '$', '%', '*', '&']

password_chars = []

for i in range(0, letters_cnt, 2):
    uIndex = random.randint(0, 25)
    lIndex = random.randint(0, 25)
    password_chars.append(uppercase[uIndex])
    password_chars.append(lowercase[lIndex])

for i in range(0, symbols_cnt):
    sIndex = random.randint(0, len(symbols) - 1)
    password_chars.append(symbols[sIndex])

for i in range(0, numbers_cnt):
    dIndex = random.randint(0, len(digits) - 1)
    password_chars.append(digits[dIndex])

password = ""
len_password = len(password_chars)
for i in range(0, len(password_chars)):
    index = random.randint(0, len_password - 1)
    password = password + password_chars.pop(index)
    len_password -= 1

print(password)
