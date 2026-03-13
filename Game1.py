import random

def choice_enemy(enemies_list):
        print("Выберите врага:")
        for i, enemy in enumerate(enemies_list):
            if current_enemy.health > 0:
                print(f"{i+1}. {enemy.name} {enemy.health} ХП")

        choice = int(input("Введите номер врага:\t")) - 1
        return enemies_list[choice].name


class Enemy:
    def __init__(self, name, health, damage):
        self.health = health
        self.damage = damage
        self.name = name

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            print(f"Вы убили {self.name} и победили!")
            exit()
        return self.health

    def info(self):
        return self.name, self.health, self.damage


class Zombie(Enemy):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def attack(self, damage=5):
        if mage.health <= 0:
            mage.health = 0
            mage_is_death = True
            print(f'{mage.name} мёртв!')
            exit()
        else:
            mage_is_death = False

        health_character = mage.take_damage(damage)

        if not mage_is_death:
            print(f"\n{self.name} ударил {mage.name}. Жизней у {mage.name}: {health_character}")
        return health_character

    def spec_attack(self, damage=10):
        if mage.health <= 0:
            mage.health = 0
            mage_is_death = True
            print(f'{mage.name} мёртв!')
            exit()
        else:
            mage_is_death = False

        health_character = mage.take_damage(damage)

        if not mage_is_death:
            print(f"\n{self.name} укусил {mage.name}! Жизней у {mage.name}: {health_character}")
        return health_character


class Skelet(Enemy):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)

    def attack(self, damage=7):
        if mage.health <= 0:
            mage.health = 0
            mage_is_death = True
            print(f'{mage.name} мёртв!')
            exit()
        else:
            mage_is_death = not True

        health_character = mage.take_damage(damage)

        if not mage_is_death:
            print(f"\n{self.name} выстрелил в {mage.name}. Жизней у {mage.name}: {health_character}")
        return health_character

    def spec_attack(self, damage=20):
        if mage.health <= 0:
            mage.health = 0
            mage_is_death = True
            print(f'{mage.name} мёртв!')
            exit()
        else:
            mage_is_death = not True

        health_character = mage.take_damage(damage)

        if not mage_is_death:
            print(f"\n{self.name} пронзил голову {mage.name}! Жизней у {mage.name}: {health_character}")
        return health_character


zombie = Zombie("Зомби", 50, 5)
skelet = Skelet("Скелет", 35, 7)

enemies = [zombie, skelet]
current_enemy = random.choice(enemies)

class Sword:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

diamond_sword = Sword("Деревянный Меч", 10)

class Character:
    def __init__(self, name, age, health, role):
        self.name = name
        self.age = age
        self.health = health
        self.role = role

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            exit()
        return self.health

    def attack(self):
        if current_enemy.health <= 0:
            zombie.health = 0
            enemy_is_death = True
            print(f'{current_enemy.name} мёртв!')
        else:
            enemy_is_death = not True

        health_enemy = current_enemy.take_damage(diamond_sword.damage)

        if not enemy_is_death:
            print(f"\n{'*- | ' + self.role + ' |-*'} {self.name} атаковал {current_enemy.name}. Жизней у {current_enemy.name}: {health_enemy}")
        current_enemy.attack(20)
        return health_enemy



    def info(self):
        print(f"\n\n{'='*25}\n|         ИГРОК         |\n|                       |\n| ХП: {self.health}\t\t\t\t|\n| Имя: {self.name}\t\t\t\t|\n| Возраст: {self.age}\t\t\t|\n| Роль: {self.role}\t\t\t|\n| Оружие: {diamond_sword.name}|\n{'='*25}\n\n")

name = input("Введите имя:\t")
try:
    while True:
        age = int(input("Введите возраст:\t"))
        if age < 0 or age > 100:
            print("Введите верный возраст!")
        else:
            break
except ValueError:
    exit()

while True:
    role = input("Введите вашу роль(МАГ, ВОИН):\t")
    if role == "Маг".lower().upper() or role == "Воин".lower().upper():
        confirm_role = role.upper()
        break
    else:
        print("Введите существующую роль!")

mage = Character(name, age, 100, confirm_role)

while True:
    main_menu = int(input(f"\nВижу {current_enemy.name} по курсу\n=*1*= Атаковать {current_enemy.name}\n=*2*= Информация о персонаже\n=*3*= Выбрать врага\n=*4*= Выйти из игры\nВыберите один из предложенных вариантов выше:\t"))
    if main_menu == 1:
        mage.attack()
    elif main_menu == 2:
        mage.info()
    elif main_menu == 3:
        choice_enemy(enemies)
    elif main_menu == 4:
        break
