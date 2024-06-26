class Rabin_Karp:
    def __init__(self, text):
        """!
        Konstruktor dla klasy Rabin_Karp
        @Param text - tekst w którym będziemy szukali wzorców
        """
        self.text = text

    def find_pattern(self, pattern):
        """!
        find_pattern Metoda która wyszukuje wzorzec w  tekście podanym jako argument
        konstruktora
        @param pattern - wzorzec który chcemy wyszukać
        @return słownik {"wzorzec":[i1, i2, ..., in]}, gdzie in są to indeksy wystąpień
         wzorca w tekście dla n należącego do liczb naturalnych
        """
        indexes = {}
        n = len(self.text)
        m = len(pattern)
        if m == 0:
            return indexes
        
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
                    if pattern not in indexes:
                        indexes[pattern] = []
                    indexes[pattern].append(i)
                    
            if i < n - m:
                hash_text = (bns * (hash_text - ord(self.text[i]) * h) + 
                            ord(self.text[i + m])) % pm
                
                if hash_text < 0:
                    hash_text += hash_text + pm

        return indexes

#przyklad uzycia

# text = "tekst"
# RK = Rabin_Karp(text)

# pattern = "t"

# RK.find_pattern(pattern)

# print(RK.indexes)
