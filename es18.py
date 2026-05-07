#Usando le classi BST e LinkedList che abbiamo costruito durante il corso confronta il tempo di ricerca tra le due strutture dati.

#1). Genera una lista di 1000 numeri casuali tra 1 e 10k usando una list comprehnsion
#2). Inserisci gli stessi 1000 numeri sia nella lista linkata che nel BST
#3). Scegli un numero da cercare - prendi il 500esimo elemento della lista generata
#4). Misura il tempo di ricerca nella lista collegata usando time.perf_counter()
#5). Misura il tempo di ricerca nel BST usando time.perf_counter()
#6). Stampa i due tempi e calcola quante volte una struttura è più veloce dell'altra


import random
import time

class NodoBST:
    def __init__(self, valore):
        self.valore = valore
        self.left   = None
        self.right  = None

class BST:
    def __init__(self):
        self.__radice = None

    def insert(self, valore):
        if self.__radice is None:
            self.__radice = NodoBST(valore)
        else:
            self.__insertRicorsivo(self.__radice, valore)

    def __insertRicorsivo(self, nodo, valore):
        if valore < nodo.valore:
            if nodo.left is None:
                nodo.left = NodoBST(valore)
            else:
                self.__insertRicorsivo(nodo.left, valore)
        else:
            if nodo.right is None:
                nodo.right = NodoBST(valore)
            else:
                self.__insertRicorsivo(nodo.right, valore)

    def search(self, valore):
        return self.__searchRicorsivo(self.__radice, valore)

    def __searchRicorsivo(self, nodo, valore):
        if nodo is None:
            return False
        if nodo.valore == valore:
            return True
        if valore < nodo.valore:
            return self.__searchRicorsivo(nodo.left, valore)
        else:
            return self.__searchRicorsivo(nodo.right, valore)

    def inOrder(self):
        elementi = []
        self.__inOrderRicorsivo(self.__radice, elementi)
        return elementi

    def __inOrderRicorsivo(self, nodo, elementi):
        if nodo is None:
            return
        self.__inOrderRicorsivo(nodo.left, elementi)
        elementi.append(nodo.valore)
        self.__inOrderRicorsivo(nodo.right, elementi)

    def isEmpty(self):
        return self.__radice is None

    def __repr__(self):
        return f"BST(inOrder={self.inOrder()})"


class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.next   = None

class LinkedList:
    def __init__(self):
        self.__testa = None
        self.__size  = 0

    def insertLast(self, valore):
        nuovo = Nodo(valore)
        if self.__testa is None:
            self.__testa = nuovo
        else:
            corrente = self.__testa
            while corrente.next is not None:
                corrente = corrente.next
            corrente.next = nuovo
        self.__size += 1

    def search(self, valore):
        """Ricerca lineare: scorre tutta la lista finché non trova il valore."""
        corrente = self.__testa
        while corrente is not None:
            if corrente.valore == valore:
                return True
            corrente = corrente.next
        return False

    def isEmpty(self):
        return self.__testa is None

    def size(self):
        return self.__size



random.seed(42)
numeri=[random.randint(1, 10000) for _ in range(1000)]

print("Confronto linkedlist e BST")
print(f"\nLista generata -> {len(numeri)} numeri casuali (1-10000)")
print(f"Primi 5 valori   : {numeri[:5]}")


ll=LinkedList()
bst=BST()

for n in numeri:
    ll.insertLast(n)
    bst.insert(n)

print(f"\nValori inseriti")

target=numeri[499]
print(f"\n500esimo elemento {target}")


ripetizioni=10000
start_ll=time.perf_counter()
for _ in range(ripetizioni):
    ll.search(target)
end_ll=time.perf_counter()

tempo_ll=(end_ll-start_ll)/ripetizioni

start_bst=time.perf_counter()
for _ in range(ripetizioni):
    bst.search(target)
end_bst=time.perf_counter()

tempo_bst=(end_bst-start_bst)/ripetizioni

print("RISULTATI")
print(f"LinkedList  : {tempo_ll:} s  ({tempo_ll * 1e6:} µs)")
print(f"BST         : {tempo_bst:} s  ({tempo_bst * 1e6:} µs)")

if tempo_ll>tempo_bst:
    rapporto=tempo_ll/tempo_bst
    print(f"\nIl BST è {rapporto:.1f}* più veloce della LinkedList")
    print(f"   (trovato in O(log n) vs O(n))")
else:
    rapporto=tempo_bst/tempo_ll
    print(f"\nLa LinkedList è {rapporto:.1f}* più veloce del BST")

import math
n=1000
print(f"LinkedList O(n)-> {n} confronti")
print(f"BST O(log n)->{math.log2(n):} confronti")
print(f"Speedup teorico atteso: {n / math.log2(n):}x")
