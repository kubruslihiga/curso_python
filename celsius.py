class Celsius:
    def __init__(self, temperature=0):
        self.__temperature = temperature

    @property
    def temperature(self):
        return self.__temperature

    @temperature.setter
    def temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273. It's invalid.")
        self.__temperature = value


ct = Celsius()
ct.temperature = 10
print(ct.temperature)
