import random

rock = '''
Rock
          _______
      ---'   ____)
            (_____)
            (_____)
    VK      (____)
      ---.__(___)

'''

paper = '''
 Paper
          _______
      ---'   ____)____
                ______)
                _______)
    VK         _______)
      ---.__________)
'''

scissors = '''
 Scissors
          _______
      ---'   ____)____
                ______)
             __________)
    VK      (____)
      ---.__(___)
'''

list_of_signs = [rock, paper, scissors]

# Rules
# Rock win against scissors
# Scissors win against paper
# Paper win against rock

user_choice = int(
    input(
        'What do you want to choose? 0 for Rock, 1 for Papre, 2 for Scissors: '
    ))

computer_choice = random.randint(0, 2)

print(f"User choice is:  \n {list_of_signs[user_choice]}")

print(f"Computer choice is : \n {list_of_signs[computer_choice]}")

if user_choice == computer_choice:
    print('Play again')
else:
    if user_choice == 0 and computer_choice == 2:
        print('You win')
    elif user_choice == 2 and computer_choice == 1:
        print('You win')
    elif user_choice == 1 and computer_choice == 0:
        print('You win')
    else:
        print('You lose')
