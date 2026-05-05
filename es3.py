class Studente:

    # 1. COSTRUTTORE — chiamato automaticamente alla creazione
    def __init__(self, nome, eta):
        self.nome = nome   # 2. ATTRIBUTI — dati propri di ogni oggetto
        self.eta  = eta

    # 3. METODI — azioni che l'oggetto sa fare
    def saluta(self):
        return f"Ciao, sono {self.nome}!"
    


s1=Studente("Banana Joe", 45)
print(s1.saluta())