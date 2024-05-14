import random 

def randomPoints(num):
    points = set()

    for i in range(num):
        x = random.randint(-100000, 100000)
        y = random.randint(-100000, 100000)
        points.add((x, y))
    
    points = list(points)
    return points