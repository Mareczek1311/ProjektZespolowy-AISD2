class Klub:
    def __init__(self, nazwa):
        self.nazwaKlubu = nazwa
        self.dobreRelacje = set()
        #self.kosa = []
    
    def __str__(self):
        return f"{self.id} {self.nazwaKlubu}"
    
    def dodajDobraRelacje(self, klub):
        self.dobreRelacje.add(klub)
    
    #def dodajKose(self, klub):
    #   self.kosa.append(klub)
    
    def sprawdzRelacje(self, klub):
        if klub in self.dobreRelacje:
            return True
        return False