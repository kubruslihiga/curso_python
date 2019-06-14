from multiprocessing import Pool


def f(x):
    x * x


if __name__ == "__main__":
    with Pool(2) as p:
        p.map(f, range(100000))
