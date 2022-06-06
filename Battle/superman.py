from Battle.Hero import Hero


class superman(Hero):
    def __init__(self, name, armor):
        super().__init__(self, name)
        self.armor = armor

    def extra_point(self):
        self.health += self.armor
        print(f'Dodano super strój z armorem {self.armor} twoje życie wynosi: {self.health}')
