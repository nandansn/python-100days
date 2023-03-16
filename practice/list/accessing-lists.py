fruits_veg = ["apple","banana","carrot","drumstick","grapes"]

## accessing an item
print(fruits_veg[0])

## from the last
print(fruits_veg[-1])

## range from first
print(fruits_veg[:])
print(fruits_veg[1:])
print(fruits_veg[1:3]) # starting till end, not including the end
print(fruits_veg[:3])

## range from last
print(fruits_veg[-1:]) ## from reverse last 1
print(fruits_veg[:-2]) ## till -2 reverse order
print(fruits_veg[-3:-1]) ## pick last 3 and exclude last one

## checking item in the list
if 'apples' in fruits_veg:
	print("item present")
else:
	print("item not present")
