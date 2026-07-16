import random
import time
import ipaddress

class NodoBST:
    def __init__(self, valore):
        self.valore = valore
        self.left = None
        self.right = None


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

    def isEmpty(self):
        return self.__radice is None



class Nodo:
    def __init__(self, valore):
        self.valore = valore
        self.next = None


class Queue:
    def __init__(self):
        self.__testa = None
        self.__coda = None
        self.__size = 0

    def enqueue(self, valore):
        nuovo = Nodo(valore)

        if self.__coda is None:
            self.__testa = self.__coda = nuovo
        else:
            self.__coda.next = nuovo
            self.__coda = nuovo

        self.__size += 1

    def dequeue(self):
        if self.isEmpty():
            raise IndexError("Queue vuota")

        valore = self.__testa.valore
        self.__testa = self.__testa.next

        if self.__testa is None:
            self.__coda = None

        self.__size -= 1
        return valore

    def isEmpty(self):
        return self.__testa is None

    def size(self):
        return self.__size


def ipToInt(ip: str) -> int:
    """Converte un IP in intero."""
    return int(ipaddress.ip_address(ip))


def intToIp(n: int) -> str:
    """Converte un intero in IP."""
    return str(ipaddress.ip_address(n))



random.seed(42)

IP_MIN = int(ipaddress.ip_address("1.0.0.0"))
IP_MAX = int(ipaddress.ip_address("223.255.255.255"))


blacklist_ip = [
    str(ipaddress.ip_address(random.randint(IP_MIN, IP_MAX)))
    for _ in range(1000)
]

blacklist_interi = [ipToInt(ip) for ip in blacklist_ip]

bst_blacklist = BST()

for ip in blacklist_interi:
    bst_blacklist.insert(ip)

print("==========================================")
print("BLACKLIST")
print("==========================================")
print(f"Numero IP: {len(blacklist_interi)}")
print(f"Esempio: {blacklist_ip[0]} -> {blacklist_interi[0]}")


ip_bloccati = random.sample(blacklist_interi, 10)

ip_permessi = []

while len(ip_permessi) < 10:
    nuovo = random.randint(IP_MIN, IP_MAX)

    if nuovo not in blacklist_interi and nuovo not in ip_permessi:
        ip_permessi.append(nuovo)

pacchetti = ip_bloccati + ip_permessi
random.shuffle(pacchetti)

queue = Queue()

for ip in pacchetti:
    queue.enqueue(ip)

print("\n==========================================")
print("PACCHETTI IN ARRIVO")
print("==========================================")
print(f"Totale pacchetti: {queue.size()}")


bloccati = 0
permessi = 0

print("\nVerifica pacchetti:\n")

while not queue.isEmpty():

    ip = queue.dequeue()

    if bst_blacklist.search(ip):
        print(f"{intToIp(ip):15} --> BLOCCATO")
        bloccati += 1
    else:
        print(f"{intToIp(ip):15} --> PERMESSO")
        permessi += 1


print("\n==========================================")
print("RIEPILOGO FINALE")
print("==========================================")

print(f"Pacchetti bloccati : {bloccati}")
print(f"Pacchetti permessi : {permessi}")


inizio = time.perf_counter()

for ip in pacchetti:
    bst_blacklist.search(ip)

tempo_bst = time.perf_counter() - inizio

inizio = time.perf_counter()

for ip in pacchetti:
    ip in blacklist_interi

tempo_lista = time.perf_counter() - inizio

print("\n==========================================")
print("CONFRONTO PRESTAZIONI")
print("==========================================")

print(f"Tempo ricerca BST   : {tempo_bst:.10f} secondi")
print(f"Tempo ricerca Lista : {tempo_lista:.10f} secondi")

if tempo_bst < tempo_lista:
    print(f"\nIl BST è {tempo_lista / tempo_bst:.2f} volte più veloce della lista.")
elif tempo_lista < tempo_bst:
    print(f"\nLa lista è {tempo_bst / tempo_lista:.2f} volte più veloce del BST.")
else:
    print("\nLe due strutture hanno prestazioni simili.")