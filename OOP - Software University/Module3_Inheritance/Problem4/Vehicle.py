

class Vehicle:

    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
  

    def drive(self, kilometers):
        self.kilometers = kilometers
        distance = self.fuel / self.fuel_consumption

        if distance >= self.kilometers:
            self.fuel -=  self.fuel_consumption * self.kilometers
            return f"Afet {self.kilometers} km you have {self.fuel} fuel left"