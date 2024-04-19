
class Tragarz:
    def __init__(self, id_klubu, czy_rece_z_przodu):
        self.rece_z_przodu = czy_rece_z_przodu
        self.id_ulubionego_klubu = id_klubu
    
    def __str__(self):
        return f"Klub: {self.id_ulubionego_klubu}, rece z przodu: {self.rece_z_przodu}"
    