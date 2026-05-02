class Scanner:
    def __init__(self, accuracy):
        self.accuracy = accuracy
    def __call__(self, target_name):
        return (f"Объект {target_name} просканирован с точностью {self.accuracy}%")
my_scanner = Scanner(85)
print(my_scanner("Грузовик"))
print(my_scanner("Стена"))