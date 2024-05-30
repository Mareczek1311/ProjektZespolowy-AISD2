import random

def random_tragarze(ilosc, option='default'):
    if ilosc % 2 != 0:
        ilosc += 1
    
    tragarze = {}

    tragarze[(0,0)] = []
    tragarze[(6,0)] = []

    for i in range(0, ilosc//2):
        tragarze[(5, i)] = []
        tragarze[(5, i)].append(((6,0), 1))

    
    for i in range(0, ilosc//2):
        tragarze[(1, i)] = []
        tragarze[(0,0)].append(((1, i), 1))

        if option == 'default':
            for j in range(0, ilosc//2):
                tragarze[(1, i)].append(((5, j), 1))
        elif option == '50/50':
            for j in range(0, ilosc//4):
                tragarze[(1, i)].append(((5, random.randint(0, ilosc//2)), 1))

    punkty = []
    for key in tragarze:
        punkty.append(key)
    
    full_res = {"adjList": tragarze, "start": (0,0), "end": (6,0), "punkty": punkty}

    return full_res
