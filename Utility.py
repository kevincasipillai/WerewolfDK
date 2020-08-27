import random
import numpy as np
import smtplib
import email
import time 
import os 

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
    choosen_characters_for_game = []
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

    while character_num > 16 or character_num < 1:      # Making sure the first charachter is a valid number
        print(" ")
        print("Invalid character!")
        character_num = int(input("Choose another character: "))

    choosen_characters_for_game.append(character_num)
    print(" ")

    for i in range(0, number_of_characters-1):          # Choose the rest of the charachters and making sure the chose charachters are not repeated or invalid (outside 1-16)
        character_num = int(input("Next character: "))
        while character_num in choosen_characters_for_game or character_num > 16 or character_num < 1:
            print(" ")
            print("Invalid character or character is already chosen!")
            character_num = int(input("Choose another character: "))

        choosen_characters_for_game.append(character_num)
        print(" ")

    choosen_characters_for_game.sort()
    choosen_characters_for_game = [x-1 for x in choosen_characters_for_game]
    all_chosen_characters = [character_list[i] for i in choosen_characters_for_game] # characters chosen to play with
    random_character = random.sample(range(0, number_of_characters), x_players)
    playing_characters = [all_chosen_characters[i] for i in random_character]

    hidden_characters_num = []                                                          # Find hidden charachters with for loop
    for i in range(0, len(all_chosen_characters)):
        if i not in random_character:
            hidden_characters_num.append(i)

    hidden_characters_num.sort()
    hidden_characters = [all_chosen_characters[i] for i in hidden_characters_num]

    return all_chosen_characters, playing_characters, hidden_characters



def send_mail(mail_list, character):
    sender_email = "dannydasan@hotmail.com" # Skriv, hvilken mail vi skal sende fra her 
    password = input(str("Please enter password:")) # Skriv password her 
    
    
    
    for i in range(len(mail_list)):
       
        msg = email.message_from_string('You are a:' + ' ' + character[i])
        msg['From'] = sender_email
        msg['To'] = mail_list[i]
        msg['Subject'] = "Werewolf game"
    
        sever = smtplib.SMTP('smtp.live.com', 587)
        sever.ehlo()
        sever.starttls()
        sever.ehlo()
        sever.login(sender_email, password)
        print("Login success")
        sever.sendmail(sender_email, mail_list[i], msg.as_string())
        print("Email has been sent to:", mail_list[i])
        
    print('The character is now sent to your mails, please check it')
    sever.quit()
    
def reveal_sys(players, character): 
    mail_list = []
    reveal = input(str("Do you want to reveal the characters on the screen or mail. (screen/mail):"))
    
    if reveal == "screen": 
        for i in range(0, len(players)): 
            print(f"Show the screen to {players[i]}")
            time.sleep(2)
            #print(f"{players[i], are you ready? [y/n]?}")
            ans_temp = input(str(f"{players[i]}, are you ready? (y/n)?:"))
            
            while ans_temp == "n": 
                ans_temp = input(str(f"{players[i]}, are you ready now? (y/n)?:"))
            
            if ans_temp == "y":
            
                print(f"{players[i]}, you are {character[i]}")
                time.sleep(2)
                os.system('clear')
                                   
                    
    elif reveal == "mail":
        for i in range(0,len(players)):
            mail_temp = input(str(f"{players[i]}, enter your mail:"))
            mail_list.append(mail_temp)
            
        send_mail(mail_list, character)
        
        #return mail_list
        
    else: 
        print('Invalid syntax, please try again')
        reveal_sys(players, character)
        
    return mail_list
    

