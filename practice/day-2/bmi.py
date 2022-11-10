weight = float(input('Your weight in kg: '))
height = float(input('Your weight in cm: '))

height = height * 0.01

bmi = weight / (height ** 2)


print(round(bmi,2))