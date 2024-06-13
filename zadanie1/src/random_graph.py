import random

def random_graph(n, option='default'):
    graf = {}

    for i in range(n):
        while True:
            randomX = random.randint(0, n+10)
            randomY = random.randint(0, n+10)
            if (randomX, randomY) not in graf:
                graf[(randomX, randomY)] = []
                break
    
    keys = list(graf.keys())
    
    if option == 'default':
        for i in range(n):
            for j in range(i + 1, n):
                graf[keys[i]].append(keys[j])
                graf[keys[j]].append(keys[i])
    elif option == '50/50':
        for i in range(n):
            for j in range(i + 1, n):
                if random.randint(0, 1):
                    graf[keys[i]].append(keys[j])
                    graf[keys[j]].append(keys[i])
    elif option == 'half_connections':
        for i in range(n):
            while len(graf[keys[i]]) < n // 2:
                j = random.randint(0, n - 1)
                if i != j and keys[j] not in graf[keys[i]]:
                    graf[keys[i]].append(keys[j])
                    graf[keys[j]].append(keys[i])
    
    return graf
