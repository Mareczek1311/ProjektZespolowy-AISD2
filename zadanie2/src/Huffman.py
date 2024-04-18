import heapq as HuffmanTree

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

    HuffmanTree.heapify(priority_queue)
        