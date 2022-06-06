from Battle.Hero import Hero


class batman(Hero):
    def __init__(self, name, perk):
        super().__init__(self, name)
        self.perk = perk

    def super_hit(self, other):
        other.health -= 50
        self.mana -= 100

