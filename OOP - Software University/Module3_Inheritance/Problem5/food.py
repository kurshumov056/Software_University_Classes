from Project.product import Product


class Food(Product):
    

    def __init__(self, name, quantity = 15):
        self.name = name
        self.quantity = quantity 
        super().__init__(name, quantity)