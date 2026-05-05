#inizializziamo la cronologia
history = ["google.com", "wikipedia.org", "python.org"]
forward = []
current = history.pop()                 #python.org, è la pagina che stiamo visitando

print(f"pagina corrente: {current}")    #python.org
print(f"cronologia: {history}")         #['google.com', 'wikipedia.org']

 #---torniamo indietro
forward.append(current)                 #salviamo python.org nella pila avanti
current = history.pop()                 #estraiamo wikipedia

print(f"pagina corrente: {current}")    #wikipedia.org
print(f"cronologia: {history}")         #google
print(f"avanti:{forward}")              #python.org

forward.append(current)                 #salviamo wikipedia.org
current=history.pop()                   #estraiamo google.com


print(f"pagina corrente: {current}") #wikipedia.org
print(f"cronologia: {history}")   #[google.com]
print(f"Avanti: {forward}")         #[python.org]

history.insert(1, "yahoo.com") #inserisce nel mezzo-una pila non lo prevede

history[0] #legge il fondo della pila-dovrebbe essere inaccessibile
history[1] #legge nel mezzo

history.remove("google.com") #rimuove per valore, non per posizione
history.pop(0)#rimuove dal fondo invece che dalla cima

del history[1]              #rimuove dal mezzo


history.sort()      # riordina tutto — distrugge completamente l'ordine LIFO
history.reverse()   # capovolge la pila



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

#inizializziamo le pile
history = Stack()
forward = Stack()

#visitiamo le pagine
history.push("google.com")
history.push("wikipedia.org")
history.push("python.org")

current = history.pop() #python.org -pagina corrente
print(f"pagina corrente: {current}") #python.org
print(f"cronologia:{history}") #stack(['google.com', 'wikipedia.org'])

#-- torniamo indietro
forward.push(current)
current=history.pop()

print(f"pagina corrente:{current}") #wikipedia.org
print(f"avanti: {forward}") #stack(['python.org'])

#--andiamo avanti
history.push(current)
current=forward.pop()

print(f"pagina corrente: {current}") #python.org

#--proviamo a violare l'incapsulamento
history.__data.append("yahoo.com")

# AttributeError: 'Stack' object has no attribute '__data'
history._Stack__data.append("yahoo.com")
# funziona — ma è un atto deliberato, non un errore accidentale