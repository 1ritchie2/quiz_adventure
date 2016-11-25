# An adventure game
from random import randint
hardmode = 0
easymode = 0
def modechoose():
    global easymode
    global hardmode
    print("Would you like")
    print("A. Easy mode or")
    print("B. Hard mode")
    mode = input("A or B? Enter here: ")
    if mode.lower() == "a":
        print("Easy mode? This means when you die you go back to the start of the room, good luck.")
        easymode = easymode + 1
        room1()
        

    if mode.lower() == "b":
        print("Hard mode? Good choice but be careful when you die.. Theres no second chance...")
        hardmode = hardmode + 1
        room1()

    

def room1():
    global easymode
    global hardmode
    print("You wake up exhausted, you feel like your chests caving in from the inside as if something was moving around inside of you...")
    print("Anyway... you find that you're deep underground as you look up above you and the hole you are in goes on forever, there is a corridor in front of you, you choose to walk down it")
    room2()
    

def room2():
    global easymode
    global hardmode
    print("As you approach the end of the corridor you see a group of small shadows getting closer and closer")
    print("A. Do you confront the shadows or...")
    print("B . Do you hide in the room to the right of you")
    answer = input("A or B?: ")

    if answer.lower() == "a":
        print("You approach the shadows and they turn out to be Goblins on the hunt for trespassing humans, since you were prepared for a fight you realise you are able to do it with your fists as the Goblins are small and frail, you win the fight and sustain no damage, and continue on to the next room.")
        room3()

    if answer.lower() == "b":
        print("The door is locked!! You are ambushed by goblins and eaten alive...")
        print("Gameover. You died.")
    if hardmode == 1 and easymode == 0:
        room1()
    elif easymode == 1 and hardmode == 0:
        room2() 
    

def room3():
    global easymode
    global hardmode
    print("As you reach the next room you see a strange man sitting on a throne with his armour shining with a mystical power. What do you do?")
    print("A. Do you ambush him while he sleeps? Or...")
    print("B. Do you question him?")
    answer = input("A or B? Which do you choose?")

    if answer.lower() == "a":
        print("As you attempt to cave his skull in he wakes up and grabs you by the throat and crushes your neck as blood gushes out of your face.")
        if hardmode == 1 and easymode == 0:
            room1()

        elif easymode == 1 and hardmode == 0:
            room3() 

    if answer.lower() == "b":
        print("You ask him who he is and why you're here, at that moment the wiggling in your stomach intensifies")
        print("He says 'I know you're feeling that thing in your stomach, that is my Queen, its growing inside of you. After a while it will burst out your body. It's inevitable'")
        room4() 


def room4():
    global easymode
    global hardmode
    print("You feel a surging power rattle through your bones chilling your spinal cord.")
    print("A bright mist if aura shrouds your body in beautiful, divine colours as your feet lift you into the airand you hover over the king ahead of you like a giant looking down at a puny, weak, small ant.")
    print("Now is the best to chance to kill him")
    print("What do you do?")
    print("A. Try and kill him while you have the chance")
    print("B. Kill yourself while destroying the queen inside your stomach")
    answer = input("A or B, this could be your final decision... Enter here: ")

    if answer.lower() == "a":
        ending1()

    if answer.lower == "b":
        ending2()

def ending1():
    global easymode
    global hardmode
    if hardmode == 1 and easymode == 0:
        print("This is it you gain all the aura in your body to your hand. You prepare to fire, but you realise it isn't a guaranteed hit. May fortune be with you.")
    hit = randint(1, 3)
    if hit == 1 or hit == 3:
        print("You fire the shot with all the power and arua in your body. As the gigantic ball of power approaches the man in the chair he ducks and jumps forward, he slices you in half as your guts pour out your body, at this second the Queen falls out.. Humanity is doomed.")
        print("Game Over.")
        room1()
    if hit == 2:
        print("This is it you gain all the aura in your body to your hand. You prepare to fire")
        print("You shoot the ball of aura straight at him, he doesnt budge, he knows when you kill him you wont be able to stop the Queen, the realisation hits.")
        print("The human race is doomed. Its all your fault")
        credit()

    elif easymode == 1 and hardmode == 0:
        print("This is it you gain all the aura in your body to your hand. You prepare to fire")
        print("You shoot the ball of aura straight at him, he doesnt budge, he knows when you kill him you wont be able to stop the Queen, the realisation hits.")
        print("The human race is doomed. Its all your fault")
        credit()

def ending2():
    global easymode
    global hardmode

    if hardmode == 1 and easymode == 0:
        hit = randint (1, 5)
        if hit == 3:
            print("You rip open your stomach and ateempt to grab the thing inside of you by the head, you grab it, then crush it.")
            print("The man screams at you charges and plunges you with a sword. You die. But for the good of humanity. Farewell and good luck.")
            credit()

        else:
            print("You rip open you stomach and attempt to grab the head of the thing inside of you and crush it. You accidentally crush your beating heart.")
            print("Game over")
            room1()

    if easymode == 1 and hardmode == 0:
        print("You rip open your stomach and ateempt to grab the thing inside of you by the head, you grab it, then crush it.")
        print("The man screams at you charges and plunges you with a sword. You die. But for the good of humanity. Farewell and good luck.")
        credit()

def credit():
    print("Producer Designer and everything else:")
    print("Alex Ritchie") 
    
        
        

     

    



















          
    
          
          
        
    
        
    
        
        
    


    








# Leave this at the bottom - it makes room1 run automatically when you
# run your code.
if __name__ == "__main__":
    modechoose()
