# pre-req
# ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen and king

# display you want to play the game y or n
# if y enter into the game
# 
# else, exit the game


# Rules,
# if the cards in your hand adds up more than 21, its called bust then you are lose
# J, Q, K each count 10
# A is 1 or 11
# if dealer and your score is same then it is draw
# if the dealer score less than 17 then dealer has to take another card

import random
import art as art

cards = [11,2,3,4,5,6,7,8,9,10,10,10]
user_cards = []
dealer_cards = []


print(art.logo)

def random_card():
    return random.randint(0,len(cards) - 1)


def draw_cards():
    pass

def sum_of_cards(cards):
    sum = 0
    for c in cards:
        sum = sum + c

    if sum > 21:
        if 11 in cards:
            sum = sum - 10
    
    return sum


user_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")


def display_result():
    user_sum = sum_of_cards(user_cards)
    dealer_sum = sum_of_cards(dealer_cards)
    if user_sum == dealer_sum:
        print('Draw')
    elif user_sum > 21:
        print('Dealer wins. You went over')
    elif dealer_sum > 21:
        print('You win. Dealer went over')
    elif user_sum == 21 or user_sum > dealer_sum:
        print('User win')
    else:
        print('Dealer wins')
    

while True:
   

    if user_input == 'n':
        if sum_of_cards(user_cards) == sum_of_cards(dealer_cards):
            print('Draw')
        else:
            user_total = sum_of_cards(user_cards)
            dealer_total = sum_of_cards(dealer_cards)

            if user_total > dealer_total and user_total <= 21:
                print('You win')
            else:
                print('Dealer win')
        break
    elif len(user_cards) == 0:
        user_cards.append(cards[random_card()])
        user_cards.append(cards[random_card()])
        user_total = sum_of_cards(user_cards)
        print('your cards: {}, current score is: {}'.format(user_cards, user_total))
        dealer_cards.append(cards[random_card()])
        dealer_total = sum_of_cards(dealer_cards)
        print('Computer\'s first card: {}'.format(dealer_cards))
        
    else:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == 'y':
            user_cards.append(cards[random_card()])
            print('your cards: {}, current score is: {}'.format(user_cards, sum_of_cards(user_cards)))
            while True:
              dealer_cards.append(cards[random_card()])
              if (sum_of_cards(dealer_cards)) < 17:
                continue
              else:
                break
            print('Computer\'s card: {} current score {}'.format(dealer_cards, sum_of_cards(dealer_cards)))         
        else:
            display_result()
            break


    


