
from Project.product import Product


class ProductRepository(Product):

    def __init__(self):
        self.products = list()

    def add(self, product: Product):
        self.product = product
        
        if product not in self.products:
            self.products.append(self.product)

    def find(self, product_name: str):
        for section in self.products:
            if str(section.name) == product_name:
                return section    

    def remove(self, product_name):
        for i in range(0, len(self.products)):
            section = self.product[i]
            if name == section.name:
                del section


    def __repr__(self):
        result = " "
         

        for x,y in zip(self.products.name, self.products.quantity):
            result += f"Product Name: {x} Product Quantity: {y}"
        return result 



