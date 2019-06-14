class Animal:
    species = None

    def __init__(self, legs=0, age=0, gender="female"):
        self.age = age
        self.gender = gender
        self.hungry = False
        self.walking = False
        self.legs = legs

    def eat(self):
        self.hungry = False

    def walk(self):
        self.walking = True

    def stop(self):
        self.walking = False

    # Built-in class Method to overload
    def __str__(self):
        return f"""{self.__class__.__name__}: 
    age: {self.age},
    gender: {self.gender},
    legs: {self.legs}"""


if __name__ == "__main__":
    from subclasses.classes import Carnivore
    animal = Animal()
    print(animal)
    c = Carnivore()
    print(c)
