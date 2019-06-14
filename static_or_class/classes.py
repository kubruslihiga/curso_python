class Logger:
    active = True

    @staticmethod
    def info(msg):
        print(f'This a message "{msg}"')


class Math:
    pi = 3.14

    @classmethod
    def add(cls, x, y):
        return x + y
