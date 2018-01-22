#imports
import random
import time
import sys

#global variables for lightside and dark side points, C1 is used to put a loop inside a loop, and E to get the correct epilouge depending on the player's actions
dp = 0
lp = 0
C1 = 0
E = 0

#defining class for the characters and abilities able to be used
class Dnd(object):

#initializing the class and setting up traits of a class
    def __init__(self, hp, mp, inven, feats):
        """
        Define the certain traits of each class to choose from
        """
        self.hp = hp
        self.mp = mp
        self.inven = inven
        self.feats = feats

#function for taking damage from an opponent depending on which enemy it is. Also, puts in the GAME OVER text and makes sure that
#the game never prints that you have negative hp bc that just isn't very professional
    def lose_hp():
        """
        Function for taking certain damage
        """
        if opponent == guard:
            player.hp -= random.randint(1,4)
        if opponent == commander:
            player.hp -= random.randint(2,5)
        if opponent == lord:
            player.hp -= random.randint(3,5)
        if player.hp < 0:
            player.hp = 0
        if player.hp > 0:
            print(f"Your opponent attacks you, but you still have {player.hp} left.")
        if player.hp == 0:
            print("Your opponent finds a crack in your defenses and strikes you down!")
            print("GAME OVER")


#function that sets the damage of the lightsaber depending on which class the player chooses
    def attack():
        if player == guardian:
            opponent.hp -= random.randint(4,9)
        if player == counsular:
            opponent.hp -= random.randint(2,8)
        if player == sentinel:
            opponent.hp -= random.randint(3,8)
        if opponent.hp < 0:
            opponent.hp = 0

#function for the flurry attack which does a bunch of dmg but only the guardian can use it
    def flurry():
        if player == guardian:
            opponent.hp -= random.randint(3,12)
        if opponent.hp < 0:
            opponent.hp = 0

#defining the power strike attack, which does more than attack, but only sentinel can use it
    def power_strike():
        opponent.hp -= random.randint(4,10)
        if opponent.hp <= 0:
            opponent.hp = 0
        if opponent.hp > 0:
            Dnd.lose_hp()

#the force lightning ability, which does tons of dmg but has to be learned through gaining dark side points in game
    def lightning():
        if "lightning" in player.feats:
            if player.mp >= 5:
                print("Feeding into your anger, you strike at your opponent with a powerful blast of lightning!")
                player.mp -= 5
                opponent.hp -= random.randint(5,15)
                print(f"You're opponent now has {opponent.hp} health left!")
                Dnd.lose_hp()
            else:
                print("You don't have enough mana points!")
        else:
            print("You are not in tune with the dark side enough to use this!")

#the force revitalize ability, which restores the player back to full health in the middle of combat depending on which class they are
    def revitalize():
        if "revitalize" in player.feats:
            if player.mp >= 5:
                player.mp -= 5
                if player == counsular:
                    player.hp = 16
                if player == sentinel:
                    player.hp = 21
                if player == guardian:
                    player.hp = 26
                print("Peace and harmony comes to your mind and you restore to full health!")

#the heal ability, which heals the player but it can't overheal and they need enough mana just like all the other abilities
    def heal():
        if player == counsular:
            if player.hp != 16:
                if player.mp >= 5:
                    player.hp += random.randint(3,7)
                    player.mp -= 5
                    print(f"You heal yourself up to {player.hp} health points!")
                    print(f"You now have {player.mp} mana points")
                    Dnd.lose_hp()
                else:
                    print("You don't have enough mana points!")
            else:
                print("You're already at full hp!")

#long rest, which brings the player to full health and mana depending on his/her class
    def longrest():
        if player == counsular:
            player.hp = 16
            player.mp = 30
        if player == sentinel:
            player.hp = 21
            player.mp = 20
        if player == guardian:
            player.hp = 26
            player.mp = 10

#force push, and right here it defines the damage and the mana usage. Late in the do combat function there is a one in four
#chance that the opponent will not attack back when this is used, to simulate him losing a turn
    def force_push():
        if player.mp >= 5:
            opponent.hp -= random.randint(1,6)
            player.mp -= 5
            print(f"You now have {player.mp} mana points")
        else:
            print("You don't have enough mana points!")

#repulse ability, which is like force push but costs more and has a 3/4 chance to knock down the opponent and make them lose a turn
    def repulse():
        if player.mp >= 8:
            opponent.hp -= random.randint(4,10)
            player.mp -= 8
            print(f"You now have {player.mp} mana points left.")
        else:
            print("You don't have enough mana points!")

#function for the player to be able to check his status with out taking up a turn
    def status():
        print(f"""
        hp : {player.hp}
        mp : {player.mp}
        inven : {player.inven}
        feats : {player.feats}
        """)

#allows the player to decide what they will do in combat. basically calls whatever function the user inputs except for push and repulse
#which rolls a 1d4 to see if the opponent will attack the player that turn or get stunned
#only allows combat while the player has hp bc otherwise they'd be dead
    def docombat():
        while opponent.hp > 0:
            a = input(f"\n-You can attack (atk) or use one of your feats, {player.feats}. You may also check your status (status).\n-What will you do?\n")
            if a == "atk".lower():
                Dnd.attack()
                print(f"Your opponent now has {opponent.hp} health left.")
                if opponent.hp > 0:
                    Dnd.lose_hp()
            if a == "attack".lower():
                Dnd.attack()
                print(f"Your opponent now has {opponent.hp} health left.")
                if opponent.hp > 0:
                    Dnd.lose_hp()
            if a == "heal".lower():
                Dnd.heal()
            if a == "lightning":
                Dnd.lightning()
            if a == "status":
                Dnd.status()
            if a == "force push":
                Dnd.force_push()
                print(f"Your opponent now has {opponent.hp} health left.")
                b = random.randint(1,4)
                if b == 1:
                    if opponent.hp > 0:
                        Dnd.lose_hp()
                if b == 2:
                    if opponent.hp > 0:
                        Dnd.lose_hp()
                if b == 3:
                    if opponent.hp > 0:
                        Dnd.lose_hp()
                if b == 4:
                    print("You knock your opponent down, he loses a turn!\n")
            if a == "flurry".lower():
                Dnd.flurry()
                print("You attack with a flurry of blows!")
                print(f"Your opponent now has {opponent.hp} health left!")
                if opponent.hp > 0:
                    Dnd.lose_hp()
            if a == "power strike".lower():
                if player == sentinel:
                    Dnd.power_strike()
                    print("You wind up and strike with great force!")
                    print(f"Your opponent now has {opponent.hp} health left!")
            if a == "repulse".lower():
                if player == counsular:
                    Dnd.repulse()
                    r = random.randint(1,5)
                    print(f"The sheer power of this attack bring your opponent to {opponent.hp} health!")
                    if r == 5:
                        if opponent.hp > 0:
                            print("Somehow, your opponent withstands the attack and strike back at you!")
                            Dnd.lose_hp()
                    else:
                        print("An explosion of telekenetik energy erupts from your body, knocking your opponent to the floor ten feet away! Your opponent loses a turn!")
#this function cuts out all system function when the player gets a game over screen bc they're dead
#also makes it so that the opponent hp won't ever get printed as a negative number
            if player.hp == 0:
                sys.exit()
            if opponent.hp < 0:
                opponent.hp = 0
            if opponent.hp == 0:
                print("You have defeated your opponent!")
                break


#defines the traits of each class and the different opponents that the player might face
guardian = Dnd(26, 10, {"robes": 1, "lightsaber": 1}, ["flurry", "force push"])
sentinel = Dnd(21, 20, {"robes": 1, "lightsaber": 1}, ["force push", "heal", "power strike"])
counsular = Dnd(16, 30, {"lightsaber": 1, "robes": 1}, ["heal", "force push", "repulse"])
guard = Dnd(20, 10, {"lightsaber": 1, "sith robes": 1}, ["power strike"])
commander = Dnd(30,20,{"lightsaber": 1, "sith robes": 1},["flurry"])
lord = Dnd(30, 40, {"lightsaber":1,"lord's robes":1}, ["blast", "choke"])



#Welcome and choosing name, threw the name in there bc I know that people like to put in silly things so this is just for fun
print("""Welcome to Michael Hensley's Star Wars DnD game! First step before you start your journey is to choose a character name.""")
time.sleep(2)
name = input("What will your character's name be?  ")

#class information for the player to read
print(f"-Welcome, jedi knight {name}. There are three classes you may choose from.")
time.sleep(2)
print(f"""-The first, the guardian has an health points of {guardian.hp}, mana points of {guardian.mp}, starts
with an inventory of {guardian.inven}, and is able to use {guardian.feats}.
Guardians are almost always take the combat path because of their physical conditioning and combat skills.""")
time.sleep(4)
print(f"-Next is the sentinel, who has {sentinel.hp} hp, {sentinel.mp} mp, an inventory of {sentinel.inven}, and can use {sentinel.feats}.\nSentinels are also stealthy by nature.")
time.sleep(4)
print(f"""-The final class is the counsular, who has {counsular.hp} hp,{counsular.mp} mp, an inventory of {counsular.inven}, and can use
{counsular.feats}.
Furthermore, they are good talkers by nature.""")


#loop that breaks once player gives valid input to decide which class their char will play as
while True:
    decision = input("\n-Which class will you choose? ")
    if decision == "counsular".lower():
        print("-So you have chosen the way of the force, we shall see whether you use the light, or the dark side.")
        player = counsular
        break
    if decision == "sentinel".lower():
        print("-You have chosen balance between the force and physical strength. We shall see if you become light side or dark side.")
        player = sentinel
        break
    if decision == "guardian".lower():
        print("-You have chosen the way of the blade. We shall see if you use it force defense or agression.")
        player = guardian
        break


#exposition and plot before the game actually starts
time.sleep(3)
print("\nThere is yet unrest in the galaxy.")
time.sleep(1.5)
print("The jedi-sith wars rage on")
time.sleep(1.5)
print("Thousands of jedi have died in the ongoing six year war.")
time.sleep(2)
print("However, hope has been restored to the jedi. The sith overlord's position has been revealed.")
time.sleep(3.5)
print("""You stand in the council room which you are so familiar with, the same place where you were granted the rank of knight
six years before.""")
time.sleep(4)
print("\"This war is coming to an end,\" Master Vrook says.")
time.sleep(2)
print("\"This mission you're about to embark can very well bring this world back to peace and balance.\"")
time.sleep(3)
print("\"We need you to travel to Mustafar to these coordinates, and defeat Darth Ragnos,\" Master Alis continued.")
time.sleep(4)
print(f"\"Her defeat will be a quick and decisive end to this war. We're counting on you, {name}.\"")
time.sleep(4)
print(f"\"Furthermore, if you succeed in this, your title will be changed to master {name}, and you will be granted a seat on this council.\"")
time.sleep(3)
print("""

You land to the coordinates on Mustafar. You look up and see a giant black and red tower raise high above you.

""")
time.sleep(3)

#First time the player gets to decide what they want to do first interaction with a guard at the front gate
#use loops so that a misinput will just make the dialouge box open again
opponent = guard  # < this is how I can switch between opponents with different stats. before a fight might occur between anybody I switch what opponent equals, bc opponent is the variable in the combat function
while player.hp > 0:
    A = input("\nIn front of the tower, you can see a guard sitting near the enterance of the tower, slouching in his chair nodding off. What do you do? You can attempt to sneak past, fight him, or talk to him. ")
    if A == "fight":
        print("\nAs you approach the guard, he takes notice to you and arms his red lightsaber!")
        Dnd.docombat()
        break
    if A == "attack":
        print("\nAs you approach the guard, he takes notice to you and arms his red lightsaber!")
        Dnd.docombat()
        break
    if A == "atk":
        print("\nAs you approach the guard, he takes notice to you and arms his red lightsaber!")
        Dnd.docombat()
        break
    if A == "talk":
        if player == counsular:
#to go along with counsulars being good talkers, they get a small dialouge to hint at which words will let the player pass unharmed
            print("'Maybe if I use the sith lord's name, or ask to pass or go I can get past him peacefully...' you think to yourself")
            time.sleep(1.5)
        print("The man perks up a little bit but goes back into his slouching position.")
        A1 = input("\"What do you want?\" ")
#the in function is used to check what words are in the input, so that they can say whatever they want but these words will let them pass
        if "pass" in A1:
            print("\"To be honest I don't really care just go.\"")
            break
        elif "go" in A1:
            print("\"Just go up the tower whatever.\"")
            break
        elif "ragnos".lower() in A1:
            print("\"Ragnos!? I'm so sorry my lord I've never seen you before, please spare my life.\"")
            time.sleep(1)
            A4 = input("\nThe guard kneels at your feet, what do you do?(kill, spare) ")
#chance for the player to either kill or spare the guard and killing will grant a dark side point, and sparing will grant a light side point
            if A4 == "kill".lower():
                print("Consumed by your anger and hatred for the sith, you strike down the defensless guard. Your dark side points increase by one.")
                dp += 1
                break
            if A4 == "spare".lower():
                print("Seeing no point in destroying the guard, you continue into the tower. Your light side points have increased by one.")
                lp += 1
                break
        else:
            print("At the sound of your voice, the guard stands up quickly realizing you are a jedi.")
            time.sleep(1)
            print("He ignites his red lightsaber!")
            time.sleep(.833)
            print("\"Now you die jedi!\"")
            Dnd.docombat()
            break
    if A == "sneak":
#sets up a 75% chance to get past as the sentinel and a 50% chance to get past on any other class. also if they get caught a similar situation to the talk function arises and they still have the chance for a lp or a dp
        if player == sentinel:
            A2 = random.randint(1,4)
        else:
            A2 = random.randint(1,2)
            if A2 == 1:
                print("The guard perks up and looks directly at you!")
                A3 = input("\"Who the hell are you!?\"\n")
                if "ragnos".lower() in A3:
                    print("\"I'm so sorry my lord I've never seen you before, please spare my life.\"")
                    time.sleep(1)
                    A4 = input("The guard kneels at your feet, what do you do?(kill, spare) ")
                    if A4 == "kill".lower():
                        print("Consumed by your anger and hatred for the sith, you strike down the defensless guard. Your dark side points increase by one.")
                        dp = 1
                        break
                    if A4 == "spare".lower():
                        print("Seeing no point in destroying the guard, you continue into the tower. Your light side points have increased by one.")
                        lp = 1
                        break
                else:
                    print("\"You think you'd fool me jedi scum? Now you die!\"")
                    Dnd.docombat()
                    break
            else:
                print("You successfully stealth past the sleeping guard!")
            break
    else:
        print("invalid input please don't use caps and spell correctly")

#Encounter number two. can take a long rest but then you'll be attacked by a commander or don't take a rest and get a chance for another lp or dp by finding the commander with his back turned
#The "time passing in game" just means that the commander will sense your presence and find you as soon as you come out
#killing him give a dark side point (dp)
#use append function to add lightning to the list of usable abilities in combat
#sparing gives a light side point (lp)
#uses append function to add  to the list of usable abilities in combat, lightning for dp and revitalize for lp

opponent = commander # < switches the opponent to commander stats so that they fight him instead of the guard stats
print("\n\nYou've successfully moved on into the tower!")
time.sleep(1)
print("As soon as you enter, you see a closed off door to your right. You can go inside and safely take a long rest to heal and restore mana, however time will pass in the game.")
while True:
    B1 = input("Would you like to take a long rest? (y/n) ")
    if B1 == "y".lower():
        print("You take a short rest and meditate to heal yourself. You now have full hp and mp.")
        Dnd.longrest()
        print("Upon exiting the room, a large sith commander stands in front of you! He must of sensed a jedi!")
        #time.sleep(2)
        print("'Don't bother trying to talk your way out of this one jedi, you die here!'")
        Dnd.docombat()
        break
    elif B1 == "n".lower():
        print("Time is of the essence, you press on.")
        #time.sleep(1)
        print("As you enter, you see a stair case and start to ascend sensing a power force user above you.")
        #time.sleep(3)
        print("As you're sneaking up the stairs, you see sith a commander with his back turned to you.")
        #time.sleep(3)
        if dp == 1:
            print("'I could get up behind him and kill another sith if I wanted to...' you think to yourself")
        if lp == 1:
            print("'I could probably pass by unnoticed and avoid another needless conflict...' you think to yourself.")
        else:
            print("'He's completely unaware of me, and isn't in my way. He is a powerful sith though... what should I do?' you think to yourself.")
        C1 += 1
        break
    elif B1 == "status".lower():
        Dnd.status()
    else:
        print("Invalid input please retry.")

if C1 == 1:
    while True:
        C = input("What will you do? (kill/sneak)\n")
        if C == "kill":
            dp += 1
            print("Anger for the sith makes your blood boil.")
            #time.sleep(1.2)
            print("You approach the command, lightsaber in hand.")
            #time.sleep(1.2)
            print("You ignite the blade into the commander's back.")
            #time.sleep(1)
            print("The former jedi knight looks down at the lightsaber, and for a second thought it was red before realizing it's blue hue.")
            #time.sleep(3)
            print("The commander falls to the floor, motionless.")
            #time.sleep(1)
            print("A dark energy swirls around you body and you feel your dark side powers grow. It also heals you and restores your mana to full.")
            Dnd.longrest()
            #time.sleep(1)
            player.feats.append("lightning")
            print("You have learned the ability force lightning! Good job you murderer.")
            break
        elif C == "sneak":
            lp += 1
            print("The tension in your muscles from first spotting the commander disappears. ")
            #time.sleep(1.5)
            print("As you walk past him, you feel a light energy swirl around your body.")
            #time.sleep(1.5)
            Dnd.longrest()
            print("You have gained one light side point and have been fully healed and your mana restored!")
            #time.sleep(2)
            player.feats.append("revitalize")
            print("Also, you have gained the ability revitalize! Use it to gain full hp even in combat!")
            break
        else:
            print("Invalid input please retry.")

print("\n\n\nYou've successfully moveed on!")
Dnd.longrest()
opponent = lord
time.sleep(1)
print("Finally, you come to the top of the staircase.")
time.sleep(1)
print("You enter a dark room, and a chill is sent down your spine from the dark energy permeating the air.")
time.sleep(3)
print("A thick metal door slides shut behind you, trapping you in the room.")
time.sleep(1)
print("In front of you there is a small step up to a giant red metal chair.")
time.sleep(1)
print("You suddenly spot the woman occupying the chair.")
time.sleep(1)
print("'How did I not see her as soon as I walked in!?' you think to yourself.")
time.sleep(3)
print("The woman cloaked in black robes and red sith face paint sat on her sits on her throne legs crossed, studying you.")
time.sleep(3)
print("Gaining back your courage, you speak up, \"Darth Ragnos! This war is at an end!\"")
time.sleep(3)
print("\"It seems that will be the case one way or another,\" she responds in a cool calm voice.")
time.sleep(3)

#Now the encounter starts to get involved with the actual player
D = input(f"\"Tell me {name}, why have you come here?\"\n")
if "kill" in D:
    print("Do really wish to kill me or is that what the council want of you?")
elif "defeat" in D:
    print("Do you really wish to defeat me or is that what the council wants of you?")
elif "master" in D:
    print("So you've come all this way for a promotion on your council?")
#this one is if the player throws the quote "I will do what I must" in from ep 3
elif "will do what" in D:
    print("You will try...")
    Dnd.docombat()
    E += 2
elif "attack" in D:
    print("\"Already trying to kill me? Listen to what I have to say first.\"")
elif "atk" in D:
    print("\"Already trying to kill me? Listen to what I have to say first.\"")
elif "fight" in D:
    print("\"Already trying to kill me? Listen to what I have to say first.\"")
elif "lightning" in D:
    print("\"Already trying to kill me? Listen to what I have to say first.\"")
elif "flurry" in D:
    print("\"Already trying to kill me? Listen to what I have to say first.\"")
elif "sneak" in D:
    print("\"No no hunny, there's no sneaking your way out of this.\"")
elif D == "":
    print("\"I see you have few words, so I'll be speaking now.\"")
elif D == " ":
    print("\"I see you have few words, so I'll be speaking now.\"")
elif "run" in D:
    print("\"No running, neither of us are running, now listen to what I have to say.\"")
#if they say "I am your father" you get a funny response
elif "your father" in D:
    print("\"...um.. j-just listen to what I have to say...\"")
else:
    print("\"I don't believe that is why you came here really.\"")
time.sleep(3)

#special encounter for if the player has two light side points
if lp == 2:
    print("Suddenly, her confidence seems to subside as if she has realized the powerful light aura surronding you.")
    time.sleep(3)
    print("'Maybe I can turn her to the light to let go of her anger...' you think as you sense conflict within her.")
    time.sleep(3)
    D1 = input("\"Who are you? Are you the grandmaster of the council?\"\n")
    if "no" in D1:
        print("\"You are the strongest light side user I've ever seen before... If we fought together we could take down the council and rule over everything...\"")
    elif D1 == name:
        print("\"Yes I know your name, but what are you... If you joined me you can forget about the promotion on the council once you return...\"")
    elif "yes" in D1:
        print("\"Well I'll only get on shot at killing you, then.\"")
        time.sleep(2)
        print("She stands up and ignites her double-sided red lightsaber.")
        Dnd.docombat()
        E += 2
    elif "let go" in D1:
        print("\"I-I... yes too many lives have been lost in this war. It is time for it to end.\"")
    else:
        print("Actually, I've had enough tlaking. Let us end this through battle.")
        Dnd.docombat()
        E += 2

    if opponent.hp > 0:
        while True:
            D2 = input(f"\"What do you say, {name}, will you join me?\"(y/n)  ")
            if D2 == "y":
                print("\"Good.. Now let us pay a visit to the council and end their tyrany and lies.\"")
                E += 1
                break
            elif D2 == "n":
                print("\"Then this place will be your tomb.\"")
                time.sleep(2)
                print("She stands up and ignites red double-sided red lightsbaer!")
                Dnd.docombat()
                E += 2
                break

#special encounter for having one dark side point. possible to have one lp and one dp, but the dp overrides the lp because dark side completely goes against everything the jedi stand for
elif dp == 1:
    print("\"I sense that you are strong in the dark side of the force.\"")
    time.sleep(2)
    print("\"The council you work for is corrupt and only cares for its own needs.\"")
    time.sleep(3)
    print("\"I know you've noticed this yourself. Think, why did they send you here to kill me, the most powerful sith alive, alone?\"")
    time.sleep(3)
    print("\"They want you dead, they don't want you to expose them to the citizens who trust the council and allow them power.\"")
    time.sleep(3)
    print("\"If you were to join me, then we could rule over all of it together, and take down the corrupt system in place.\"")
    time.sleep(3)
    print("Darth Ragnos extends a hand out and down towards you...")
    time.sleep(3)
    while True:
        D2 = input(f"\"What do you say, {name}, will you join me?\"(y/n)\n")
        if D2 == "y":
            print("\"Good.. Now let us pay a visit to the council and end their tyrany and lies.\"")
            E += 1
            break
        elif D2 == "n":
            print("\"Then this place will be your tomb.\"")
            time.sleep(2)
            print("She stands up and ignites red double-sided red lightsbaer!")
            Dnd.docombat()
            E += 2
            break

elif dp == 2:
    print("You really came here because you are done with the council.")
    time.sleep(2)
    print("Looking at you previous actions, you have no intention of returning back to the council as a jedi.")
    time.sleep(4)
    while True:
        D2 = input(f"\"What do you say, {name}, will you join me?\"(y/n)  ")
        if D2 == "y":
            print("\"Good.. Now let us pay a visit to the council and end their tyrany and lies.\"")
            E += 1
            break
        elif D2 == "n":
            print("\"Then this place will be your tomb.\"")
            time.sleep(2)
            print("She stands up and ignites red double-sided red lightsbaer!")
            Dnd.docombat()
            E += 3
            break

#If one lp or no l/d points at all, generic encounter
else:
    print("I believe you have come here to be done with the council.")
    time.sleep(3)
    print("\"The council you work for is corrupt and only cares for its own needs.\"")
    time.sleep(3)
    print("\"I know you've noticed this yourself. Think, why did they send you here to kill me, the most powerful sith alive, alone?\"")
    time.sleep(3)
    print("\"They want you dead, they don't want you to expose them to the citizens who trust the council and allow them power.\"")
    time.sleep(3)
    print("\"If you were to join me, then we could rule over all of it together, and take down the corrupt system in place.\"")
    time.sleep(3)
    print("Darth Ragnos extends a hand out and down towards you...")
    time.sleep(3)
    while True:
        D2 = input(f"\"What do you say, {name}, will you join me?\"(y/n)  ")
        if D2 == "y":
            print("\"Good.. Now let us pay a visit to the council and end their tyrany and lies.\"")
            E += 1
            break
        elif D2 == "n":
            print("\"Then this place will be your tomb.\"")
            time.sleep(2)
            print("She stands up and ignites red double-sided red lightsbaer!")
            Dnd.docombat()
            E += 2
            break

#every other ending changes E's value, so this one is if you spare darth ragnos (need to have 2 lp)
if E == 0:
    print("You choosen the path of the true jedi.")
    time.sleep(2)
    print("The council sent you to kill Darth Ragnos, but instead you brought her back to the council in handcuffs.")
    time.sleep(3)
    print("The senate tries Darth Ragnos and finds her guilty of war crimes, and she is sentenced to life in prison.")
    time.sleep(3)
    print("Deciding that the council is too political and cares for its own gains, you exile yourself, leaving your lightsaber with the council and going into hiding.")
    time.sleep(6)
    print("TRUE ENDING")
    time.sleep(2)
    print("Thanks for playing!!")
    sys.exit()

#Evil ending were you join the sith and destroy the jedi
if E == 1:
    print("You and Darth Ragnos go to the jedi council and slaughter everyone")
    time.sleep(2)
    print("You rule over the galaxy with Darth Ragnos for ten years, but then stab her in the back and rule over everything for yourself.")
    time.sleep(5)
    print("You have chosen the path of the betrayer.")
    time.sleep(2)
    print("EVIL ENDING")
    time.sleep(2)
    print("Thanks for playing!")
    sys.exit()

#Most likely ending where you kill darth ragnos and return to the council as a hero
if E == 2:
    print("You have choosen to kill Darth Ragnos.")
    time.sleep(2)
    print("When you return to the council, you are welcomed as a hero and recieve a spot on the council as a master.")
    time.sleep(4)
    print("GOOD ENDING")
    time.sleep(2)
    print("Thanks for playing!")
    sys.exit()

#Most evil ending possible, need to have to dp
if E == 3:
    print("After beheading Darth Ragnos, you go through the castle and kill everybody in sight.")
    time.sleep(4)
    print("Then you return to the council and kill them too.")
    time.sleep(2)
    print("Then, you start an empire of your own and rule over the galaxy through your mastery of the dark side.")
    time.sleep(4)
    print("TRUE DARK SIDE ENDING")
    time.sleep(2)
    print("Thanks for playing! :p")
    sys.exit()



