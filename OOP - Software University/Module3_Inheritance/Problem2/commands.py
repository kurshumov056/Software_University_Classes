

from Project.Animal import Animal
from Project.Bear import Bear
from Project.Gorilla import Gorilla
from Project.Lizard import Lizard
from Project.Mammal import Mammal
from Project.Reptile import Reptile
from Project.Snake import Snake
 

mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
