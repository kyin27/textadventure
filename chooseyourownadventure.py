import time
    
#dialogue, uses time function to give player time to read
def option4():
    print("There is no time left to fake defuse and someone starts to defuse.")
    time.sleep(2)
    print("a: use your ult"
          "\nb: spray with your gun hoping to kill the defuser")
#choice function, makes player start over if wrong
def uinput1():
    ans = input("enter choice: ")
    if ans == "a":
        print("You use your sova ult and get the defuser and also another enemy. The spike explodes and you win the round")
        time.sleep(1)
        print("THE END (Good Ending)")
        time.sleep(2)
        restart = input("Would you like to play again? (y/n) ")
        if reset == "y":
            start()
        elif reset == "n":
            exit()
    elif ans == "b":
        print("You miss all your shots and the enemy sticks the defuse. You lose the round and end up losing the game")
        time.sleep(1)
        print("THE END (Bad Ending)")
        time.sleep(2)
#restart prompt, exits game if player types n
        reset = input("Would you like to try again? (y/n) ")
        if reset == "y":
            start()
        elif reset == "n":
            exit()
    else:
        uinput1()

#third choice
def option3():
    print("The enemy omen smokes main off and you can’t see the spike.")
    time.sleep(2)
    print("a: use utility to recon"
          "\nb: push through the smoke")
def uinput2():
    ans = input("enter choice: ")
    if ans == "a":
        print("You see that the enemy faked the defuse")
        option4()
        uinput1()
    elif ans == "b":
        print("You push through the smoke and are killed by people expecting you")
        time.sleep(1)
        print("game over")
        time.sleep(2)
        reset = input("Would you like to try again? (y/n) ")
        if reset == "y":
            start()
        elif reset == "n":
            exit()
    else:
        uinput2()

#second choice
def option2():
    print("You got on site. Where do you plant")
    time.sleep(2)
    print("a: main (you defend from b long)"
          "\nb: default (you defend from elbow)")
def uinput3():
    ans = input("enter choice: ")
    if ans == "a":
        print("You plant the spike and prepare for defense.")
        option3()
        uinput2()
    elif ans == "b":
        print("You get the plant down and hear someone tap the spike. You swing and see that they kill you.")
        time.sleep(1)
        print("game over")
        time.sleep(2)
        reset = input("Would you like to try again? (y/n) ")
        if reset == "y":
            start()
        elif reset == "n":
            exit()
    else:
        uinput3()

#first choice
def option1():
    ans = input("enter choice: ")
    if ans == "a":
        print("You get through mid safely. The other team was rotating through spawn thinking you were a site")
        option2()
        uinput3()
    elif ans == "b":
        print("The other team pushes through main and you are killed")
        time.sleep(1)
        print("game over")
        time.sleep(2)
        reset = input("Would you like to try again? (y/n) ")
        if reset == "y":
            start()
        elif reset == "n":
            exit()
    else:
        option1()

#starting dialogue to familiarize player with story
def start():
    print("You are in a 1v5 situation in valorant. The map is pearl and you are playing sova on a site."
            "\nThe enemy jett is definitely a smurf and sweeps all four of your teammates (they are throwing your rank up game). What do you do")
    time.sleep(2)
    print("a: rotate to b site through mid"
          "\nb: stay and plant")
    option1()
#instructions and name detector that doesn't really do much in the game
print('type "a" or "b" to select options. have fun'
      "\n")
time.sleep(2)
def naming():
    n = input("Enter name: ")
    verify = input("Is your name "+n+"? ")
    if verify == "y":
        start()
    elif verify == "n":
        naming()
    else:
        print("invalid answer")
        naming()
naming()
