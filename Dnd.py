import random
import time
class Dnd(object):

    def __init__(self, hp, mp, inven, feats):
        """
        Define the certain traits of each class to choose from
        """
        self.hp = hp
        self.mp = mp
        self.inven = inven
        self.feats = feats

    def lose_hp():
        """
        Function for taking certain damage
        """
        player.hp -= random.randint(1,6)

    def dead():
        if player.hp <= 0:
            print("ur ded")
            print("git gud")

    def attack():
        opponent.hp -= random.randint(2,8)

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


guardian = Dnd(25, 5, {"robes": 1, "lightsaber": 1}, ["flurry", "force push"])
sentinel = Dnd(17, 10, {"robes": 1, "lightsaber": 1}, ["force push", "mind trick"])
counsular = Dnd(15, 20, {"lightsaber": 1, "robes": 1}, ["heal", "force push", "stasis", "mind trick"])
opponent = Dnd(20, 10, {"sword": 1, "key": 1}, ["power strike"])



print("-There are three classes you may choose from.")
print(f"""-The first, the guardian has an health points of {guardian.hp}, mana points of {guardian.mp}, starts
with an inventory of {guardian.inven}, and is able to use {guardian.feats}.""")
print(f"-Next is the theif, who has {sentinel.hp} hp, {sentinel.mp} mp, an inventory of {sentinel.inven}, and can use {sentinel.feats}.")
print(f"""-The final class is the mage, who has {counsular.hp} hp,{counsular.mp} mp, an inventory of {counsular.inven}, and can use
{counsular.feats}.""")

while True:
    decision = input("\n-Which class will you choose? ")
    if decision == "counsular".lower():
        print("-You'll only use your knowledge for want of power, but we shall continue.")
        player = counsular
        break
    if decision == "sentinel".lower():
        print("-You scoundrel, but we shall continue your story.")
        player = sentinel
        break
    if decision == "guardian".lower():
        print("-Wars not make one great, but we shall continue.")
        player = guardian
        break
time.sleep(1)
print("You encounter an evil knight!\n You begin combat!")













