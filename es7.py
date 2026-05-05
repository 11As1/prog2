class Stack:
    def __init__(self):
        self.__data = []

    def push(self, item):
        self.__data.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.__data.pop()

    def peek(self):
        if self.isEmpty():
            raise IndexError("empty stack")
        return self.__data[-1]

    def isEmpty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def __repr__(self):
        return f"Stack({self.__data})"
