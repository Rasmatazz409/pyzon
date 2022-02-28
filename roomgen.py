#GENERATES ROOMS AND MANAGES COMBAT FOR PLAYER PROGRESSION
import random, valids, classes
from time import sleep
#Initialize the random module - uses current system time as a seed
random.seed()

#Room Descriptions
rooms = [
    "an immense, dark, damp cave barren of noise except the occasional drip of condensation.",
    "a dimly lit stone hallway, lit by a lone torch hanging on the wall.",
    "a musty, vast library lined with row upon row of ancient scrolls and books.",
    "a deep dungeon lined on both sides with empty cells.",
    "an abandoned barracks strewn with broken armor, weapons, and the splatter of blood.",
    "a central courtyard surrounded by tall, impassible stone walls and a circular garden at its center.",
    "a throne room, now littered with destroyed furniture, torn tapestries, and glass from the broken windows."
]
roomnum = len(rooms)

########Room Variables###########
#Chance an enemy will spawn out of 10 (10 meaning an enemy will ALWAYS spawn, 0 meaning they will NEVER spawn)
enemy_chance = 4
chanceint = 10 - enemy_chance

######### Main Generation Function #########
def gen_room(player, cur_room = 0):
    print("")
    if cur_room != 0:
        print("The door closes firmly behind you.")
    print("You enter " + random.choice(rooms))
    sleep(1)
    enemy_present = True if random.randint(1,10) > chanceint else False
    if enemy_present:
        combat(player)
    print("Will you press on?")
    if not valids.yes_no():
        print("You have decided to end your adventure abruptly.  Farewell...")
        quit()
    
########### Main Combat Function ###########
def combat(player):
    enemy = eval("classes." + random.choice(classes.enemies) + "()")
    print(f"You encounter an {enemy.name}!") if enemy.name[0] in 'aeiou' else print(f"You encounter a {enemy.name}!\n")

    sleep(1)

    if combat_menu(player,enemy) == "run":
        return
    
    #Ranged advantage attack
    if player.ranged and not enemy.ranged:
        print("You use your range to fire off an early attack.")
        print(f"You deal {player.attack} damage to the {enemy.name}.")
        enemy.health -= player.attack
        input("Press enter to continue...\n")
    
    #Combat loop
    #TODO: Add player choices
    while enemy.health > 0 and player.health > 0:
        if combat_menu(player, enemy) == "run":
            break
        print(f"You deal {player.attack} damage to the {enemy.name}.")
        enemy.health -= player.attack
        if enemy.health <= 0:
            break
        print(f"The {enemy.name} deals {enemy.attack} damage to you.")
        player.health -= enemy.attack
        input("Press enter to continue...\n")
    
    #Messages based on victor of the battle
    if enemy.health <= 0:
        print(f"You have successfully defeated the {enemy.name}!")
        input("Press enter to continue...\n")
    elif player.health <= 0:
        print("You have fallen in battle! GAME OVER")
        quit()


############ Helper Functions ############
#Player Status Function
def player_status(player):
    print(f"Name: {player.name}\nAttack: {player.attack}\nHealth: {player.health}")
    input("Press enter to continue...\n")

#Player Combat Menu
def combat_menu(player, enemy):
    print("Will you ATTACK, RUN, or check your STATUS?")
    while True:
        choice = valids.player_choice()
        if choice == "status":
            #TODO: NEED TO FIND WAY TO RETURN TO PLAYER CHOICE WITHOUT CONTINUING FUNCTION
            player_status(player)
            continue
        elif choice == "run" and player.ranged:
            print("Your distance from the enemy allowed you to safely escape.")
            input("Press enter to continue...\n")
            return "run"
        elif choice == "run" and not player.ranged:
            print("The enemy managed to get an attack in while you were running away.")
            print(f"You took {enemy.attack} damage.")
            player.health -= enemy.attack
            if player.health <= 0:
                print("You were slain in battle.  GAME OVER")
                quit()
            else:
                input("Press enter to continue...\n")
                return "run"
        else:
            break