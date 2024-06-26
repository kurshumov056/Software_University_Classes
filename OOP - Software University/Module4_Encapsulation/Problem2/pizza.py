from Project.dough import Dough
from Project.topping import Topping



class Pizza:

    def __init__(self, name:str, dough:Dough, toppings_capacity:int ):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = dict()



    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")
        self.__name = value


    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value is None:
            raise ValueError("You should add dough to the pizza")
        self.__dough = value


    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self,value):
        if value <= 0:
            raise ValueError("The topping's capacity can not be less or equal to zero")
        self.__toppings_capacity = value



    def add_topping(topping: Topping):
        if len(self.toppings) == self.toppings_capacity:
            raise ValueError("Not enough space for another topping")

        if topping.topping_type in self.toppings:
            self.toppings[topping.topping_type] += topping.weight

        else:
            self.toppings[topping.topping_type] = topping.weight

    def calculate_total_weight(self):
        return self.dough.weight + sum(self.toppings.values())


