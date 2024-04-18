def Levenshtein(string1, string2):
    len1 = len(string1)
    len2 = len(string2)

    arr =  []

    for _ in range(len1 + 1):
        row = []
        for _ in range(len2 + 1):
            row.append(0)
        arr.append(row)

    for i in range(len1 + 1):
        arr[i][0] = i
    for j in range(len2 + 1):
        arr[0][j] = j
    
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if string1[i - 1] == string2[j - 1]:
                arr[i][j] = arr[i - 1][j - 1]
            else:
                arr[i][j] = 1 + min(arr[i][j - 1], arr[i - 1][j], arr[i - 1][j - 1])

    return arr[len1][len2]
