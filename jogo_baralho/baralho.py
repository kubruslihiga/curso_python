from carta import Carta


class Baralho:
    __slots__ = ["cartas"]

    def __init__(self, cartas):
        self.cartas = cartas

    def embaralhar(self):
        print("Embaralhar")

    def dar_carta(self):
        print("Dar as cartas")


carta = Carta("as", "10")
baralho = Baralho([carta])
baralho.embaralhar()
baralho.dar_carta()
