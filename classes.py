#CLASSES FOR BOTH PLAYER CLASSES AND ENEMY INFORMATION
import valids

######### PLAYER CLASSES AND FUNCTIONS #############

#Main player class menu
player_class_total = 5
def player_class_menu(name):
    print("""
Do you see yourself as...
(1) A heroic adventurer?
(2) A savage barbarian?
(3) A worldly monk?
(4) A swift archer?
(5) A strong-firing pistolier?
    """)
    selection = class_choice(name)
    return selection

#Character class selection menu
def class_choice(name):
    choice = valids.classval()
    if choice == 1:
        return adventurer(name)
    if choice == 2:
        return barbarian(name)
    if choice == 3:
        return monk(name)
    if choice == 4:
        return archer(name)
    if choice == 5:
        return pistolier(name)

class adventurer:
    def __init__(self, name):
        self.name = name
        self.attack = 2
        self.health = 10
        self.title = "adventurer"
        self.ranged = False

class barbarian:
    def __init__(self, name):
        self.name = name
        self.attack = 4
        self.health = 5
        self.title = "barbarian"
        self.ranged = False

class monk:
    def __init__(self, name):
        self.name = name
        self.attack = 1
        self.health = 20
        self.title = "monk"
        self.ranged = False

class archer:
    def __init__(self, name):
        self.name = name
        self.attack = 2
        self.health = 6
        self.title = "archer"
        self.ranged = True

class pistolier:
    def __init__(self, name):
        self.name = name
        self.attack = 4
        self.health = 4
        self.title = "pistolier"
        self.ranged = True

#Player class debug information
def player_debug(pclass):
    print(f"""
Player Name: {pclass.name}

Player Attack: {pclass.attack}
Player Health: {pclass.health}

Player Title: {pclass.title}
Player is Ranged: {pclass.ranged}
""")


######### ENEMY CLASSES ###########

#List of enemies
enemies = [
    "goblin",
    "troll"
]

#Enemy Classes
class goblin:
    def __init__(self):
        self.name = "goblin"
        self.attack = 1
        self.health = 3
        self.ranged = False

class troll:
    def __init__(self):
        self.name = "troll"
        self.attack = 2
        self.health = 5
        self.ranged = False