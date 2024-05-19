import heapq as heap

class Node:
    def __init__(self, character = None, frequency = 0):
        """!
        Konstruktor dla klasy Node
        """
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.frequency < other.frequency
    

class Huffman:
    def __init__(self, text):
        """!
        Konstruktor dla klasy Huffman
        @param text - tekst który chcemy skompresować 
        """
        self.text = text.rstrip("\n")
        self.codesArr = {}
        self.encoded_text = ""
        self.root = None

        
    def build_huffman_tree(self, text):
        """!
        build_huffman_tree Metoda która tworzy drzewo Huffmana
        @param text - tekst na podstawie którego tworzymy drzewo Huffmana
        @return root - korzeń do naszego drzewa Huffmana
        """
        frequency = {}
        for c in text:                     # c == character
            if c in frequency:
                frequency[c] += 1
            elif c not in frequency:
                frequency[c] = 1

        priority_queue = []

        for c, freq in frequency.items():
            priority_queue.append(Node(c, freq))

        heap.heapify(priority_queue)

        while len(priority_queue) > 1:
            right = heap.heappop(priority_queue)
            left = heap.heappop(priority_queue)

            newNode = Node(frequency = None)
            newNode.frequency = left.frequency + right.frequency
            newNode.right = right
            newNode.left = left

            heap.heappush(priority_queue, newNode)

        root = priority_queue[0]   

        return root

    def huffman_coding(self, tree, prefix = "", codes = {}):
        """!
        huffman_coding Metoda rekurencyjna która tworzy słownik w którym każdej literze
        z podanego w konstruktorze klasy tekstu jest przypisywany kod
        @param tree - Node w którym się aktualnie znajdujemy
        @return słownik codes w którym każda litera ma przypisany kod
        """

        if tree is not None:
            if tree.character is not None:
                codes[tree.character] = prefix
            self.huffman_coding(tree.left, prefix + "0", codes)
            self.huffman_coding(tree.right, prefix + "1", codes)

        return codes

    def huffman(self):
        """!
        huffman Metoda która najpierw wywołuje metodę build_huffman_tree,
        następnie za pomocą zwroconego korzenia do drzewa Huffmana wywołuje
        rekurencyjną metodę huffman_coding, która zaś zwraca nam słownik.
        Za pomocą słownika kompresujemy tekst podany w konstruktorze klasy
        @return skompresowany tekst podany jako parametr konstruktora klasy Huffman 
        """
        self.root = self.build_huffman_tree(self.text)
        self.codesArr = self.huffman_coding(self.root)
        encoded_text = ""
        
        for c in self.text:
            encoded_text += self.codesArr[c]
        
        return encoded_text

    def dehuffman(self, encoded_text):
        """!
        dehuffman Metoda która dekoduje skompresowany tekst na tekst oryginalny
        @param encoded_text - skompresowany tekst który chcemy odkodować
        @returns odkodowany tekst
        """
        original_text = ""
        current_code = ""
        rev_codes = {}

        for c, code in self.codesArr.items():
            rev_codes[code] = c

        for bit in encoded_text:
            current_code += bit
            
            if current_code in rev_codes:
                original_text += rev_codes[current_code]
                current_code = ""
        
        self.codesArr.clear()

        return original_text

### przykład użycia 
# text = "DOLO_TO_FAJNY_KOLEGA"
# h = Huffman(text)
#h.huffman()
# print(h.encoded_text) ##zwraca skompresowany tekst

### możemy tak też sprawdzić czy zamiana skompresowanego tekstu 
### z powrotem na originalny wyraz będzie prawidłowa
### tzn. text == original text
 
# original_text= h.dehuffman()
#print(original_text)

    
