class Fibonacci:
    def __init__(self, number):
        self.start(number)
    
    def start(self, number):
        self.number = number + 1
        self.__index = 0
        self.__j = 1
        self.__i = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        # Fibonacci
        t = self.__index
        # from 2 to number + 1
        if 1 < self.__index <= self.number:
            t = self.__i + self.__j
            self.__i = self.__j
            self.__j = t
        # Iterator
        if self.__index == self.number:
            raise StopIteration
        self.__index += 1
        return t

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144,233, 377, 610, 987
# 1597, 2584, 4181, 6765, 10946

fib = Fibonacci(21)
nums = []
for i in fib:
    nums.append(i)
print('Fibonacci Sequence: ')
print(nums)


class PythonIt:
    def __init__(self):
        self.__num_times = 5
    def __iter__(self):
        return self
    def __next__(self):
        if self.__num_times <= 0:
            raise StopIteration
        self.__num_times -= 1
        return "a" * self.__num_times

if __name__ == "__main__":
    it = PythonIt()
    for x in it:
        print(x)