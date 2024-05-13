class Tragarz:
    def __init__(self, x, y, klub):
        self.punkt = (x, y)
        self.lista_sasiedztwa = []
        self.klub = klub

    def dodaj_relacje(self, punkt):
        self.lista_sasiedztwa.append(punkt)