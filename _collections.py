from collections import namedtuple

Person = namedtuple("Person", ["name", "age", "gender"])
print("Type:", type(Person))

rodolfo = Person("Rodolfo", 36, "Masculino")
print("Type:", type(rodolfo))

print(rodolfo.name)

from collections import Counter

a = Counter({"a": 10, "b": 5, "c": 1})
b = Counter({"a": 1, "b": 2, "c": 0, "d": 15})

print("Type:", type(a))
print(a + b)

from dataclasses import dataclass


# Old class to mimic DataClass
class OldPoint:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"{self.__class__.__name__}(x={self.x}, y={self.y})"

    def __eq__(self, other):
        if other.__class__ is not self.__class__:
            return NotImplemented
        return other.x == self.x and other.y == self.y

    def draw(self):
        return (self.x, self.y)


# New Python 3.7 DataClass
@dataclass
class Point:
    x: float = 0.0
    y: float = 0.0

    def draw(self):
        return f"Drawing point at ({self.x}, {self.y})"


po0, po1 = OldPoint(), OldPoint()
pn0, pn1 = Point(), Point()
print(po0)
print(pn0)
print("Equals operation: ", po0 == po1)
print("Equals operation: ", pn0 == pn1)
print("Method call:", pn0.draw())

from dataclasses import dataclass
from typing import List


@dataclass
class Carta:
    rank: str
    naipe: str


@dataclass
class Baralho:
    cartas: List[Carta]


baralho = Baralho([Carta("Q", "Copa"), Carta("A", "Espada")])
print(baralho)
