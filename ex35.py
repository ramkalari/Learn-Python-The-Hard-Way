from sys import exit

def gold_room():
    """ This is the gold room. Called by bear_room """
    print "This room is full of gold. How much do you take?"

    next = raw_input("> ")
    try:
        how_much = int(next)
    except ValueError:
        dead("Man, learn to type a number")
        
#    if "0" in next or "1" in next:
 #       how_much = int(next)
  #  else:
   #     dead("Man, learn to type a number")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You are greedy!")

def bear_room():
    print "There's a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps you face off.")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulu_room():
    print "Here you see the great evil Cthulu."
    print "He, it, whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulu_room()

def dead(why):
    print why, "Good job!"
    exit(0)

def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulu_room()
    else:
        dead("You stumble around the room until you starve.")

start()
    
    
    
    
      



    
    

            
        
        
        
