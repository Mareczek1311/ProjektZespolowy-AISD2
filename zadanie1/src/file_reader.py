# Dane w plikach /data
# w pierwszej linii ilosc wierzcholkow (n), ilosc polaczen (m) oraz x i y punktu startowego (fabryki)
# w kolejnych n liniach wierzcholki
# w kolejnych liniach dwa wierzcholki (x, y) tworzace krawedz oraz jej przepustowosc

# Przyklad
"""
11 3 3 4
1 2
3 4
4 3 
5 4
4 5
2 6
1 4
2 4
3 3
5 5
6 6
3 4 2 4 1
3 4 3 3 1
2 4 1 4 1
"""
#wszystkie punkty powinny byc klasa oddzielna poniewaz gdy zmienie x i y to zmieni sie wszedzie

from tragarz import Tragarz

class File_reader:
    
    def readTragarzy(self, filename):
        if not filename:
            return {}
        
        tragarze = []
        index_z_przodu = 0
        index_z_tylu = 0
        with open(filename, 'r') as file_in:
            for line in file_in:
                line = line.rstrip()
                rece, klub = line.split()
                if rece == 'przod':
                    t = Tragarz(1, index_z_przodu, klub)
                    tragarze.append(t)
                    index_z_przodu += 1
                else:
                    tragarze.append(Tragarz(5, index_z_tylu, klub))
                    index_z_tylu += 1

        for tragarz in tragarze:
            if tragarz.punkt[0] == 1:
                for tragarz2 in tragarze:
                    if tragarz != tragarz2 and tragarz.klub == tragarz2.klub and tragarz2.punkt[0] == 5:
                        tragarz.dodaj_relacje((tragarz2.punkt, 1))

        res = {(0,0):[], (6,0):[]}

        for tragarz in tragarze:
            if tragarz.punkt[0] == 1:
                res[(0,0)].append((tragarz.punkt, 1))
            res[tragarz.punkt] = tragarz.lista_sasiedztwa

            if tragarz.punkt[0] == 5:
                res[tragarz.punkt].append(((6,0),1))

        punkty = []
        for key in res:
            punkty.append(key)

        full_res = {"adjList": res, "start": (0,0), "end": (6,0), "punkty": punkty}

        return full_res
        
    def readPoints(self, filename):
        if not filename:
            return {}
        
        data = {"adjList": {}, "start": None}
        currLine = 0
        startX = 0
        startY = 0
        endX = 0
        endY = 0

        with open(filename, 'r') as file_in:
            for line in file_in:
                line = line.rstrip()

                if currLine == 0:
                    n, m, startX, startY, endX, endY = line.split()
                    numOfVertices = int(n)
                    numOfEdges = int(m)
                    currLine += 1
                    continue

                if currLine <= numOfVertices:
                    x, y = line.split()
                    data["adjList"][(int(x), int(y))] = []
                    currLine += 1
                    continue
                
                x, y, w, z, flow = line.split() 
                
                pointA = (int(x), int(y))
                pointB = (int(w), int(z))

                if pointA not in data["adjList"]:
                    data["adjList"][pointA] = []
                if pointB not in data["adjList"]:
                    data["adjList"][pointB] = []
                
                data["adjList"][pointA].append((pointB, int(flow)))

        data["start"] = (int(startX), int(startY))
        data["end"] = (int(endX), int(endY))

        return data


def main():
    fr = File_reader('../data/przyklad3.txt')
    data = fr.read()
    print(data)

def testKluby():
    fr = File_reader()
    kluby = fr.readKluby('../data/kluby.txt')
    fr.readKlubyRelacje('../data/kluby_relacje.txt', kluby)

    for key, value in kluby.items():
        print(value.nazwaKlubu)
        print("Dobre relacje:")
        for rel in value.dobreRelacje:
            print(kluby[rel].nazwaKlubu, end=' ')
        print()
        print("=========")
if __name__ == '__main__':
    #main()

    testKluby()