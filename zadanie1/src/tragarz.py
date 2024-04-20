
class Tragarz:
    def __init__(self, id, id_klubu, czy_rece_z_przodu, indexY, start_lub_end=None):
        self.id = id
        self.rece_z_przodu = czy_rece_z_przodu
        self.id_ulubionego_klubu = id_klubu
        self.indexY = indexY
        self.start_lub_end = start_lub_end
    
    def __str__(self):
        return f"Klub: {self.id_ulubionego_klubu}, rece z przodu: {self.rece_z_przodu}, indexY: {self.indexY}"
    