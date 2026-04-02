class Persona():
    def __init__(self, nome, cognome, eta):
        self.nome=nome
        self.cognome=cognome
        self.eta=eta



class Dottore(Persona):
    def __init__(self, nome, cognome, eta, specializzazione, stipendio):
        super().__init__(nome, cognome, eta)
        self.specializzazione=specializzazione
        self.stipendio=stipendio

    def __str__(self):
        return f"Nome= {self.nome} Cognome={self.cognome} Eta={self.eta} Specializzazione={self.specializzazione} Stipendio={self.stipendio}"



class Paziente(Persona):
    def __init__(self, nome, cognome, eta, gruppoSanguigno, patologie):
        super().__init__(nome, cognome, eta)
        self.gruppoSanguigno=gruppoSanguigno
        self.patologie=patologie
    
    def __str__(self):
        return f"Nome= {self.nome} Cognome={self.cognome} Eta={self.eta} Gruppo sanguigno={self.gruppoSanguigno} patologie={self.patologie}"




dot1=Dottore("Dario", "Bianchi", 50, "Radiologia", 2000)
dot2=Dottore("Andree", "Verdi", 40, "Ginecologia", 2100)

paz1=Paziente("Mario", "Rossi", 22, "0",["pat1","pat2"] )
paz2=Paziente("Luca", "Neri", 22, "AB", ["pat6"])


print(dot1)
print(dot2)
print(paz1)
print(paz2)