#Un team di sicurezza è composto da tre analisti che si alternano nel monitoraggio di un sistema. Usa la classe CircularLinkedList per gestire i turni.

#1)   Aggiungi in ordine: "alice", "bob", "carlo"
#2)   Stampa la lista
#3)   Simula 6 turni con traverse(6) — verifica che la rotazione funziona
#4)   Un nuovo analista "diana" entra nel team — aggiungila dopo "bob"
#5)   Stampa la lista aggiornata
#6)   Simula altri 8 turni — verifica che "diana" è entrata nella rotazione
#7)   "bob" lascia il team — rimuovilo 
#8)   Stampa la lista aggiornata
#9)   Simula altri 6 turni — verifica che la rotazione continua senza "bob"
#10   Stampa quanti analisti sono nel team

class NodoC:
    def __init__(self, valore):
        self.valore = valore
        self.next   = None


class CircularLinkedList:
    def __init__(self):
        self.__testa = None
        self.__coda  = None
        self.__size  = 0

    def insertFirst(self, valore):
        nuovo = NodoC(valore)
        if self.isEmpty():
            self.__testa = nuovo
            self.__coda  = nuovo
            nuovo.next   = nuovo
        else:
            nuovo.next       = self.__testa
            self.__coda.next = nuovo
            self.__testa     = nuovo
        self.__size += 1

    def insertLast(self, valore):
        nuovo = NodoC(valore)
        if self.isEmpty():
            self.__testa = nuovo
            self.__coda  = nuovo
            nuovo.next   = nuovo
        else:
            nuovo.next       = self.__testa
            self.__coda.next = nuovo
            self.__coda      = nuovo
        self.__size += 1

    def insertAfter(self, valore_riferimento, nuovo_valore):
        if self.isEmpty():
            raise IndexError("lista vuota")
        corrente = self.__testa
        while True:
            if corrente.valore == valore_riferimento:
                if corrente == self.__coda:
                    self.insertLast(nuovo_valore)
                    return
                nuovo         = NodoC(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
            if corrente == self.__testa:
                break
        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def insertBefore(self, valore_riferimento, nuovo_valore):
        if self.isEmpty():
            raise IndexError("lista vuota")
        if self.__testa.valore == valore_riferimento:
            self.insertFirst(nuovo_valore)
            return
        corrente = self.__testa
        while corrente.next != self.__testa:
            if corrente.next.valore == valore_riferimento:
                nuovo         = NodoC(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def removeFirst(self):
        if self.isEmpty():
            raise IndexError("removeFirst da una lista vuota")
        valore = self.__testa.valore
        if self.__testa == self.__coda:
            self.__testa = None
            self.__coda  = None
        else:
            self.__testa     = self.__testa.next
            self.__coda.next = self.__testa
        self.__size -= 1
        return valore

    def removeLast(self):
        if self.isEmpty():
            raise IndexError("removeLast da una lista vuota")
        valore = self.__coda.valore
        if self.__testa == self.__coda:
            self.__testa = None
            self.__coda  = None
        else:
            corrente = self.__testa
            while corrente.next != self.__coda:
                corrente = corrente.next
            corrente.next = self.__testa
            self.__coda   = corrente
        self.__size -= 1
        return valore

    def peekFirst(self):
        if self.isEmpty():
            raise IndexError("lista vuota")
        return self.__testa.valore

    def peekLast(self):
        if self.isEmpty():
            raise IndexError("lista vuota")
        return self.__coda.valore

    def traverse(self, passi):
        if self.isEmpty():
            raise IndexError("lista vuota")
        corrente = self.__testa
        for i in range(passi):
            print(f"passo {i + 1}: {corrente.valore}")
            corrente = corrente.next

    def isEmpty(self):
        return self.__testa is None

    def size(self):
        return self.__size

    def __repr__(self):
        if self.isEmpty():
            return "CircularLinkedList([])"
        elementi = []
        corrente = self.__testa
        while True:
            elementi.append(str(corrente.valore))
            corrente = corrente.next
            if corrente == self.__testa:
                break
        return "CircularLinkedList([" + " -> ".join(elementi) + " -> ...])"



team=CircularLinkedList()

print("\n1) Inserimento analisti")
team.insertLast("alice")
team.insertLast("bob")
team.insertLast("carlo")
print("Analisti aggiunti: alice, bob, carlo")

print("\n2) Lista team")
print(team)

print("\n3) Simulazione — 6 turni")
team.traverse(6)

print("\n4) Nuovo analista: diana (inserita dopo bob)")
team.insertAfter("bob", "diana")
print("diana aggiunta dopo bob")

print("\n5) Lista team aggiornata")
print(team)

print("\n6) Simulazione - 8 turni")
team.traverse(8)

print("\nbob lascia il team")
team.removeValue("bob")
print("bob rimosso")

print("\n8) Lista team aggiornata")
print(team)

print("\n9) Simulazione — 6 turni (senza bob)")
team.traverse(6)

print("\n10) Dimensione del team")
print("Analisti attivi nel team:", team.size())