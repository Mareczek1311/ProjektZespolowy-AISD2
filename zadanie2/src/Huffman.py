import heapq as heap

class Node:
    def __init__(self, character = None, frequency = None):
        self.character = character
        self.frequency = frequency
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.frequency < other.frequency

def build_huffman_tree(word):
    frequency = {}
    for c in word:                     # c == character
        if c in frequency:
            frequency[c] += 1
        elif c not in frequency:
            frequency[c] = 1
    #print(frequency)
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

def huffman_coding(tree, prefix = "", codes = {}):

    if tree is not None:
        if tree.character is not None:
            codes[tree.character] = prefix
        huffman_coding(tree.left, prefix + "0", codes)
        huffman_coding(tree.right, prefix + "1", codes)

    return codes

def huffman(word):
    root = build_huffman_tree(word)
    codes = huffman_coding(root)
    encoded_word = ""
    for c in word:
        encoded_word += codes[c]
    
    return encoded_word, codes

def dehuffman(encoded_word, codes):
    original_word = ""
    current_code = ""
    rev_codes = {}

    for c, code in codes.items():
        rev_codes[code] = c

    for bit in encoded_word:
        current_code += bit
        
        if current_code in rev_codes:
            original_word += rev_codes[current_code]
            current_code = ""

    return original_word

word = "DOLO_TO_FAJNY_KOLEGA"
encoded_word, codes = huffman(word)
print(encoded_word)
original_word = dehuffman(encoded_word, codes)
print(original_word)
    
