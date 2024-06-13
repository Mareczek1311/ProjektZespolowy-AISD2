from huffman import Huffman 
from rabinkarp import Rabin_Karp
from file_reader import File_reader

class Main:
    def __init__(self, filename):
        self.fr = File_reader(filename)
        self.indexes = {}

    def run(self):
        self.fr.readText()
        self.rk = Rabin_Karp(self.fr.text)
        incorrectWords = list(self.fr.wordsToReplace.keys())

        for word in incorrectWords:
            self.indexes = self.rk.find_pattern(word)

            for indexes in self.indexes.values():
                for i in indexes:
                    self.repair(i, self.fr.wordsToReplace[word])

            self.indexes.clear()

        print("\nNaprawiony tekst: \n")
        print(self.fr.text)

        self.hm = Huffman(self.fr.text)
        
        encoded_text = self.hm.huffman()

        print("Skompresowany tekst: \n")
        print(encoded_text)

        print("Rozkompresowany tekst: \n")
        print(self.hm.dehuffman(encoded_text))

    def repair(self, idx, word):
        m = len(word)
        text_list = list(self.fr.text)

        for i in range(0, m):
            text_list[idx] = word[i]
            idx += 1
                    
        self.fr.text = ''.join(text_list)


#przyklad uzycia

m = Main('examples/example1.txt')
m.run()


