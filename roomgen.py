#GENERATES ROOMS AND MANAGES COMBAT FOR PLAYER PROGRESSION
import random, valids, classes
from time import sleep
#Initialize the random module - uses current system time as a seed
random.seed()

#Room Descriptions
rooms = [
    "an immense, dark, damp cave barren of noise except the occasional drip of condensation.  The smell of mildew and the sea permeate the environment and glints of light reflect off of the slick walls, casting dancing visuals around you.",
    "a dimly lit stone hallway, lit by a lone torch hanging on the wall.  The hallway extends far beyond the vision provided by the sole light source.  Distant echoes can be heard but are faint enough to be indistinguishable or recognizeable.",
    "a musty, vast library lined with row upon row of bookcases.  Stairs lead to an additional floor above that lines the walls, leaving the center open to views of the lower floor.  Lanterns are scattered around the room, giving the environment a gloomy but well-lit atmosphere.",
    "a chamber that is clearly a prison. Small barred cells line the walls, leaving a 15-foot-wide pathway for a guard to walk. Channels run down either side of the path next to the cages, probably to allow the prisoners' waste to flow through the grates on the other side of the room. The cells appear empty but your vantage point doesn't allow you to see the full extent of them all.",
    "a room littered with remnants of broken tables, chairs, and what appears to be the remains of broken armor and weapons.  Blood is splattered in all directions and stains the walls, floor, and ceiling as if an immense struggle took place here.",
    "a central courtyard surrounded by tall, impassible stone walls and a circular garden at its center.  The garden is occupied by numerous plants of unknown origin and a singular, towering tree that twists and stretches above you.",
    "and see that a dozen statues stand or kneel in this room, and each one lacking a head and standing in a posture of action or defense. All are garbed for battle. It's difficult to tell for sure without their heads, but two appear to be dwarves, one might be an elf, six appear human, and the rest look like they might be orcs.",
    "the room. A stone throne stands on a foot-high circular dais in the center of this cold chamber. The throne and dais bear the simple adornments of patterns of crossed lines -- a pattern also employed around each door to the room.",
    "a small room lined with benchlike seats on all the walls. The seats all have holes in their top, like a privy. Facing stones on the front of the benches prevent you from seeing how deep the holes go. It looks like a communal bathroom.",
    "and the sound of rushing water fills your ears.  Along the walls, channels of flowing water can be seen running towards the wall you entered from.  On the opposite end, gargoyles with gaping maws can be seen hanging from the walls, water pouring from their mouths into the channels.",
    "a small, round room.  The focal point of the room appears to be the unnaturally tall ceiling, featuring supports and windows usually seen on the outside of castles.  It appears to be a tower of some sort but with no way to ascend.",
    "a square room filled with crates, barrels, and chests.  They are laid out in an organized manner, hinting that this may be some form of storage room.  However, further inspection reveals them all to be empty or contain useless junk.",
    "a room with a door on the opposite wall and windows lining the adjacent walls.  The door opposite of you has been hastily boarded up and barricaded with whatever furniture could be found.  Signs of wear and damage can be seen around the edges of the door on the wall and the door itself.",
    "what appears to be a catacomb or tomb.  Slots in the walls are occupied by coffins and skeletons, brittle with signs of decay.  Skulls and bones that have unfortunately lost their bodily counterparts can be seen littered around the floor.",
    "and see rows of tables covered in utensils, bowls, mugs, and scraps of rotten food.  This appears to be what remains of a mess hall.  The remnants of legends and tales of glory can be felt in the memories lingering in the air."
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
        elif choice == "attack":
            break