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


def accept_quest(self, quest):
        self.active_quests.append(quest)
        print(f"You accepted the quest: {quest.name}")

    def complete_quest(self, quest):
        self.add_gold(quest.reward_gold)
        self.gain_experience(quest.reward_experience)
        self.active_quests.remove(quest)
        print(f"You completed the quest: {quest.name}")

    def use_special_ability(self, ability_name):
        if ability_name in self.special_abilities:
            ability = self.special_abilities[ability_name]
            if ability_name == "Fireball":
                return ability["damage"]
            elif ability_name == "Heal":
                self.health += ability["heal_amount"]
                if self.health > 100:
                    self.health = 100
                return 0
        else:
            print("Invalid ability.")
            return 0

# Define the Enemy class
class Enemy(Character):
    def __init__(self, name, health, attack, defense, experience_reward, gold_reward):
        super().__init__(name, health, attack, defense)
        self.experience_reward = experience_reward
        self.gold_reward = gold_reward

# Define the Game class
class Game:
    def __init__(self):
        self.player = None
        self.running = True
        self.shop_items = [
            Weapon("Sword", 5, 50),
            Weapon("Axe", 7, 70),
            Armor("Shield", 3, 40),
            Armor("Helmet", 2, 30),
            Consumable("Health Potion", 20, 10),
            Consumable("Elixir", 50, 25)

]
        self.available_quests = [
            Quest("Goblin Menace", "Defeat 3 goblins in the forest.", 100, 50),
            Quest("Orc Invasion", "Defeat 2 orcs near the village.", 200, 100)
        ]

    def start(self):
        print("Welcome to the RPG Game!")
        player_name = input("Enter your character's name: ")
        self.player = Player(player_name)
        self.main_menu()

    def main_menu(self):
        while self.running:
            print("\nMain Menu")
            print("1. Explore")
            print("2. View Character")
            print("3. View Inventory")
            print("4. Visit Shop")
            print("5. View Quests")
            print("6. Exit Game")
            choice = input("Choose an option: ")

            if choice == '1':
                self.explore()
            elif choice == '2':
                self.view_character()
            elif choice == '3':
                self.view_inventory()
            elif choice == '4':
                self.visit_shop()
            elif choice == '5':
                self.view_quests()
            elif choice == '6':
                self.exit_game()
            else:
                print("Invalid choice. Please try again.")

    def explore(self):
        print("\nExploring...")
        encounter_chance = random.randint(1, 100)
        event_chance = random.randint(1, 100)
        if event_chance <= 20:
            self.random_event()
        elif encounter_chance <= 50:
            self.encounter_enemy()
        else:
            print("You found nothing of interest.")

    def encounter_enemy(self):
        enemy = self.generate_enemy()
        print(f"\nA wild {enemy.name} appeared!")
        while enemy.is_alive() and self.player.is_alive():
            print(f"\n{self.player.name}: {self.player.health} HP")
            print(f"{enemy.name}: {enemy.health} HP")
            print("1. Attack")
            print("2. Use Special Ability")
            print("3. Use Item")
            print("4. Run")
            choice = input("Choose an action: ")

if choice == '1':
                damage = self.player.attack_enemy(enemy)
                print(f"You attacked {enemy.name} for {damage} damage.")
                if enemy.is_alive():
                    enemy_damage = enemy.attack_enemy(self.player)
                    print(f"{enemy.name} attacked you for {enemy_damage} damage.")
            elif choice == '2':
                self.use_special_ability()
            elif choice == '3':
                self.use_item()
            elif choice == '4':
                print("You ran away safely.")
                return
            else:
                print("Invalid choice. Please try again.")

        if not self.player.is_alive():
            print("You have been defeated!")
            self.running = False
        elif not enemy.is_alive():
            print(f"You defeated {enemy.name}!")
            self.player.gain_experience(enemy.experience_reward)
            self.player.add_gold(enemy.gold_reward)
            print(f"You gained {enemy.experience_reward} experience and {enemy.gold_reward} gold.")
            self.check_quest_completion(enemy)

    def generate_enemy(self):
        enemy_types = [
            ("Goblin", 30, 5, 2, 20, 10),
            ("Orc", 50, 8, 3, 30, 20),
            ("Troll", 70, 10, 5, 50, 30),
            ("Dragon", 100, 15, 10, 100, 50)
        ]
        enemy_choice = random.choice(enemy_types)
        return Enemy(*enemy_choice)

    def random_event(self):
        events = [
            ("You found a hidden treasure chest!", 50, 0),
            ("A mysterious stranger offers you a potion.", 0, 20),
            ("You stumble upon an abandoned campsite.", 0, 0)
        ]
        event = random.choice(events)
        print(event[0])
        self.player.add_gold(event[1])
        self.player.gain_experience(event[2])

    def check_quest_completion(self, defeated_enemy):
        for quest in self.player.active_quests:
            if quest.name == "Goblin Menace" and defeated_enemy.name == "Goblin":
                self.player.complete_quest(quest)
            elif quest.name == "Orc Invasion" and defeated_enemy.name == "Orc":
                self.player.complete_quest(quest)

def view_character(self):
        print(f"\nCharacter Information:")
        print(f"Name: {self.player.name}")
        print(f"Level: {self.player.level}")
        print(f"Health: {self.player.health}")
        print(f"Attack: {self.player.attack}")
        print(f"Defense: {self.player.defense}")
        print(f"Experience: {self.player.experience}/{self.player.experience_to_next_level}")
        print(f"Gold: {self.player.gold}")
        if self.player.equipped_weapon:
            print(f"Equipped Weapon: {self.player.equipped_weapon.name}")
        if self.player.equipped_armor:
            print(f"Equipped Armor: {self.player.equipped_armor.name}")

    def view_inventory(self):
        print("\nInventory:")
        if self.player.inventory:
            self.player.inventory.sort(key=lambda item: item.name)
            for idx, item in enumerate(self.player.inventory):
                print(f"{idx + 1}. {item}")
            print("Select an item number to use or 0 to go back:")
            choice = input("Choose an item: ")
            if choice.isdigit() and 0 < int(choice) <= len(self.player.inventory):
                self.use_item(int(choice) - 1)
            elif choice == '0':
                return
            else:
                print("Invalid choice. Please try again.")
        else:
            print("Your inventory is empty.")

    def use_item(self, item_index=None):
        if item_index is None:
            item_index = input("Enter the item number to use: ")
            if not item_index.isdigit() or not (0 < int(item_index) <= len(self.player.inventory)):
                print("Invalid item number.")
                return
            item_index = int(item_index) - 1
        item = self.player.inventory[item_index]
        if isinstance(item, Consumable):
            self.player.use_consumable(item)
            self.player.inventory.pop(item_index)
            print(f"You used {item.name} and restored {item.heal_amount} HP.")
        elif isinstance(item, Weapon):
            self.player.equip_weapon(item)
            print(f"You equipped {item.name}.")
        elif isinstance(item, Armor):
            self.player.equip_armor(item)
            print(f"You equipped {item.name}.")

