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
    def __init__(self, text):
        self.text = text
        self.codesArr = {}
        self.encoded_text = ""
        self.root = Node

        
    def build_huffman_tree(self, text):
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


        if tree is not None:
            if tree.character is not None:
                codes[tree.character] = prefix
            self.huffman_coding(tree.left, prefix + "0", codes)
            self.huffman_coding(tree.right, prefix + "1", codes)

        return codes

    def huffman(self):
        self.root = self.build_huffman_tree(self.text)
        self.codesArr = self.huffman_coding(self.root)
        encoded_text = ""
        for c in self.text:
            encoded_text += self.codesArr[c]
        
        self.encoded_text = encoded_text

    def dehuffman(self):
        original_text = ""
        current_code = ""
        rev_codes = {}

        for c, code in self.codesArr.items():
            rev_codes[code] = c

        for bit in self.encoded_text:
            current_code += bit
            
            if current_code in rev_codes:
                original_text += rev_codes[current_code]
                current_code = ""

        return original_text

### przykład użycia 
text = "DOLO_TO_FAJNY_KOLEGA"
h = Huffman(text)
h.huffman()
print(h.encoded_text) ##zwraca skompresowany tekst

### możemy tak też sprawdzić czy zamiana skompresowanego tekstu 
### z powrotem na originalny wyraz będzie prawidłowa
### tzn. text == original text
 
original_text= h.dehuffman()
print(original_text)

    
