class Drone:
    status = "Патрулирование"
    @classmethod
    def change_status(cls, new_status):
        cls.status = new_status
    @staticmethod
    def is_name_too_long(name):
        return len(name) > 20
    def __init__(self, name, model):
        self.name = name
        self.model = model
        self.__health = 50
    def __str__(self):
        return f"У {self.name} {self.__health}% здоровья]"
    def __len__(self):
        return self.guns_count
    def __eq__(self, other):
        return self.name == other.name
    def check_conditions(self):
        return self.__health 
    def receive_repair(self):
        self.__health = 100
    def take_damage(self, ammount):
        self.__health -= ammount
        if self.__health < 0:
            self.__health = 0
    def report(self):
        print(f"Дрон {self.name} системы чисты, к полету готов!")
class BattleDrone(Drone):
    def __init__(self, name, model, gun_type):
        super().__init__(name, model)
        self.gun_type = gun_type
        def report(self):
            print(f"Боевой дрон {self.name} перезарядил {self.gun_type}!")
class RepairStation:
    def fix(self, robot):
        robot.receive_repair()
        robot.report()
my_drone = BattleDrone("Alfa", "X-100", "Laser")
my_drone.take_damage(30)
print(my_drone.check_conditions())
station = RepairStation()
station.fix(my_drone)
print(my_drone.check_conditions())
class CleanerBot(Drone):
    def move(self):
        print(f"Робот-пылесос едет по ковру и сосет пыль")
class FlyBot(Drone):
    def move(self):
        print(f"Дрон взлетает и кружит в небе")
class SpiderBot(Drone):
    def move(self):
        print(f"Робот-паук цепляется лапами за стены")
fleet = [CleanerBot("Сеня", "В1"), FlyBot("Глаз", "С1"), SpiderBot("Гоша", "Д1")]
for i in fleet:
    i.move() 
class ScoutDrone(Drone):
    pass
print(ScoutDrone.status)
ScoutDrone.status = "Разведка"
print(Drone.status)
print(Drone.is_name_too_long("ОченьДлинноеИмяДляРобота123"))
d = Drone("Сеня", "100")
print(d.is_name_too_long("Тест"))