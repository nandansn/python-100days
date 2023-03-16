# creating empty dictionary
computer_dictionary = {}

## adding an item to the dictionary
computer_dictionary["bug"] = "an unexpceted result"
computer_dictionary["server"] = "computer that serves the requested resource"

## access the item in the dictionary
print(computer_dictionary["bug"])

## edit the item in the dictionary
computer_dictionary["bug"] = "a process failure"

## loop the dictionary
for key in computer_dictionary:
	print(computer_dictionary[key])

## empty the dictionary
computer_dictionary = {}

print(computer_dictionary)
