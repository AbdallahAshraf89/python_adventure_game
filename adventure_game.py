import time
import random

# Function to print a message and pause
def print_pause(*messages):
    for message in messages:
        print(message)
        time.sleep(2)

# Initialize the score
total_score = 0

# Function to display choices and get player input
def get_choice(choices):
    print_pause(*choices)
    choice = input("What would you like to do? (Please enter 1 or 2): ")
    while choice not in ["1", "2"]:
        print_pause("<< Invalid input. Please enter 1 or 2 >>")
        choice = input("What would you like to do? (Please enter 1 or 2): ")
    return choice

# Function to handle the field scenario
def field():
    print_pause("You find yourself standing in an open field, filled with grass",
                "and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairy is somewhere around here,",
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)",
                "magic wand.")
    
    choice = get_choice([
        "Enter 1 to knock on the door of the house.",
        "Enter 2 to peer into the cave."
    ])
    
    if choice == "1":
        house()
    elif choice == "2":
        cave()

# Function to handle the house scenario
def house():
    print_pause("You approach the house and knock on the door.")
    print_pause("The door creaks open, and you find yourself in a dimly lit room.")
    print_pause("A friendly old lady offers you some tea and a magical potion.")
    
    choice = get_choice([
        "Enter 1 to accept the tea and potion.",
        "Enter 2 to decline and leave the house."
    ])
    
    if choice == "1":
        print_pause("The tea and potion make you feel stronger.")
        add_score(10)
        end_game("Congratulations! You have completed your quest!")
    elif choice == "2":
        print_pause("You leave the house and wander back into the field.")
        field()

# Function to handle the cave scenario
def cave():
    print_pause("You peer into the cave and see glowing eyes.")
    print_pause("A fierce dragon emerges and blocks your way.")
    
    choice = get_choice([
        "Enter 1 to fight the dragon with your magic wand.",
        "Enter 2 to run away and return to the field."
    ])
    
    if choice == "1":
        if random.choice([True, False]):
            print_pause("Your magic wand miraculously defeats the dragon!")
            add_score(10)
            end_game("Congratulations! You have completed your quest!")
        else:
            print_pause("The dragon overpowers you. You have been defeated.")
            add_score(-10)
            end_game("Game Over. Better luck next time!")
    elif choice == "2":
        print_pause("You run away and find yourself back in the field.")
        field()

# Function to add to the player's score and print it
def add_score(points):
    global total_score
    total_score += points
    print(f"Score: {total_score}")

# Function to end the game and ask to play again
def end_game(message):
    print_pause(message)
    if total_score <= 0:
        print_pause("Your adventure ends here.")
        play_again()
    else:
        play_again()

# Function to reset game settings if the player chooses to play again
def reset_game_settings():
    global total_score
    total_score = 0

# Function to ask if the player wants to play again
def play_again():
    print_pause("Would you like to play again? (y/n)")
    option = input().lower()
    if option == "y":
        reset_game_settings()
        field()
    elif option == "n":
        print_pause("Thanks for playing! Goodbye.")
    else:
        print_pause("<< Invalid input. Please enter y or n >>")
        play_again()

# Start the game
field()
