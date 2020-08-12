from random import shuffle

def shuffle_cups(game_list):
	shuffle(game_list)
	return(game_list)

def player_guess():
	guess = ""

	while guess not in ["0", "1", "2"]:
		guess = input("Pick a number. 0, 1, or 2.")

	return int(guess)

def check_guess(game_list,guess):
	if(game_list[guess] == "O"):
		print("Correct!")
		print(game_list)
	else:
		print(f"Incorrect. The ball was not at {guess}")
		print(game_list)

def three_cup_monte():
	cups = [" ", "O", ""]

	mixed_cups = shuffle_cups(cups)

	guess = player_guess()

	check_guess(mixed_cups,guess)

three_cup_monte()