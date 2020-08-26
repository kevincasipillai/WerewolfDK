from Utility import *

number_of_players = number_of_players_func()                                                # Choose number of players and return the value
players = player_names(number_of_players)                                                   # Return list with player names
character_info = characters(number_of_players)
all_characters = character_info[0]
character = character_info[1]
hidden_characters = character_info[2]


# HIDDEN INFORMATION IN-GAME
for i in range(0, number_of_players):
    print(f"{players[i]} is {character[i]}")

print(f"Hidden charachters are {hidden_characters}")
print(f"All characters are {all_characters}")

