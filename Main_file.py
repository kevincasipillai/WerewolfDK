from Utility import *

number_of_players = number_of_players_func()                                                # Choose number of players and return the value
players = player_names(number_of_players)                                                   # Return list with player names
character_info = characters(number_of_players)
character = character_info[0]
all_characters = character_info[1]
#hidden_characters = character_info[2]


# HIDDEN INFORMATION IN-GAME
for i in range(0, number_of_players):
    print(f"{players[i]} is {character[i]}")

print(f"All characters are {all_characters}")

# Find out how to just find hidden characters which are the four lying on the table