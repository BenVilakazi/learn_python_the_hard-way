def win():
    print("congratulations, you win!")

def start():
    print("You wake up in a dark room")
    print("in front of you, you have 3 doors choose a door to start the game\nEnter either 1,2 or 3")
    choice = input("> ")
    if choice == "1":
        first_door()
    elif choice == "2":
        second_door()
    elif choice == "3":
        third_door()
    else:
        dead("You died, please try again")

def first_door():
    print("You have entered thru the first door")
    print("To get through to the next door you have to get the key")
    print("There's a snake protecting the key")
    print("In front of you a choice of a either a sword, crossbow or spear")
    print("choose your weapon")
    weapon = input("> ")
    print(f"you have choosen a {weapon} as your weapon")
    if weapon == "sword":
        print("""
              You do the following:
              1. Attack the Snake
              2. Charm the snake
              3. Run away""")
        answer = input("> ")
        if answer == "1":
            print("You got bitten by the snake")
            dead("You poisoned by the snake")
        elif answer == "2":
            print("The snake is charmed")
            print("You got the key!")
            final_door()
        elif answer == "3":
            print("You go back to start")
            dead("You died of starvation")
        else:
            exit(0)
    elif weapon == "spear":
        print("""
              You do the following:
              1. Attack the Snake
              2. Charm the snake
              3. Run away""")
        answer = input("> ")
        if answer == "1":
            print("You strike the snake")
            print("The snake spit at you")
            print("You are poisoned you and the snake die")
            dead("You died from poisoning")
        elif answer == "2":
            print("The snake is charmed")
            print("You got the key!")
            final_door()
        elif answer == "3":
            print("You go back to start")
            dead("You died of starvation")
            start()
        else:
            first_door()
    elif weapon == "crossbow":
        print("""
              You do the following:
              1. Attack the Snake
              2. Charm the snake
              3. Run away""")
        answer = input("> ")
        if answer == "1":
            print("You shoot & kill the snake")
            print("You the key")
            final_door()
        elif answer == "2":
            print("You charm the snake")
            print("You get the key")
            print("You move onto the final test")
            final_door()
        elif answer == "3":
            print("You go back to start")
            dead("You died of starvation")
            start()
        else:
            first_door()
    else:
        first_door()
        
    
def second_door():
    print("There is a bear here")
    print("The bear has honey")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear?")
    bear_moved = False
    
    while True:
        choice = input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door")
            print("You can go through it now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off")
        elif choice == "open door" and bear_moved:
            treasure_room()
        else:
            print("I got no idea what that means")
    
def third_door():
    print("Here you see the great evil Wizard")
    print("He, it, whatever stares at you and you go insane")
    print("Do you flee for your life or eat your head")
    
    choice = input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        third_door()
        
def dead(why):
    print(why, "Good job!")
    exit(0)
    
def final_door():
    print("You have made it to the final test")
    print("In front of you have 2 doors")
    print("Enter the door on the left or the door on the right")
    pick = input("> ")
    if pick == "left":
        print("You have fallen into a trap")
        dead("You fell into a trap and died")
        start()
    elif pick == "right":
        print("You have chosen correctly")
        treasure_room()
    else:
        final_door()
        
def treasure_room():
    print("This room is full of gold. How much do take?")
    
    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")
        
    if how_much < 50:
        print("Nice, you're not greedy,you win!")
        exit(0)
    else:
        dead("You greedy bastard!")
start()