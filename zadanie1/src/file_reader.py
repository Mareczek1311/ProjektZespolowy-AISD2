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
  
class File_reader:
    
    def readTragarzy(self, filename):
        if not filename:
            return {}
        idx = 0
        idy = 0
        tragarze = {(0,0): [], (6,0): []}
        with open(filename, 'r') as file_in:
            num_of_tragarzy = int(file_in.readline())

            for line in file_in:
                line = line.rstrip()
                arr = line.split()
                idx = int(arr[0])
                idy = int(arr[1])

                tragarze[(idx, idy)] = []

                if(idx == 1):
                    tragarze[(0,0)].append(((idx, idy), 1))
                if(idx == 5):
                    tragarze[(idx, idy)].append(((6,0), 1))

                for i in range(2, len(arr), 2):
                    tragarze[(idx, idy)].append(((int(arr[i]), int(arr[i+1])), 1))

        punkty = []
        for key in tragarze:
            punkty.append(key)

        full_res = {"adjList": tragarze, "start": (0,0), "end": (6,0), "punkty": punkty}

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

if __name__ == '__main__':
    #main()

    testKluby()