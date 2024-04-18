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

def huffman_coding(tree, prefix = "", code = dict):

    if tree is not None:
        if tree.character is not None:
            code[tree.character] = prefix
        huffman_coding(tree.left, prefix + "0", code)
        huffman_coding(tree.right, prefix + "1", code)

    return code

def huffman(word):
    root = build_huffman_tree(word)
    code = huffman_coding(root)
    encoded_word = ""
    for c in word:
        encoded_word += code[c]
    
    return encoded_word, code
    
    

