
'''
food = Food("Apple")
drink = Drink("Water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
print(repo.products)
print(repo.find("water"))
repo.find("apple").decrease(5)
print(repo)

'''

from Project.food import Food
from Project.drink import Drink
from Project.product_repository import ProductRepository
from Project.drink import Drink


food = Food("Apple")
drink = Drink("Water")
repo = ProductRepository()
repo.add(food)
repo.add(drink)
result = ''
for product in repo.products:
    result += product.name + '   '

print(result)
print(repo.find("Apple").decrease(5))



