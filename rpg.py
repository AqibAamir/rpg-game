mport random

# Define the Item class
class Item:
    def __init__(self, name, item_type, effect, cost):
        self.name = name
        self.item_type = item_type
        self.effect = effect
        self.cost = cost

    def __str__(self):
        return f"{self.name} ({self.item_type}): {self.effect} - Cost: {self.cost} gold"

# Define the Weapon subclass
class Weapon(Item):
    def __init__(self, name, attack_boost, cost):
        super().__init__(name, 'Weapon', f"Attack +{attack_boost}", cost)
        self.attack_boost = attack_boost

# Define the Armor subclass
class Armor(Item):
    def __init__(self, name, defense_boost, cost):
        super().__init__(name, 'Armor', f"Defense +{defense_boost}", cost)
        self.defense_boost = defense_boost

# Define the Consumable subclass
class Consumable(Item):
    def __init__(self, name, heal_amount, cost):
        super().__init__(name, 'Consumable', f"Heals {heal_amount} HP", cost)
        self.heal_amount = heal_amount

# Define the Quest class
class Quest:
    def __init__(self, name, description, reward_gold, reward_experience):
        self.name = name
        self.description = description
        self.reward_gold = reward_gold
        self.reward_experience = reward_experience

    def __str__(self):
        return f"{self.name}: {self.description} - Reward: {self.reward_gold} gold, {self.reward_experience} XP"

# Define the Character class
class Character:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    def is_alive(self):
        return self.health > 0
