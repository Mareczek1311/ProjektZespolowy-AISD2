from huffman import Huffman 
from rabin_karp import Rabin_Karp
from file_reader import File_reader

class Main:
    def __init__(self, filename):
        self.fr = File_reader(filename)

    def run(self):
        self.fr.readText()
        self.rk = Rabin_Karp(self.fr.text)
        incorrectWords = list(self.fr.wordsToReplace.keys())

        for word in incorrectWords:
            self.rk.find_pattern(word)

            for indexes in self.rk.indexes.values():
                for i in indexes:
                    self.repair(i, self.fr.wordsToReplace[word])

            self.rk.indexes.clear()

        print("\nNaprawiony tekst: \n")
        print(self.fr.text)

        self.hm = Huffman(self.fr.text)
        self.hm.huffman()

        print("Skompresowany tekst: \n")
        print(self.hm.encoded_text)

    def repair(self, idx, word):
        m = len(word)
        text_list = list(self.fr.text)

        for i in range(0, m):
            text_list[idx] = word[i]
            idx += 1
                    
        self.fr.text = ''.join(text_list)


#przyklad uzycia

m = Main('tests/test3.txt')
m.run()

