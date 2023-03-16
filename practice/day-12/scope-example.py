count = 1

def change_count(num):
    count = num
    print(f"count inside {count}")

change_count(11)
print(f"count outside {count}")


if 1 < 2:
    name="nanda" # global variable

def test_block_var():
    print(name)

print(name)

test_block_var()

friends = 0

def increase_friends():
    global friends
    friends += 1
    print(f"friends {friends}")

increase_friends()
print(friends)