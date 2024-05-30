import random 

def randomPoints(num):
    points = set()

    for i in range(num):
        x = random.randint(-num - 100, num + 100)
        y = random.randint(-num - 100, num + 100)
        points.add((x, y))
    
    points = list(points)
    return points