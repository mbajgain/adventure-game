import time
import random
items = []
creatures = ["wicked fairie", "gorgon", "dragon", "small child"]
creature = random.choice(creatures)


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field, filled with "
                "grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {creature} is somewhere around here, "
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand, you hold your trusty (but not very "
                "effective) dagger.\n")


def choice():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    house_or_cave = input("(Please enter 1 or 2.)\n")
    if house_or_cave == '1':
        confrontation()
        house()
    elif house_or_cave == '2':
        cave()
    else:
        choice()


def confrontation():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens "
                f"and out steps a {creature}.")
    print_pause(f"Eep! This is the {creature}'s house!")
    print_pause(f"The {creature} attacks you!")


def new_game():
    play_again = input("Would you like to play again? (y/n)\n")
    if play_again == 'y':
        print_pause("Excellent! Restarting the game ...")
        play_game()
    elif play_again == 'n':
        print("Thanks for playing! See you next time.")
    else:
        new_game()


def house():
    fight_or_flight = input("Would you like to (1) fight or (2) run away?\n")
    if fight_or_flight == '1':
        if "sword" in items:
            print_pause(f"As the {creature} moves to attack, you "
                        "unsheath your new sword.")
            print_pause("The Sword of Ogoroth shines brightly in "
                        "your hand as you brace "
                        "yourself for the attack.")
            print_pause(f"But the {creature} takes one look at your "
                        "shiny new toy and runs away!")
            print_pause(f"You have rid the town of the {creature}. "
                        "You are victorious!")
            new_game()
        else:
            print_pause("You do your best...")
            print_pause(f"but your dagger is no match for the {creature}.")
            print_pause("You have been defeated!")
            new_game()
    elif fight_or_flight == '2':
        print_pause("You run back into the field. Luckily, "
                    "you don't seem to have been followed.\n")
        choice()
    else:
        house()


def cave():
    if "sword" in items:
        print_pause("You peer cautiously into the cave.")
        print_pause("You've been here before, and gotten "
                    "all the good stuff. It's just an empty cave now.")
        print_pause("You walk back out to the field.\n")
        choice()
    else:
        print_pause("You peer cautiously into the cave.")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger "
                    "and take the sword with you.")
        print_pause("You walk back out to the field.\n")
        items.append("sword")
        choice()


def play_game():
    intro()
    choice()


play_game()
