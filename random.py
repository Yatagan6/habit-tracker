
class Drone:
    @staticmethod
    def generate_random_name():
        prefixes = ["Cyber", "Steel", "Neo", "Volt"]
        suffixes = ["-100", "-X", "-Beta", "-Prime"]
        
        # Выбираем случайные элементы из списков
        name = random.choice(prefixes) + random.choice(suffixes)
        return name

# Вызываем без создания дрона
new_name = Drone.generate_random_name()
print(f"Сгенерировано имя: {new_name}")