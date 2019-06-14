# gerado simples
def simple_gen(x):
    for y in range(x):
        yield y


m = simple_gen(10)
while True:
    try:
        print(next(m))
    except StopIteration as si:
        print(si)
        print("StopIteration : exception")
        break


# Exemplo de um gerador criado de objetos
class Cat:
    def __init__(self, name):
        self.name = name


def gerador_gatos(num):
    for i in range(num):
        yield Cat(f"Cat {i}")


gc = gerador_gatos(4)
print(next(gc).name)
print(next(gc).name)


def generator_mucho_loco(my_file):
    next_line = my_file.readline()
    while next_line is not None:
        yield next_line
        next_line = my_file.readline()


with open("file.txt", "r") as f:
    gml = generator_mucho_loco(f)
    print(next(gml))
    print(next(gml))

# outro gerador louco
# a = (_ for _ in range(10))
# print(next(a));print(next(a));print(next(a));print(next(a))

