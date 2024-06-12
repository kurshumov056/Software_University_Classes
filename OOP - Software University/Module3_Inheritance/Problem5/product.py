
class Product:

    def __init__(self, name: str, quantity: int):

        self.name = name
        self.quantity = quantity
        

    def decrease(self, quantity: int):
        
        if quantity <= int(self.quantity):
            self.quantity -= quantity 
            return f"Decrease succesful, Remaining {self.name} quantity: {self.quantity}"

    def increase(self, quantity: int):
        pass
 