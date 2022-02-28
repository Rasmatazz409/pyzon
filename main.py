#  _______           _______  _______  _       
# (  ____ )|\     /|/ ___   )(  ___  )( (    /|
# | (    )|( \   / )\/   )  || (   ) ||  \  ( |
# | (____)| \ (_) /     /   )| |   | ||   \ | |
# |  _____)  \   /     /   / | |   | || (\ \) |
# | (         ) (     /   /  | |   | || | \   |
# | )         | |    /   (_/\| (___) || )  \  |
# |/          \_/   (_______/(_______)|/    )_)
# 
# Pyzon - Text-Based Adventure Game
# by Tyler Rasmussen
# 
# A basic text-based adventure game akin to Zork
# and other early-era games.  Used as a learning
# and technical demo showcasing python features
# such as multi-file handling, classes, and others
# 

import valids, classes, pyfiglet, menu, roomgen, config, random
from time import sleep

##### VARIABLE SETUPS #####
rooms_max = 5 + (3 * config.game_diff)


##### GAME LOGO ######
logo_text = pyfiglet.figlet_format("PyZon", font="epic")
print(logo_text)

##### MAIN GAME FUNCTION ######
def main():

    #Character creation loop - allows for player to go back and make changes with confirmation
    char_creation_complete = False
    while char_creation_complete == False:
        print("\nLet's begin...\nFirst, let's start with introductions.  What name do you go by?")
        player_name = valids.nameval()

        print("\nNow... Tell me about yourself.")
        sleep(1)
        player = classes.player_class_menu(player_name)

        sleep(1)
        ranged = " ranged" if player.ranged else ""
        if player.title[0] in "aeiou":
            print(f"So... your name is {player.name}, you are an {player.title}, you have {player.attack}{ranged} attack, and you have {player.health} hit points...")
        else:
            print(f"So... your name is {player.name}, you are a {player.title}, you have {player.attack}{ranged} attack, and you have {player.health} hit points...")
        sleep(1)
        print("Is this correct?")
        if valids.yes_no():
            char_creation_complete = True
    
    #TODO: CHARACTER INVENTORY SELECTION GOES HERE
    
    #TODO: INTRODUCTION BLOCK GOES HERE

    #MAIN GAME BEGINS HERE
    room_num = 0
    while room_num < rooms_max:
        roomgen.gen_room(player, room_num)
        room_num += 1
    print("You have successfully completed your adventure! Congratulations!")

##### CODE EXECUTION STARTS HERE #####
menu.menu()
main()