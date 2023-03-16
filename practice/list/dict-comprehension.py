data = {
    'person':'nanda',
    'age':40,
    'city':'erode'
}

new_data = {key:value for (key,value) in data.items() }

print(new_data)


new_number_dict = {num: num ** 2 for num in range(1, 11) if num % 2 == 0 }

print(new_number_dict)