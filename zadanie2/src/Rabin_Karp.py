class Rabin_Karp:
    def __init__(self, text):
        self.text = text
        self.indexes = {}

    def find_pattern(self, pattern):
        n = len(self.text)
        m = len(pattern)
        bns = 256   # bns == base of number system
        pm = 101    # pm == prime number

        hash_pattern = 0
        hash_text = 0

        h = pow(bns, m - 1) % pm

        for i in range(m):
            hash_pattern = (bns * hash_pattern + ord(pattern[i])) % pm
            hash_text = (bns * hash_text + ord(self.text[i])) % pm

        for i in range(n - m + 1):
            if hash_text == hash_pattern:
                idx = 0
                for j in range(m):
                    if self.text[i + j] == pattern[j]:
                        idx += 1
                    else:
                        break
                if idx == m:
                    if pattern not in self.indexes:
                        self.indexes[pattern] = []
                    self.indexes[pattern].append(i)
                    
            if i < n - m:
                hash_text = (bns * (hash_text - ord(self.text[i]) * h) + 
                            ord(self.text[i + m])) % pm
                
                if hash_text < 0:
                    hash_text += hash_text + pm

#przyklad uzycia

text = "dolo to fajny kolega"

RK = Rabin_Karp(text)

pattern = "fajny"

RK.find_pattern(pattern)

print(RK.indexes)
