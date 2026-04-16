# classe e oggetto
class Persona():
    # attributo di classe: condiviso da tutte le istanze
    macchina="Renault Twingo"
    # costruttore
    def __init__(self, nome, cognome, eta):
        # attributi di oggetto:unici per ogni istanza
        self.nome=nome
        self.cognome=cognome
        self.eta=eta

    def saluta(self):
        return f"Ciao, sono {self.nome} {self.cognome}, ho {self.eta} anni e ho una {self.macchina}"

# istanzio due oggetti dalla stessa classe
p1=Persona("Lucio", "Dalla", 50)
p2=Persona("Vasco", "Rossi", 72)

print(p1.saluta()) 
print(p2.saluta())


# Incapsulamento

class Persona():
    macchina="Renault Twingo"

    def __init__(self,nome,cognome,eta):
        self.nome=nome
        self.cognome=cognome
        self.__eta=eta  # attributo privato: non accessibile direttamente dall'esterno

    def saluta(self):
        return f"Ciao, sono {self.nome} {self.cognome}, ho {self.__eta} anni e ho una {self.macchina}"

    # metodo getter: unico modo corretto per leggere l'età dall'esterno
    def get_eta(self):
        return self.__eta

    # metodo setter: unico modo corretto per modificare l'età dall'esterno
    # include validazione: impedisce valori non validi
    def set_eta(self, nuova_eta):
        if nuova_eta<0:
            print("L'età non può essere negativa")
        elif nuova_eta>150:
            print("Impossibile")
        else:
            self.__eta=nuova_eta

p1=Persona("Lucio","Dalla",50)

print(p1.get_eta())       #50  (accesso corretto tramite getter)
p1.set_eta(51)            #modifica corretta tramite setter
print(p1.get_eta())       #51

p1.set_eta(-5)            #L'età non può essere negativa.
print(p1.__eta)           #AttributeError: non accessibile direttamente


#Ereditarietà

#classe genitore
class Persona():
    macchina="Renault Twingo"

    def __init__(self,nome,cognome,eta):
        self.nome=nome
        self.cognome=cognome
        self.eta=eta

    def saluta(self):
        return f"Ciao, sono {self.nome} {self.cognome}, ho {self.eta} anni"

#studente eredita da Persona e aggiunge attributi e metodi propri
class Studente(Persona):
    def __init__(self,nome,cognome,eta,corso):
        super().__init__(nome,cognome,eta)  # richiama il costruttore di Persona
        self.corso=corso                    # attributo aggiuntivo

    def studia(self):
        return f"{self.nome} sta studiando {self.corso}"

#lavoratore eredita da Persona e aggiunge attributi e metodi propri
class Lavoratore(Persona):
    def __init__(self,nome,cognome,eta,azienda):
        super().__init__(nome,cognome,eta)
        self.azienda=azienda

    def lavora(self):
        return f"{self.nome} lavora in {self.azienda}"

s1=Studente("Lucio","Dalla",20,"Informatica")
l1=Lavoratore("Vasco","Rossi",45,"Sony")

print(s1.saluta())   #metodo ereditato da Persona
print(s1.studia())   #metodo di Studente
print(l1.saluta())   #metodo ereditato da Persona
print(l1.lavora())   #metodo di Lavoratore



#Polimorfismo

class Persona():
    def __init__(self,nome,cognome,eta):
        self.nome=nome
        self.cognome=cognome
        self.eta=eta

    # metodo che verrà sovrascritto nelle sottoclassi
    def presentati(self):
        return f"Sono {self.nome} {self.cognome}"

class Studente(Persona):
    def __init__(self,nome,cognome,eta,corso):
        super().__init__(nome,cognome,eta)
        self.corso=corso

    # override: stessa firma del metodo genitore, comportamento diverso
    def presentati(self):
        return f"Sono {self.nome} {self.cognome} studente di {self.corso}"

class Lavoratore(Persona):
    def __init__(self,nome,cognome,eta,azienda):
        super().__init__(nome,cognome,eta)
        self.azienda=azienda

    # override: stessa firma, comportamento diverso ancora
    def presentati(self):
        return f"Sono {self.nome} {self.cognome}, lavoro in {self.azienda}"

persone = [
    Persona("Mario", "Rossi", 40),
    Studente("Lucio", "Dalla", 20, "Informatica"),
    Lavoratore("Vasco", "Rossi", 45, "Sony")
]

# il ciclo non sa di che tipo è ogni oggetto
# chiama .presentati() e ognuno risponde a modo suo
for p in persone:
    print(p.presentati())


# Astrazione
from abc import ABC, abstractmethod

# classe astratta: definisce il contratto che le sottoclassi devono rispettare
# non può essere istanziata direttamente
class Persona(ABC):
    def __init__(self,nome,cognome,eta):
        self.nome=nome
        self.cognome=cognome
        self.eta=eta

    # metodo astratto: ogni sottoclasse è obbligata a implementarlo
    @abstractmethod
    def presentati(self):
        pass

    @abstractmethod
    def attivita_principale(self):
        pass

class Studente(Persona):
    def __init__(self,nome,cognome,eta,corso):
        super().__init__(nome,cognome,eta)
        self.corso=corso

    def presentati(self):
        return f"Sono {self.nome} {self.cognome}, ho {self.eta} anni"

    def attivita_principale(self):
        return f"{self.nome} studia {self.corso}"

class Lavoratore(Persona):
    def __init__(self,nome,cognome,eta,azienda):
        super().__init__(nome,cognome,eta)
        self.azienda=azienda

    def presentati(self):
        return f"Sono {self.nome} {self.cognome}, ho {self.eta} anni"

    def attivita_principale(self):
        return f"{self.nome} lavora in {self.azienda}"

# questa funzione lavora con qualsiasi Persona
def scheda_persona(p: Persona):
    print(p.presentati())
    print(p.attivita_principale())

s1=Studente("Lucio","Dalla",20,"Informatica")
l1=Lavoratore("Vasco","Rossi",45,"Sony")

scheda_persona(s1)

scheda_persona(l1)

p=Persona("Mario","Rossi",30)