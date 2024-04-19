def Rabin_karp(pattern, text):
    n = len(text)
    m = len(pattern)
    bns = 256   # bns == base of number system
    pm = 101    # pm == prime number

    hash_pattern = 0
    hash_text = 0

    h = pow(bns, m - 1) % pm

    for i in range(m):
        hash_pattern = (bns * hash_pattern + ord(pattern[i])) % pm
        hash_text = (bns * hash_text + ord(text[i])) % pm

    for i in range(n - m + 1):
        if hash_text == hash_pattern:
            idx = 0
            for j in range(m):
                if text[i + j] == pattern[j]:
                    idx += 1
                else:
                    break
            if idx == m:
                print("B)")
                
        if i < n - m:
            hash_text = (bns * (hash_text - ord(text[i]) * h) + 
                         ord(text[i + m])) % pm
            
            if hash_text < 0:
                hash_text += hash_text + pm

text = "dolo to ziomal"
patt = "o"

Rabin_karp(patt, text)
