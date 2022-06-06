class Hero:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.mana = 100
        self.money = 1000

    def introduce_yourself(self):
        print(f"My name is: {self.name}. My health is: {self.health}")

    def rest(self):
        self.health += 20

    def phy_attack(self, enemy):
        enemy.health -= 20

    def rob(self, how, other):
        other.money -= how
        self.money += how
