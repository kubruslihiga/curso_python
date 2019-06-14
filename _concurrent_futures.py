from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import math

NUMBERS = range(0, 2)


def cpu_heavy(x):
    count = 0
    for i in range(x ** 2):
        count += i ** 2


def threading_example(fn=cpu_heavy, chunksize=100):
    """Threaded version: 8 threads."""
    items = []
    # Melhores práticas sugerem que max_workers para thread deve ser n = 2 * num_cores
    with ThreadPoolExecutor(max_workers=8) as executor:
        items = executor.map(fn, NUMBERS, chunksize=chunksize)
    return list(items)


def processing_example(fn=cpu_heavy, chunksize=100):
    """Multiprocessed version: 4 'threads'."""
    items = []
    # Melhores práticas sugerem que max_workers para process deve ser n = num_cores
    with ProcessPoolExecutor(max_workers=4) as executor:
        items = executor.map(fn, NUMBERS, chunksize=chunksize)
    return list(items)


def normal_example(fn=cpu_heavy):
    """Single threaded version."""
    items = []
    for i in NUMBERS:
        items.append(fn(i))
    return items


ex1 = threading_example()
ex2 = processing_example()
ex3 = normal_example()
print(ex1 == ex2)
print(ex1 == ex3)
print(ex2 == ex3)
