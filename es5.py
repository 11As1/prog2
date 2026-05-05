class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta  = eta

    def presentati(self):
        return f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni."
    
    def fai_presentare(persona):
        print(persona.presentati())   # non sa e non deve sapere il tipo


class Studente(Persona):
    def __init__(self, nome, eta, matricola, voto):
        super().__init__(nome, eta)
        self.matricola = matricola
        self.voto      = voto

    def presentati(self):
        return f"Sono {self.nome}, matricola {self.matricola}, voto medio {self.voto}."

class Insegnante(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.materia = materia

    def presentati(self):
        return f"Sono il prof. {self.nome}, insegno {self.materia}."

class Bidello(Persona):
    def __init__(self, nome, eta, piano):
        super().__init__(nome, eta)
        self.piano = piano

def presentati(self):
    return f"Sono {self.nome}, mi occupo del piano {self.piano}."

   