class Keyword_tree:
    def __init__(self):
        self.children = {}
        self.output = []

def build_keyword_tree(words):
    root = Keyword_tree()

    for word in words:
        node = root
        for c in word:        # c == character
            
            if c not in node.children:
                node.children[c] = Keyword_tree()
            
            node = node.children[c]
        
        node.output.append(word)

    return root