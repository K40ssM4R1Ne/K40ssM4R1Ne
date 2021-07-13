answer = input("would you like to start the game? (yes/no) ")
stage = 0
inventory = 0
counter = 0
while answer.lower().strip() != "yes":
    answer = input("would you like to start the game? (yes/no) ")
if answer.lower().strip() == "yes":
    print("\nType forward/back/left/right to move around each area")
    print(
        "\nYou wake up groggy in a small, dimly lit room. You can see broken \nwindows on all 4 walls and debris scattered all over the place. It's obvious that no one has been here \nin a very long time.")
    stage = 1
else:
    print("Maybe another time")


def room1(stage, inventory, answer):
    answer = input("-forward/back/left/right ")
    if answer.lower().strip() == "forward":
        if inventory == 1:
            print("\nYou try the key you found, the door opens with a distinct clicking sound.")
            stage = 2
            inventory = 2
        elif inventory == 0:
            print("\nYou walk up to a rusty metal door, it appears to be locked.")
            print("\nYou go back to the center of the room.")
        elif inventory >= 2:
            print("\nYou exit the room you woke up in, and enter the dimly lit hallway once again")
            stage = 3
    elif answer.lower().strip() == "left":
        print("\nYou see a broken window, but it's too high up to reach.")
        print("\nYou go back to the center of the room.")
    elif answer.lower().strip() == "right":
        print("\nYou see a broken window, but it's too high up to reach.")
        print("\nYou go back to the center of the room.")
    elif answer.lower().strip() == "back":
        if inventory == 0:
            answer = input("\nYou find an old wooden crate, what would you like to do with it? (leave it/open it) ")            
            if answer.lower().strip() == "open it":
                inventory +=1
                print("\nYou pry open the crate and find a key inside.")
                print("\nYou go back to the center of the room.")
            else:
                print("\nYou go back to the center of the room.")
        elif inventory > 0:
            print("\nYou look at the wooden crate you opened.")
            print("\nYou go back to the center of the room.")
    return inventory, stage


def room2(stage):
    print("\nYou exit the room you were previously in and enter a long hallway, the light level is roughly the same except for\nthe light bulb furthest to the left, which is flickering.")
    stage = 3
    return stage

   
def room3(stage, inventory, answer):
    answer = input("-forward/back/left/right ")
    if answer.lower().strip() == "forward":
        print("\nYou examine the wall in front of you but all you see are some creepy paintings")
    elif answer.lower().strip() == "back":
        print("you go back inside the room you woke up in, nothing seems to have changed.")
        stage = 1
    elif answer.lower().strip() == "left":
        if inventory == 2:
            answer = input("You walk left until you the reach the end of the hallway, the door there is ajar.\nWould you like to open it? (open it/go back)")
            if answer.lower().strip() == "open it":
                stage = 4
                inventory = 3
            else:
                print("you go back to the middle of the hallway.")
        elif inventory >= 3:
            print("go from hallway into kitchen, no basic text")
            stage = 5
    elif answer.lower().strip() == "right":
        print("Go into the dining room")
        stage = 6
    return inventory, stage


def room4(stage):
    print("You enter the kitchen, basic text")
    stage = 5
    return stage


def room5(stage, inventory, answer):
    answer = input("-forward/back/left/right ")
    if answer.lower().strip() == "back":
        print("You exit the kitchen and go back into the hallway.")
        stage = 3
    elif answer.lower().strip() == "forward":
        print("whatever is at this side of kitchen")
    elif answer.lower().strip() == "left":
        print("Maybe something to help progress the story in a cabinet idk yet")
    elif answer.lower().strip() == "right":
        print("Whatever I decide goes here")
    return inventory, stage


def room6(stage):
    print("You enter the dining room, basic text")
    stage = 7
    return stage


def room7(inventory, stage, answer):
    answer = input("-forward/back/left/right ")
   
    return inventory, stage
