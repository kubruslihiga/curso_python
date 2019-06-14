# Exemplo de map
lista = [1, 2, 3, 4, 5, 6, 7]

def sqrt(x):
    return x*x

print('map : sqrt : ', list(map(sqrt, lista)))

#Reduce
from functools import reduce

def add(x, y):
    print(x, "+", y)
    return x + y

# (1 + 2) + (3 + 4) + (5 + 6) + 7 = 28
print('reduce = 28 : is ok? => ', reduce(add, lista) == 28)
# (1 + 2) + (3 + 4) = 10
print('reduce = 10 : is ok? => ', reduce(add, [1, 2, 3, 4]) == 10)

#Filter
lista = [None, 1, 2, 3, None, 4]

def gt(x):
    """greater than."""
    if x:
        return x > 2
    return False

print('filter, remover None: ', list(filter(None, lista))) #saparada retorna iteradores, não uma lista nova
print('filter, gt > 2 only:', list(filter(gt, lista)))

#Lambda
print('sqrt: ', list(map(lambda x : x*x, [1, 2, 3, 4, 5])))

k = [(1, 2), (3, 4)]
# Colocando a função, gerada por lambda em uma variável!
sum_up = lambda x : x[0] + x[1]
r = list(map(sum_up, k))
print(f'Soma de {k}: ', r)

function_lambda = lambda a : "Eita string" if type(a) is str else "Nao eh string"
print(list(map(function_lambda, ["teste", "teste2", 1, True, None, { "dicionario" : "loco"}])))

x = 0
a = True if x > 0 else True if x == 0 else False
print(a)

#Closure
def master(x):
    y = 2
    def slave():
        return x + y
    return slave
closure = master(5)
print('resultado: ', closure())

def master(x):
    def slave(y):
        return x + y
    return slave
closure = master(5)
print('resultado: ', closure(8))
print('resultado muito loco', master(5)(8))