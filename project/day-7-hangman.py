## Hangman Program
import random

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/     
''')

hang_man_art = '''
      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \
     |
 jgs_|___
'''

words_repo = ["apple", "banana", "grapes"]

index = random.randint(0, len(words_repo) - 1)

word_to_guess = words_repo[index]

#print(word_to_guess)


def calculate_life():
    letter_count_map = {}
    for letter in word_to_guess:
        letter_count_map[letter] = 1
    return len(letter_count_map)


total_life = calculate_life() + 2

print(f"your chances {total_life}")


def replace_blank():
    guessed_word = []
    for letter in word_to_guess:
        guessed_word.append('_')
    return guessed_word


guessed_word = replace_blank()

print("".join(guessed_word))


def diaplay_hangman(c):
    total_len = len(hang_man_art) // total_life
    print(hang_man_art[0:total_len * c + 8])


chance = 1
for num in range(0, total_life):
    if "".join(guessed_word) == word_to_guess:
        break
    else:
        user_guess = input("Your guess: ")
        if user_guess in word_to_guess and '_' in guessed_word:
            i = 0
            for l in word_to_guess:
                if user_guess == word_to_guess[i]:
                    guessed_word[i] = user_guess
                    print("".join(guessed_word))
                i = i + 1
        else:
            print("".join(guessed_word))
            diaplay_hangman(chance)
            chance += 1

final_word = "".join(guessed_word)

if "_" in final_word:
    print(f"You lose {final_word}")
else:
    print(f"You win {final_word}")
