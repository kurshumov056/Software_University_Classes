
from Project.BladeKnight import BladeKnight
from Project.DarkKnight import DarkKnight
from Project.DarkWizard import DarkWizard
from Project.Elf import Elf
from Project.Hero import Hero
from Project.Knight import Knight
from Project.MuseElf import MuseElf
from Project.SoulMaster import SoulMaster
from Project.Wizard import Wizard



hero = Hero("H", 4)
print(hero.username)
print(hero.level)
print(str(hero))
elf = Elf("E", 4)
print(str(elf))
print(elf.__class__.__bases__[0].__name__)
print(elf.username)
print(elf.level)



