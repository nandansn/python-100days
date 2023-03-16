import random

num = random.randint(100,1000)

print(num)


for _ in range(100):
    float_num = random.random()
    print(float_num * 5)

names = ['nan','san','niv']
cars = ['bmw','audi','vw']

print(names[0], cars[1])

for i in names:
    print(i)

print(names+cars)

ages = [10,20,25,45,30,18,17,6]

def age_filter(age):
    if age < 18:
        return False
    else:
        return True

filtered_ages = filter(age_filter, ages)

print(filtered_ages)

for age in filtered_ages:
    print(age)

#add item to the list
names.append('abc')

print(names)

#delete item from the list
names.pop()

print(names)

names.remove('nan')

print(names)

print(names+cars)


names_iter = iter(names)
x = next(names_iter)

print(x)
print(next(names_iter))