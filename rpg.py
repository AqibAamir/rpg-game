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


   def attack_enemy(self, enemy):
        damage = self.attack - enemy.defense
        if damage < 0:
            damage = 0
        enemy.take_damage(damage)
        return damage

# Define the Player class
class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 10, 5)
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = 100
        self.gold = 0
        self.inventory = []
        self.equipped_weapon = None
        self.equipped_armor = None
        self.active_quests = []
        self.special_abilities = {
            "Fireball": {"damage": 20, "cost": 10},
            "Heal": {"heal_amount": 30, "cost": 5}
        }

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= self.experience_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        self.experience_to_next_level *= 2
        self.health += 10
        self.attack += 2
        self.defense += 1
        print(f"{self.name} leveled up to level {self.level}!")

    def add_gold(self, amount):
        self.gold += amount

    def add_item(self, item):
        self.inventory.append(item)

    def equip_weapon(self, weapon):
        if self.equipped_weapon:
            self.attack -= self.equipped_weapon.attack_boost
        self.equipped_weapon = weapon
        self.attack += weapon.attack_boost

    def equip_armor(self, armor):
        if self.equipped_armor:
            self.defense -= self.equipped_armor.defense_boost
        self.equipped_armor = armor
        self.defense += armor.defense_boost

    def use_consumable(self, consumable):
        self.health += consumable.heal_amount
        if self.health > 100:
            self.health = 100

