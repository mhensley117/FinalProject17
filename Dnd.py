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
time.sleep(1)
name = input("What will your character's name be?  ")

#class info
print(f"-Welcome, jedi knight {name}. There are three classes you may choose from.")
time.sleep(4)
print(f"""-The first, the guardian has an health points of {guardian.hp}, mana points of {guardian.mp}, starts
with an inventory of {guardian.inven}, and is able to use {guardian.feats}.""")
time.sleep(5)
print(f"-Next is the sentinel, who has {sentinel.hp} hp, {sentinel.mp} mp, an inventory of {sentinel.inven}, and can use {sentinel.feats}.")
time.sleep(5)
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
        print("-You have chosen balance over either physical or force. We shall see if you become light side or dark side.")
        player = sentinel
        break
    if decision == "guardian".lower():
        print("-You have chosen the way of the blade. We shall see if you use it force defense or agression.")
        player = guardian
        break


time.sleep(3)
print("""














