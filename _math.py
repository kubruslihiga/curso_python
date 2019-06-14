class Math:
    pi = 3.14

    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def sub(x, y):
        return x - y

    def mul(x, y):
        return x * y

    def div(x, y):
        if y == 0:
            raise ValueError("Divisor não pode ser 0")
        return x / y

    @classmethod
    def deg_to_rad(cls, x):

        pass

    @classmethod
    def rad_to_deg(cls, x):
        pass
