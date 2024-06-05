import random

def random_graph(n, option='default'):
    graf = {}

    for i in range(n):
        randomX = random.randint(0, n+10)
        randomY = random.randint(0, n+10)
        graf[(randomX, randomY)] = []
    
    for key in graf:
        if option == 'default':
            for key2 in graf:
                if key != key2:
                    if key2 not in graf[key] and key not in graf[key2]:
                        graf[key].append(key2)
                        graf[key2].append(key)
        elif option == '50/50':
            for key2 in graf:
                if key != key2:
                    if len(graf[key]) < n/2:
                        if key2 not in graf[key] and key not in graf[key2]:
                            graf[key].append(key2)
                            graf[key2].append(key)
    
    return graf


