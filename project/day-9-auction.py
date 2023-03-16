# In a loop
# get user name
# get bid amouont
# store the name as key and bid amount as value in the dict
# if any other user? yes continue else break the loop
# iterate the dict and get the large amount and the name, announce the winner

# Display the auction logo

from replit import clear

logo = '''

                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                      /_______________\


'''

auction_map = {}


def display_logo():
    print(logo)


def do_bidding():

    while True:
        display_logo()
        bidder_name = input("enter name: ")
        bidder_amount = int(input("enter bid amount: "))

        any_more_bidder = input("any more bidder? yes or no: ")

        auction_map[bidder_name] = bidder_amount

        if any_more_bidder == 'yes':
            clear()
            continue
        else:
            break


def who_is_winner():
	winning_amount = -1
	winner_name = ""
	
	for entry in auction_map:
		if winning_amount < 0:
			winning_amount = auction_map[entry]
			winner_name = entry
		else:
			if (winning_amount < auction_map[entry]):
				winning_amount = auction_map[entry]
				winner_name = entry

	return { winner_name: winning_amount }


clear()
do_bidding()
auc_winner = who_is_winner()

print(f"winner is {auc_winner}")
