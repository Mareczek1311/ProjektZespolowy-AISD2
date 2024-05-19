from graham import Graham
from random_points import randomPoints

def testowanie():
    punkty = randomPoints(1000)
    g = Graham(punkty)
    print(g.getOtoczka())
    g.draw(punkty, g.getOtoczka())


if __name__ == "__main__":
    testowanie()