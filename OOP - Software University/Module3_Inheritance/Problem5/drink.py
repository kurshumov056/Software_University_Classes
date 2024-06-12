from Project.product import Product


class Drink(Product):
    
    def __init__(self, name, quantity=10):
        self.name = name 
        self.quantity = quantity 
        
        super().__init__(name, quantity)