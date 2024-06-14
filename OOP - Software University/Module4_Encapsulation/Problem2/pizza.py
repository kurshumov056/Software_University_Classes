

class Pizza:

    def __init__(self, name:str, dough:Dough, toppings_capacity:int, toppings:dict):
        self.name = name
        self.dough = dough
        self.toppings_capacity = toppings_capacity
        self.toppings = toppings



    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("The name cannot be an empty string")


    @property
    def dough(self):
        return self.__dough

    @dough.setter
    def dough(self, value):
        if value == None:
            raise ValueError("You should add dough to the pizza")
        self.dough = value


    @property
    def toppings_capacity(self):
        return self.__toppings_capacity

    @toppings_capacity.setter
    def toppings_capacity(self,value):
        if value <= 0:
            raise ValueError("The topping's capacity can not be less or equal to zero")
        self.__toppings_capacity = value


    @property
    def toppings(self):
        return self.__toppings

    @toppings.setter
    def toppings(self, value):
        #FINISH

