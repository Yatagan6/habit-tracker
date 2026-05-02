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

d1 = Drone("Alpha-7", 100, 2)
d2 = Drone("Zeta-3", 80, 4)
d3 = d1 + d2 
print(d3)
class Drone:
    def __init__(self, name, hp, slots):
        self.name = name
        self.hp = hp
        self.slots = slots # Список модулей, например ["Пушка", "Радар"]

    # 1. ТЕКСТ (Лицо и Техпаспорт)
    def __str__(self):
        return f"Дрон {self.name}"

    def __repr__(self):
        return f"Drone(name='{self.name}', hp={self.hp}, slots={self.slots})"

    # 2. МАТЕМАТИКА (Сложение здоровья)
    def __add__(self, other):
        return self.hp + other.hp

    # 3. СРАВНЕНИЕ (Кто сильнее?)
    def __gt__(self, other): # Greater Than (>)
        return self.hp > other.hp

    # 4. КОЛЛЕКЦИЯ (Доступ к модулям)
    def __len__(self):
        return len(self.slots)

    def __getitem__(self, index):
        return self.slots[index]

# --- ПРОВЕРКА В ДЕЛЕ ---
d1 = Drone("Alpha", 100, ["Лазер", "Щит"])
d2 = Drone("Beta", 80, ["Мотор"])

print(d1)            # Сработал __str__ -> Дрон Alpha
print(d1 + d2)       # Сработал __add__ -> 180
print(d1 > d2)       # Сработал __gt__  -> True
print(len(d1))       # Сработал __len__ -> 2
print(d1[0])         # Сработал __getitem__ -> Лазер