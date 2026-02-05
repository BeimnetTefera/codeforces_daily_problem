class Player:
    game_name = 'Dragon Quest'

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, amount):
        if Player.is_valid_amount(amount):
            self.health -= amount
    
    def heal(self, amount):
        if Player.is_valid_amount(amount):
            self.health += amount

    @classmethod
    def change_game_name(cls, new_name):
        cls.game_name = new_name

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0
    
p1 = Player('Alex', 100)
p2 = Player('Jamie', 80)

p1.take_damage(30)
print(p1.health)

p2.heal(20)
print(p2.health)

print(p1.game_name)
print(p2.game_name)

Player.change_game_name('Shadow Realm')
print(p2.game_name)

print(Player.is_valid_amount(-5))