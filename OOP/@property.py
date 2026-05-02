class SmartSensors:
    def __init__(self, _temperature):
        self.temp = _temperature 
    @property
    def temp(self):
        return self._temperature
    @temp.setter
    def temp(self, value):
        if not isinstance(value,(int, float)):
            print("Введите число!")
        elif value >= 80 or value <= -20:
            print("Внимание: опасный диапазон! Изменение отклонено")
        else:
            self._temperature = value
    @property
    def temp_status(self):
        if self.temp > 60:
            return("Горячо")
        else:
            return("Стабильно")
sensor = SmartSensors(25)
print(f"Текущая температура: {sensor.temp}")
sensor.temp = 70
print(f"Статус после нагрева: {sensor.temp_status}")
sensor.temp = 150
sensor.temp = "Слишком жарко"