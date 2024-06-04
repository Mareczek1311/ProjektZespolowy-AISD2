def get_graph(adjList):
    res = {}

    for key in adjList:
        for val in adjList[key]:
            if key not in res and key != (10, 0):
                res[key] = []
            if val[0] != (10, 0):
                res[key].append(val[0])
                if val[0] not in res:
                    res[val[0]] = []
                res[val[0]].append(key)    
    return res
