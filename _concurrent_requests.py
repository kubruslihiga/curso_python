import requests
import datetime
import psutil
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


uris = [
    "https://www.google.com.br",
    "https://www.uol.com.br",
    "https://twitter.com",
    "https://facebook.com",
] * 10


def download(uri):
    r = requests.get(uri)
    return r.status_code


def executor(Executor, max_workers=2, chunk_size=100):
    with Executor(max_workers=mw) as executor:
        print(list(executor.map(download, uris)))


if __name__ == "__main__":
    print(f"Quantidade de processadores: {psutil.cpu_count()}")
    """with ThreadPoolExecutor(max_workers=8) as t:
        print("Inicio thread: ", datetime.datetime.today())
        result = t.map(download, uris)
        print(list(result))
        print("Fim thread: ", datetime.datetime.today())

    with ProcessPoolExecutor(max_workers=4) as p:
        print("Inicio process: ", datetime.datetime.today())
        result = p.map(download, uris)
        print(list(result))
        print("Fim process: ", datetime.datetime.today())"""

    MyExecutor = ThreadPoolExecutor
    mw = psutil.cpu_count()
    if MyExecutor == ThreadPoolExecutor:
        mw = mw * 2
    print(MyExecutor, mw)
    executor(MyExecutor, mw, chunk_size=100)
