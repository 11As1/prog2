# inizializziamo la coda
queue = ["luca", "sara", "mario"]

# enqueue — aggiungiamo in fondo
queue.append("anna")
print(queue)   # ['luca', 'sara', 'mario', 'anna']

# dequeue — rimuoviamo dalla testa
primo = queue.pop(0)
print(primo)   # 'luca' — il primo entrato è il primo ad uscire
print(queue)   # ['sara', 'mario', 'anna']
