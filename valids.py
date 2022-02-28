#VALIDATION FUNCTIONS FOR PLAYER SELECTION - AVOIDS UNWANTED SELECTIONS

import classes, menu

def menuval():
    syms = "!@#$%^&*()_+-=//`~\\\'\"?.><}{"
    while True:
        choice = input("Please enter your selection > ")
        if not choice:
            print("Please select a valid choice.")
            continue
        for x in choice:
            if x.isalpha():
                print("Please enter a numerical value.")
                continue
            if x in syms:
                print("Please enter a valid choice")
                continue
        try:
            if int(choice) not in range(1,menu.menu_options+1):
                print("Please enter a valid choice.")
                continue
        except:
            continue
        else:
            break
    return int(choice)

def diffmenuval():
    syms = "!@#$%^&*()_+-=//`~\\\'\"?.><}{"
    while True:
        choice = input("Please enter your selection > ")
        if not choice:
            print("Please select a valid choice.")
            continue
        for x in choice:
            if x.isalpha():
                print("Please enter a numerical value.")
                continue
            if x in syms:
                print("Please enter a valid choice")
                continue
        try:
            if int(choice) not in range(1,menu.diff_options+1):
                print("Please enter a valid choice.")
                continue
        except:
            continue
        else:
            break
    return int(choice)

def nameval():
    syms = "!@#$%^&*()_+-=//`~\\\'\"?.><}{"
    while True:
        name = input("Please enter your name > ")
        if not name:
            print("I cannot call you nothing... Try again.")
            continue
        if len(name) > 16:
            print("Let's keep this succinct, shall we?")
            continue
        for x in name:
            if x in syms:
                print("Only alphabetical characters, please.")
                break
        else:
            break
    return name

def classval():
    syms = "!@#$%^&*()_+-=//`~\\\'\"?.><}{"
    while True:
        choice = input("Please enter your selection > ")
        if not choice:
            print("Please select a valid choice.")
            continue
        for x in choice:
            if x.isalpha():
                print("Please enter a numerical value.")
                continue
            if x in syms:
                print("Please enter a valid choice")
                continue
        try:
            if int(choice) not in range(1,classes.player_class_total+1):
                print("Please enter a valid choice.")
                continue
        except:
            continue
        else:
            break
    return int(choice)

def yes_no():
    valid = ["y","n","yes","no"]
    while True:
        choice = input("(Y)es or (N)o: ").lower()
        if not choice:
            print("Please enter a valid choice.")
            continue
        elif choice not in valid:
            print("Please enter a valid choice.")
            continue
        elif choice in valid:
            break
        else:
            print("VALIDATION ERROR; PLEASE CHECK")
    if choice == "y" or choice == "yes":
        return True
    else:
        return False

def player_choice():
    choices = ["status","attack","run"]
    choice = input("Please enter your command > ").lower()
    while True:
        if not choice or choice not in choices:
            print("Please enter a valid command.")
            continue
        elif choice in choices:
            break
        else:
            print("VALIDATION ERROR; PLEASE CHECK")
    return choice