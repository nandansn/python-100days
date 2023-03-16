fruits = ['apple', 'orange', 'pears']

for fruit in fruits:
    i = fruits.index(fruit, 0, len(fruits))
    print(f"{fruit} at {i}")

total = 0
for num in range(1, 101):
    total = total + num

print(total)
