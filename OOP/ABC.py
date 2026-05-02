from abc import ABC, abstractmethod

# 1. Наш шаблон-контракт
class BaseRobot(ABC):
    @abstractmethod
    def say_hello(self):
        pass

# 2. Класс-наследник, который "ленится"
class LazyRobot(BaseRobot):
    def say_hello(self):
        pass

# 3. Попытка создать ленивого робота
bot = LazyRobot()

