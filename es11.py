from collections import deque

class Queue:
    def __init__(self):
        self.__data = deque()         # deque privato — O(1) per enqueue e dequeue

    def enqueue(self, item):
        self.__data.append(item)      # aggiunge in fondo

   
    def dequeue(self):
        if self.isEmpty():
            raise IndexError("dequeue from empty queue")
        return self.__data.popleft()  # rimuove dalla testa — O(1)

    def peek(self):
        if self.isEmpty():
            raise IndexError("empty queue")
        return self.__data[0]         # guarda la testa senza rimuoverla

    def isEmpty(self):
        return len(self.__data) == 0

    def size(self):
        return len(self.__data)

    def __repr__(self):
        return f"Queue({list(self.__data)})"

fila=Queue()

clientiIniziali=["Mario", "Giulia", "Tonino", "Rosa"]
for cliente in clientiIniziali:
    fila.enqueue(cliente)

prossimo=fila.dequeue()
print(f"Servo {prossimo}")

fila.enqueue("Enzo")

print(f"Persone in attesa: {fila.size()}")
while not fila.isEmpty():
    clientServito = fila.dequeue()
    print(f"Servo {clientServito}")

print("Fila esaurita")