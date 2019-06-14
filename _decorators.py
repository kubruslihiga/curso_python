def decorator(fn):
    def wrapper(*args, **kwargs):
        print("Before function...")
        z = fn(*args, **kwargs)
        print("After function...")
        return z

    return wrapper


def soma(x, y):
    return x + y


# Without sintatic sugar
dec = decorator(soma)
print(dec(10, 2))


@decorator
def subtracao(x, y):
    return x - y


print(subtracao(10, 2))

# Este import
import functools


def dec(fn):
    # Esta chamada ao decorador da functools
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        z = fn(*args, **kwargs)
        return z

    return wrapper


@dec
def mul(x, y):
    return x * y


@decorator
def div(x, y):
    return x / y


print("Example using functools:", mul.__name__)
print("Example NOT using functools:", div.__name__)

# multiplos decoradores
def first(fn):
    # Esta chamada ao decorador da functools
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print("First decorator!")
        return fn(*args, **kwargs)

    return wrapper


def second(fn):
    # Esta chamada ao decorador da functools
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        print("Second decorator!")
        return fn(*args, **kwargs)

    return wrapper


@second
@first
def func():
    return "My function"


print(func())


# Parametro no decorador
def function(add):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kwargs):
            print(f"value of add param: {add}")
            return fn(*args, **kwargs) + add

        return wrapper

    return decorator


@function(add=5)
def parametros(x, y):
    return x + y


print("Total sum:", parametros(0, 0))

