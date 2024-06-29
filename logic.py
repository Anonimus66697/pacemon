from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   
        
        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        
        self.hp = randint(50,100)
        self.power = randint(5, 15)

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']['other']['home']['front_default'])
        else:
            return "Pikachu"
    
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"

    # Метод класса для получения информации
    def info(self):
        return f"""Имя твоего покеомона: {self.name}
Здоровье твоего покемона: {self.hp}
Сила покемона: {self.power}"""

    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    def attack(self, enemy):
        if isinstance(enemy, Wizard): # Проверка на то, что enemy является типом данных Wizard (является экземпляром класса Волшебник)
            chance = randint(1,5)
            if chance == 1:
                return "Покемон-волшебник применил щит в сражении"
            enemy.hp -= self.power
        if enemy.hp <= 0:
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
        else:
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"  
        
class Wizard(Pokemon):
    pass

class Fighter(Pokemon):
    def attack(self, enemy):
        superpower = randint(5,15)
        self.power += superpower
        res = super().attack(enemy)
        self.power -= superpower
        return res + f"\nБоец применил супер-атаку силой:{superpower} "
    