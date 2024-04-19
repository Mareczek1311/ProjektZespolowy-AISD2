import heapq as heap

class Node:
    def __init__(self, character = None, frequency = None):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.frequency < other.frequency
    

class Huffman:
    def __init__(self, word):
        self.word = word
        self.codesArr = {}
        self.encoded_word = ""
        self.root = Node

        
    def build_huffman_tree(self, word):
        frequency = {}
        for c in word:                     # c == character
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


        if tree is not None:
            if tree.character is not None:
                codes[tree.character] = prefix
            self.huffman_coding(tree.left, prefix + "0", codes)
            self.huffman_coding(tree.right, prefix + "1", codes)

        return codes

    def huffman(self):
        self.root = self.build_huffman_tree(self.word)
        self.codesArr = self.huffman_coding(self.root)
        encoded_word = ""
        for c in word:
            encoded_word += self.codesArr[c]
        
        self.encoded_word = encoded_word

    def dehuffman(self):
        original_word = ""
        current_code = ""
        rev_codes = {}

        for c, code in self.codesArr.items():
            rev_codes[code] = c

        for bit in self.encoded_word:
            current_code += bit
            
            if current_code in rev_codes:
                original_word += rev_codes[current_code]
                current_code = ""

        return original_word

### przykład użycia 
word = "DOLO_TO_FAJNY_KOLEGA"
h = Huffman(word)
h.huffman()
print(h.encoded_word) ##zwraca skompresowany wyraz 

### możemy tak też sprawdzić czy zamiana skompresowanego wyrazu 
### z powrotem na originalny wyraz będzie prawidłowa
### tzn. word == original word
 
original_word = h.dehuffman()
print(original_word)

    
