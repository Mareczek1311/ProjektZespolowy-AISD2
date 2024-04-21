class File_reader:
    def __init__(self, filename):
        self.filename = filename
        self.lines = 0
        self.words = 0
        self.wordsToReplace = {}
        self.text = ""

    def readText(self):
        with open(self.filename, 'r') as file:
            data = file.readline().strip()
            n, m = data.split()
            self.lines = int(n)
            self.words = int(m) 
            
            for i in range(self.lines):
                line = file.readline()
                self.text += line

            for i in range(self.words):
                data = file.readline().strip()
                wrongWord, correctWord = data.split()
                self.wordsToReplace[wrongWord] = correctWord



#przyklad uzycia

#f = File_reader('../tests/test1.txt')
#f.readText()
