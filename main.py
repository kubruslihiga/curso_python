# from orientacao_objeto import Animal
from animal import Animal as MyAnimal
from subclasses.classes import Herbivore, Man
from static_or_class.classes import Logger, Math
from rect import Rect

# from sys import argv
# import orientacao_objeto
# import orientacao_objeto as oop

if __name__ == "__main__":
    """animal = MyAnimal(gender=False, age=25)
    print(animal.age)
    animal.walk()
    print(animal.species)
    # delattr(animal, "species")
    print(getattr(animal, "hungry"))
    delattr(animal, "age")
    print(getattr(animal, "age", "idade removida"))
    print(animal.walking is True)

    herbivore = Herbivore()
    print(herbivore.walking)
    man = Man(legs=2)
    print(man.food_type)
    print(man.legs)
    Logger.info("Verificando... info")
    print(f"Classmethod execution: {Math.add(3, 4)}")"""
    rect = Rect(20, 30)
    print(rect.area())
    rect.__dir__
    a = [1, 2, 3, 4, 5, 6, 7]
    print(type(a))
    print(*a)
