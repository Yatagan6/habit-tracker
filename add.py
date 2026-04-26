class Drone:
    def __init__(self, name, health, guns):
        self.name = name
        self.__health = health
        self.guns = guns

    def __add__(self, other):
        # Создаем новое имя из двух половин
        new_name = self.name[:3] + other.name[3:]
        
        # Суммируем пушки
        new_guns = self.guns + other.guns
        
        # Берем среднее здоровье
        new_health = (self.__health + other.__health) // 2
        
        # ВОЗВРАЩАЕМ НОВЫЙ ОБЪЕКТ
        print(f"Система: Произошло слияние {self.name} и {other.name}!")
        return Drone(new_name, new_health, new_guns)

    def __str__(self):
        return f"Дрон {self.name} | Пушек: {self.guns} | HP: {self.__health}"

# --- ТЕСТ ---
d1 = Drone("Alpha-7", 100, 2)
d2 = Drone("Zeta-3", 80, 4)

# МАГИЯ!
d3 = d1 + d2 

print(d3) # Выведет: Дрон Alpa-3 | Пушек: 6 | HP: 90