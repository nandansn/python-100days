from ast import While

name_list = []
while True:
    name = input("Enter name:")
    if name == "":
        break
    else:
        name_list.append(name)

print(name_list)

