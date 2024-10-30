import random
import ModuleWeightConverter
from ModuleWeightConverter import lbs_to_kilo
from ModuleWeightConverter import kilo_to_lbs
from utils.Shipping import calShipping
from pathlib import Path

print(lbs_to_kilo(100))
print(kilo_to_lbs(100))
ModuleWeightConverter.printStr()

print(f'Max Number: {ModuleWeightConverter.findMaxNumber([23,1,4,67,8,11,45,99])}')

calShipping()

class Dice:
    def rollDice(self):
        first = random.randint(1,6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.rollDice())

path = Path("Test")
print(path.exists())
if path.exists():
    path.rmdir()

path1 = Path()
for file in path1.glob("*.py"):
    print(file)