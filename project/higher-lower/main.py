import art
import data
import random

# display the a option
    # generate the random number for a option (0,len of data)
    # display the option
# display the vs logo
# display the b option
    # generate the random number for b option (0,len of data)
    # if the random number equal to a, then generate again
    # else display the b option
# decide who is great and the correponding option
# ask the user for a or b
# check the user option equal to the decided option,
# if same, user winner, proceed to next
# else user lost, display the message and stop the code


# display highvslower logo
print(art.logo)

length_of_data = len(data.data)


def generate_random_number(a):
    while True:
      num = random.randint(0,length_of_data - 1)
      if a == num:
        continue
      else:
        return num

def display_option_details(item): 
    return '{} is an {} from {}'.format(item["name"], item["description"], item["country"])

def who_has_more_followers(a,b):
    if a["follower_count"] > b["follower_count"]:
        return 'A'
    else:
        return 'B'
score = 0
while True:
    a_choice = generate_random_number(-1)
    print('Compare A: {}'.format(display_option_details(data.data[a_choice])))
    print(art.vs)
    b_choice = generate_random_number(a_choice)
    print('Compare B: {}'.format(display_option_details(data.data[b_choice])))
    user_choice = input("Who has more follower count? Type A or B: ")
    if user_choice == who_has_more_followers(data.data[a_choice], data.data[b_choice]):
        score += 1
        continue
    else:
        break

print('Your score is:' , score)
  










