import valids, config

menu_options = 4
diff_options = 3

def menu():
    while True:
        print("""
------  MAIN MENU  ------

- (1) Start Game
- (2) Difficulty Settings
- (3) Game Info
- (4) Exit
""")
        choice = valids.menuval()
        if choice == 1:
            break
        elif choice == 2:
            diff_menu()
        elif choice == 3:
            gameinfo()
        elif choice == 4:
            quit()

def gameinfo():
    print("""

WELCOME TO THE WORLD OF PYZON!

Enter a fantastical realm of adventure and peril in this adventure
akin to earlier text-based games such as Zork.  Written entirely
within Python, this game is both meant to be a technical demo
as well as a pet project.

Game written by Tyler Rasmussen

""")

def diff_menu():
    print("""
------ GAME DIFFICULTY ------

- (1) Easy
- (2) Medium
- (3) Hard
""")
    sel = valids.diffmenuval()
    if sel == 1:
        config.game_diff = 0
    elif sel == 2:
        config.game_diff = 1
    elif sel == 3:
        config.game_diff = 2