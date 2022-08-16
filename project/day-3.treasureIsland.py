print('''
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
                                                                 
''')

print('Welcome to treasue island, your mission is to find the treasure')

left_or_right = input("Want to go left or right ? ").lower()

if (left_or_right == "right"):
    print('game over')
else:
    swim_or_wait = input("Want to swim or wait ? ").lower()
    if (swim_or_wait == "swim"):
        print("game over")
    else:
        which_door = input(
            "Which door you want to enter? Red, Blue or Yellow ? ").lower()
        if which_door == "red" or which_door == "blue":
            print("game over")
        else:
            print("you win")
