#imports
import random
import time

#defining class
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

#function for taking damage from an opponent
    def lose_hp():
        """
        Function for taking certain damage
        """
        player.hp -= random.randint(1,6)
        if player.hp < 0:
            player.hp = 0
        if player.hp > 0:
            print(f"Your opponent attacks you, but you still have {player.hp} left.")
        if player.hp == 0:
            print("Your opponent finds a crack in your defenses and strikes you down!")
            print("GAME OVER")


#function that sets the damage of the lightsaber
    def attack():
        opponent.hp -= random.randint(2,8)
        if opponent.hp < 0:
            opponent.hp = 0

#function for the flurry attack
    def flurry():
        if player == guardian:
            opponent.hp -= random.randint(3,12)
        if opponent.hp < 0:
            opponent.hp = 0

#defining the power strike attack
    def power_strike():
        opponent.hp -= random.randint(4,10)
        if opponent.hp <= 0:
            opponent.hp = 0
        if opponent.hp > 0:
            Dnd.lose_hp()

#the heal ability
    def heal():
        if player == counsular:
            if player.mp >= 5:
                player.hp += random.randint(3,7)
                player.mp -= 5
                print(f"You heal yourself up to {player.hp} health points!")
                print(f"You now have {player.mp} mana points")
                Dnd.lose_hp()
            else:
                print("You don't have enough mana points!")

#long rest
    def longrest():
        print("You take a short rest and meditate to heal yourself. You now have full hp and mp.")
        if player == counsular:
            player.hp = 15
            player.mp = 30
        if player == sentinel:
            player.hp = 20
            player.mp = 20
        if player == guardian:
            player.hp = 25
            player.mp = 10

#force push
    def force_push():
        if player.mp >= 5:
            opponent.hp -= random.randint(1,6)
            player.mp -= 5
            print(f"You now have {player.mp} mana points")
        else:
            print("You don't have enough mana points!")

#repulse ability
    def repulse():
        if player.mp >= 8:
            opponent.hp -= random.randint(3,8)
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

#allows the player to decide what they will do in combat
    def docombat():
        while opponent.hp > 0:
            if player.hp == 0:
                break
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


#defines the traits of each class and the first opponent
guardian = Dnd(25, 10, {"robes": 1, "lightsaber": 1}, ["flurry", "force push"])
sentinel = Dnd(20, 20, {"robes": 1, "lightsaber": 1}, ["force push", "heal", "power strike"])
counsular = Dnd(15, 30, {"lightsaber": 1, "robes": 1}, ["heal", "force push", "repulse"])
guard = Dnd(20, 10, {"lightsaber": 1, "sith robes": 1}, ["power strike"])
commander = Dnd(30,20,{"lightsaber": 1, "sith robes": 1},["flurry"])



#Welcome and choosing name
print("""Welcome to Michael Hensley's Star Wars DnD game! First step before you start your journey is to choose a character name.""")
#time.sleep(2)
name = input("What will your character's name be?  ")

#class info
print(f"-Welcome, jedi knight {name}. There are three classes you may choose from.")
#time.sleep(2)
print(f"""-The first, the guardian has an health points of {guardian.hp}, mana points of {guardian.mp}, starts
with an inventory of {guardian.inven}, and is able to use {guardian.feats}.
Guardians are almost always take the combat path because of their physical conditioning and combat skills.""")
#time.sleep(4)
print(f"-Next is the sentinel, who has {sentinel.hp} hp, {sentinel.mp} mp, an inventory of {sentinel.inven}, and can use {sentinel.feats}.\nSentinels are also stealthy by nature.")
#time.sleep(4)
print(f"""-The final class is the counsular, who has {counsular.hp} hp,{counsular.mp} mp, an inventory of {counsular.inven}, and can use
{counsular.feats}.
Furthermore, they are good talkers by nature.""")


#loop that breaks once player gives valid input to decide which class their char will be
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


#exposition before the game starts
#time.sleep(3)
#print("\nThere is yet unrest in the galaxy.")
#time.sleep(1.5)
#print("The jedi-sith wars rage on")
#time.sleep(1.5)
#print("Thousands of jedi have died in the ongoing six year war.")
#time.sleep(2)
#print("However, hope has been restored to the jedi. The sith overlord's position has been revealed.")
#time.sleep(3.5)
#print("""You stand in the council room which you are so familiar with, the same place where you were granted the rank of knight
#six years before.""")
#time.sleep(4)
#print("\"This war is coming to an end,\" Master Vrook says.")
#time.sleep(2)
#print("\"This mission you're about to embark can very well bring this world back to peace and balance.\"")
#time.sleep(3)
#print("\"We need you to travel to Mustafar to these coordinates, and defeat Darth Ragnos,\" Master Alis continued.")
#time.sleep(4)
#print(f"\"Her defeat will be a quick and decisive end to this war. We're counting on you, {name}.\"")
#time.sleep(4)
#print(f"\"Furthermore, if you succeed in this, your title will be changed to master {name}, and you will be granted a seat on this council.\"")
#time.sleep(3)
#print("""

#You land to the coordinates on Mustafar. You look up and see a giant black and red tower raise high above you.

#""")
#time.sleep(3)

#First time the player gets to play lol first interaction with a guard at the front gate
opponent = guard
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
    if A == "talk":
        if player == counsular:
            print("'Maybe if I convince him I'm his leader, or ask to pass nicely I can go...' you think to yourself")
            time.sleep(1.5)
        print("The man perks up a little bit but goes back into his slouching position.")
        A1 = input("\"What do you want?\" ")
        if "pass" in A1:
            print("\"To be honest I don't really care just go.\"")
            break
        if "go" in A1:
            print("\"Just go up the tower whatever.\"")
            break
        if "ragnos".lower() in A1:
            print("\"I'm so sorry my lord I've never seen you before, please spare my life.\"")
            time.sleep(1)
            A4 = input("\nThe guard kneels at your feet, what do you do?(kill, spare) ")
            if A4 == "kill".lower():
                print("Consumed by your anger and hatred for the sith, you strike down the defensless guard. Your dark side points increase by one.")
                dp = 1
                break
            if A4 == "spare".lower():
                print("Seeing no point in destroying the guard, you continue into the tower. Your light side points have increased by one.")
                lp = 1
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

if player.hp > 0:
    print("\n\nYou've successfully moved on!")
    time.sleep(1)
    print("As soon as you enter, you see a closed off door to your right. You can go inside and safely take a long rest to heal and restore mana.")
    while True:
        B1 = input("Would you like to take a long rest? (y/n) ")
        if B1 == "y".lower():
            Dnd.longrest()
            break
        if B1 == "n".lower():
            print("You decide to press on.")
            break













