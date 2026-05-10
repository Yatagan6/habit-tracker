from typing import Protocol

# 1. Наш контракт (Чек-лист требований)
class Speaker(Protocol):
    def talk(self) -> str:
        ...

# 2. Живой класс
class Human:
    def talk(self) -> str:
        return "Привет, как дела?"

# 3. Класс-животное
class Parrot:
    def talk(self) -> str:
        return "Попка дурак! Дай семечку!"

# 4. Технический класс (Будильник)
class AlarmClock:
    def talk(self) -> str:
        return "БИИИП-БИИИП! Пора вставать!"

# 5. ИИ-модель (просто код)
class ChatBot:
    def talk(self) -> str:
        return "Я анализирую ваш запрос..."

# 6. Класс-изгой (у него НЕТ метода talk)
class Stone:
    def lie_still(self):
        print("Я просто лежу...")

def broadcast_message(device: Speaker):
    # Нам не важно, КТО это. Нам важно, что у него можно вызвать .talk()
    print(f"Голос из системы: {device.talk()}")

# Создаем объекты
sasha = Human()
kesha = Parrot()
casio = AlarmClock()
gpt = ChatBot()
cobblestone = Stone()
broadcast_message(sasha)  # Работает!
broadcast_message(kesha)  # Работает!
broadcast_message(casio)  # Работает!
broadcast_message(gpt)