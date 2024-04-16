class File_reader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        if not self.filename:
            return []
        arr = []
        with open(self.filename, 'r') as file_in:
            for line in file_in:
                line = line.rstrip()
                x, y = line.split() 
                arr.append((int(x), int(y)))
        return arr

