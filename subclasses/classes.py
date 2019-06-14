from animal import Animal


class Herbivore(Animal):
    def __init__(self, *args, **kwargs):
        super(Herbivore, self).__init__(args, kwargs)
        # tb funciiona super().__init__(args, kwargs)
        self.food_type = "plants"


class Carnivore(Animal):
    def __init__(self, *args, **kwargs):
        super(Carnivore, self).__init__(args, kwargs)
        # tb funciiona super().__init__(args, kwargs)
        self.food_type = "animals"

class Omnivore(Animal):
    pass


class Lion(Carnivore):
    pass


class Man(Carnivore):
    pass
