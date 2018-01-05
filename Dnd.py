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

#function that checks and prints a game over message if the player's hp reaches or is less than 0
    def dead():
        if player.hp <= 0:
            print("ur ded")
            print("git gud")

#function that sets the damage of the lightsaber
    def attack():
        opponent.hp -= random.randint(2,8)

    def heal():
        player.hp += 5
        player.mp -= 7

    def status():
        print(f"""
        hp : {player.hp}
        mp : {player.mp}
        inven : {player.inven}
        feats : {player.feats}
        """)

#function that defines combat
    def combat():
        while player.hp > 0:
            if player.hp <= 0:
                Dnd.dead()
                break
            elif opponent.hp <= 0:
                print("You defeated your opponent!")
                player.hp += 10
                break
            Dnd.attack()
            print(f"You attack and your opponent has {opponent.hp} health left!")
            Dnd.lose_hp()
            print(f"The knight cuts you and you now have {player.hp} health left!")

#defines the traits of each class and the first opponent
guardian = Dnd(25, 10, {"robes": 1, "lightsaber": 1}, ["flurry", "force push"])
sentinel = Dnd(17, 20, {"robes": 1, "lightsaber": 1}, ["force push", "mind trick"])
counsular = Dnd(15, 30, {"lightsaber": 1, "robes": 1}, ["heal", "force push", "stasis", "mind trick"])
opponent = Dnd(20, 10, {"sword": 1, "key": 1}, ["power strike"])


#Welcome and choosing name
print("""Welcome to Michael Hensley's Star Wars DnD game! First step before you start your journey is to choose a character name.""")
#time.sleep(2)
name = input("What will your character's name be?  ")

#class info
print(f"-Welcome, jedi knight {name}. There are three classes you may choose from.")
#time.sleep(2)
print(f"""-The first, the guardian has an health points of {guardian.hp}, mana points of {guardian.mp}, starts
with an inventory of {guardian.inven}, and is able to use {guardian.feats}.""")
#time.sleep(4)
print(f"-Next is the sentinel, who has {sentinel.hp} hp, {sentinel.mp} mp, an inventory of {sentinel.inven}, and can use {sentinel.feats}.")
#time.sleep(4)
print(f"""-The final class is the counsular, who has {counsular.hp} hp,{counsular.mp} mp, an inventory of {counsular.inven}, and can use
{counsular.feats}.""")


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


#If/when the player's health drops below zero, it'll be set to zero so that you won't have negative hit points ever


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

print("""

You land to the coordinates on Mustafar. You look up and see a giant black and red tower raise high above you.

""")

for x in range(15):
    print(player.hp)
    Dnd.lose_hp()
    if player.hp <= 0:
        player.hp = 0
    if player.hp == 0:
        print("u r ded lol")
        break











