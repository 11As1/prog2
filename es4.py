class Persona:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta  = eta

    def presentati(self):
        return f"Ciao, mi chiamo {self.nome} e ho {self.eta} anni."


class Studente(Persona):
    def __init__(self, nome, eta, matricola, voto):
        super().__init__(nome, eta)  # delega a Persona la parte comune
        self.matricola = matricola
        self.voto      = voto

    def studia(self):                # metodo nuovo, non esiste in Persona
        return f"{self.nome} sta studiando."

    def presentati(self):            # override: riscrive il metodo del genitore
        return f"Sono {self.nome}, matricola {self.matricola}, voto medio {self.voto}."


class Insegnante(Persona):
    def __init__(self, nome, eta, materia):
        super().__init__(nome, eta)
        self.materia = materia

    def insegna(self):
        return f"{self.nome} insegna {self.materia}."

    def presentati(self):
        return f"Sono il prof. {self.nome}, insegno {self.materia}."
