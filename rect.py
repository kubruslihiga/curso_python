class Rect:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def area(self):
        return self.__x * self.__y
