# Hej med dig, dette er en utility script 

import random

def number_of_players_func():
    number_of_players = int(input("Enter Number of players: "))
    if number_of_players <= 2 or number_of_players >= 12:              # minimum 3 players and max 12 players
        number_of_players_func()
    else:
        print(f"{str(number_of_players)} player(s) joined the game!")
        print(" ")
        print(" ")
        return number_of_players


def player_names(x_players):                                            # x_players is number of players from prev func
    player_list = []
    for i in range(0, x_players):
        name = input(f"Enter player {str(i+1)}'s name: ").capitalize()
        player_list.append(name)
    return player_list


def characters(x_players):
    character_list = ["Doppelgänger",
                      "Werewolf",
                      "Werewolf",
                      "Minion",
                      "Mason",
                      "Mason",
                      "Seer",
                      "Robber",
                      "Troublemaker",
                      "Drunk",
                      "Insomniac",
                      "Hunter",
                      "Tanner",
                      "Villager",
                      "Villager",
                      "Villager"]
    number_of_characters = x_players+4                                                      # the number of players + 4 additional characters
    choose_characters_for_game = []
    character_num = int(input(f"""
Choose {str(number_of_characters)} different characters. Hit return after each choice!

1.  Doppelgänger
2.  Werewolf
3.  Werewolf
4.  Minion
5.  Mason
6.  Mason
7.  Seer
8.  Robber
9.  Troublemaker
10. Drunk
11. Insomniac
12. Hunter
13. Tanner
14. Villager
15. Villager
16. Villager

First character: """))

    choose_characters_for_game.append(character_num)

    for i in range(0, number_of_characters-1):
        character_num = int(input("Next character: "))
        choose_characters_for_game.append(character_num)

    chosen_characters = [character_list[i] for i in choose_characters_for_game] # characters chosen to play with
    random_character = random.sample(range(0, number_of_characters), x_players)
    characters = [chosen_characters[i] for i in random_character]
    # hidden_characters = [random_character[i] for i not in chosen_characters] # Find hidden characters

    return characters, chosen_characters

