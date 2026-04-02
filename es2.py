class Persona():
    def __init__(self, nome, cognome, eta):
        self.nome=nome
        self.cognome=cognome
        self.eta=eta
        

class Dottore(Persona):
    def __init__(self, nome, cognome, eta, specializzazione, matricola, stipendio, reparto, pazientiInCura):
        super().__init__(nome, cognome, eta)
        self.stipendio=stipendio
        self.specializzazione=specializzazione
        self.matricola=matricola
        self.reparto=reparto
        self.pazientiInCura=pazientiInCura

    def __str__(self):
        return (f"Nome={self.nome} Cognome={self.cognome} Eta={self.eta} "
                f"Stipendio={self.stipendio} "
                f"Specializzazione={self.specializzazione} "
                f"Matricola={self.matricola} Reparto={self.reparto}")

    def returnPazientiInCura(self):
        return f"Dottore {self.nome} {self.cognome}->ID pazienti in cura={self.pazientiInCura}"

    def aggiungiPaziente(self, id):
        self.pazientiInCura.append(id)


class Paziente(Persona):
    def __init__(self, nome, cognome, eta, gruppoSanguigno, patologie, id, allergie):
        super().__init__(nome, cognome, eta)
        self.id=id
        self.gruppoSanguigno=gruppoSanguigno
        self.patologie=patologie
        self.allergie=allergie
    
    def __str__(self):
        return f"Paziente-> Nome= {self.nome} Cognome={self.cognome} ID={self.id} Eta={self.eta} Gruppo sanguigno={self.gruppoSanguigno} patologie={self.patologie} allergie={self.allergie}"



dot1=Dottore("Dario", "Bianchi", 50, "Radiologia", "D001", 2000, "Radiologia", [])
dot2=Dottore("Andree", "Verdi", 40, "Farmacia", "D002", 2100, "Farmacia", [])

paz1=Paziente("Mario", "Rossi", 22, "0",["pat1","pat2"], "0001", ["all1"] )
paz2=Paziente("Luca", "Neri", 22, "AB", ["pat6"], "0002", ["all3"])

dot1.aggiungiPaziente(paz1.id)
dot2.aggiungiPaziente(paz2.id)
print(dot1)
print(dot2)
print(paz1)
print(paz2)
print(dot1.returnPazientiInCura())
print(dot2.returnPazientiInCura())