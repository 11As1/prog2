#Usa la classe LinkedList per gestire la cronologia degli utenti che hanno modificato il file config.txt.
#1. Registra in ordine le prime modifiche: "admin", "mario", "sara"
#2. Stampa la cronologia
#3. "guest" ha modificato il file dopo "mario" — inseriscilo nella posizione corretta
#4. Stampa la cronologia
#5. "root" ha modificato il file per primo — inseriscilo prima di "admin"
#6. Stampa la cronologia
#7. "luca" ha modificato il file prima di "sara" — inseriscilo nella posizione corretta
#8. Stampa la cronologia
#9. La modifica più vecchia è stata archiviata — rimuovi il primo elemento
#10. Stampa la cronologia
#11. L'ultima modifica è stata annullata — rimuovi l'ultimo elemento
#12. Stampa la cronologia
#13. Stampa quante modifiche sono registrate
#14. Stampa chi ha effettuato la modifica più recente da processare senza rimuoverlo


class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.next   = None


class LinkedList:
    def __init__(self):
        self.__testa = None
        self.__size  = 0

    def insertFirst(self, valore):
        nuovo        = Nodo(valore)
        nuovo.next   = self.__testa
        self.__testa = nuovo
        self.__size += 1

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

    def insertAfter(self, valore_riferimento, nuovo_valore):
        corrente = self.__testa
        while corrente is not None:
            if corrente.valore == valore_riferimento:
                nuovo         = Nodo(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def insertBefore(self, valore_riferimento, nuovo_valore):
        if self.isEmpty():
            raise IndexError("lista vuota")
        if self.__testa.valore == valore_riferimento:
            self.insertFirst(nuovo_valore)
            return
        corrente = self.__testa
        while corrente.next is not None:
            if corrente.next.valore == valore_riferimento:
                nuovo         = Nodo(nuovo_valore)
                nuovo.next    = corrente.next
                corrente.next = nuovo
                self.__size += 1
                return
            corrente = corrente.next
        raise ValueError(f"{valore_riferimento} non trovato nella lista")

    def removeFirst(self):
        if self.isEmpty():
            raise IndexError("removeFirst da una lista vuota")
        valore       = self.__testa.valore
        self.__testa = self.__testa.next
        self.__size -= 1
        return valore

    def removeLast(self):
        if self.isEmpty():
            raise IndexError("removeLast da una lista vuota")
        if self.__testa.next is None:
            valore       = self.__testa.valore
            self.__testa = None
            self.__size -= 1
            return valore
        corrente = self.__testa
        while corrente.next.next is not None:
            corrente = corrente.next
        valore        = corrente.next.valore
        corrente.next = None
        self.__size -= 1
        return valore

    def peekFirst(self):
        if self.isEmpty():
            raise IndexError("lista vuota")
        return self.__testa.valore

    def isEmpty(self):
        return self.__testa is None

    def size(self):
        return self.__size

    def __repr__(self):
        elementi = []
        corrente = self.__testa
        while corrente is not None:
            elementi.append(str(corrente.valore))
            corrente = corrente.next
        return "LinkedList([" + " -> ".join(elementi) + "])"
    


cronologia=LinkedList()

cronologia.insertLast("admin")
cronologia.insertLast("mario")
cronologia.insertLast("sara")

print("Dopo le prime modifiche ")
print(cronologia)

cronologia.insertAfter("mario", "guest")

print("\nDopo inserimento di 'guest' dopo 'mario' ")
print(cronologia)

cronologia.insertBefore("admin", "root")

print("\nDopo inserimento di 'root' prima di 'admin' ")
print(cronologia)

cronologia.insertBefore("sara", "luca")

print("\nDopo inserimento di 'luca' prima di 'sara' ")
print(cronologia)

rimosso=cronologia.removeFirst()
print(f"\nModifica più vecchia archiviata '{rimosso}'")

print("Cronologia aggiornata ")
print(cronologia)

annullato=cronologia.removeLast()
print(f"\nUltima modifica annullata '{annullato}'")

print("Cronologia aggiornata")
print(cronologia)

print(f"\nModifiche registrate {cronologia.size()}")

print(f"Prossima modifica da processare '{cronologia.peekFirst()}'")