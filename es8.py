class Notifiche:
    def __init__(self):
        self._pila=[]

    def arriva(self, messaggio):
        self._pila.append(messaggio)

    def leggi(self):
        if not self._pila:
            print("nessuna notifica")
        else:
            messaggio=self._pila.pop()
            print(f"letta: {messaggio}")

    def prossima(self):
        if not self._pila:
            print("nessuna notifica in cima")
        else:
            print(f"in cima: {self._pila[-1]}")


notifiche=Notifiche()

notifiche.arriva("WhatsApp: Ciao!")
notifiche.arriva("Gmail: Hai un nuovo messaggio")
notifiche.arriva("Instagram: Ti hanno taggato")

notifiche.prossima()
notifiche.leggi()
notifiche.leggi()
notifiche.leggi()
notifiche.leggi()