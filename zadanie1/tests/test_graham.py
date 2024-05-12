import pytest
import sys
sys.path.append('../src')
from graham import Graham

class TestGraham:
    @pytest.mark.parametrize("points, expected", [
        ([(1, 1), (2, 3), (4, 5)], -2),
        ([(4, 5), (2, 3), (1, 1)], 2),
        ([(1, 2), (3, 6), (5, 10)], 0),
        ([(0, 0), (0, 0), (0, 0)], 0),
        ([(-1, -2), (-3, -4), (-5, -6)], 0),
        ([(2, 1), (4, 2), (6, 3)], 0),
        ([(2, 1), (4, 2), (6, 3)], 0)])
    def test_det(self, points, expected):
        g = Graham()
        assert g.det(points[0], points[1], points[2]) == expected
    

    @pytest.mark.parametrize("points, expected", [
        ([[0,3], [3,1], [2,2]], [3,1]), #klasyczny przypadek, punkt 3,1 ma najmniejsza wartosc y 
        ([[0,3], [1,2], [1,1], [2,1]], [2,1]), #przypadek gdy punkty maja taka sama wartosc y
        ([[0,3], [3,1], [1,2], [1,1], [2,1]], [3,1]),#przypadek gdy punkt 3,1 ma najwieksza wartosc x
        ([(2, 2)], (2, 2))])  #przypadek gdy jest tylko jeden punkt
    def test_find_min(self, points, expected):   
        g = Graham()
        assert g.findMin(points) == expected

    @pytest.mark.parametrize("p1, p2, expected", [
        ((1, 2), (1, 2), 0),       # te same punkty
        ((0, 0), (3, 4), 25),      # przypadek 1
        ((-1, -1), (-4, -5), 25),  # przypadek 1 tylko ze ujemne liczby
        ((1, 1), (-1, -1), 8),     # punkty na przekatnej
    ])
    def test_distSq(self, p1, p2, expected):
        g = Graham()
        assert g.distSq(p1, p2) == expected
    
    @pytest.mark.parametrize("p1, p2, mini, expected", [
        ((2, 3), (4, 5), (1,1), 1),       # przyklad 1
        ((2, 3), (1, 2), (1,1), -1),       # przyklad 2
        ((3, 6), (5, 10), (1,2), -1) ,    # Points in different quadrants
        ((5, 10), (3, 6), (1,2), 1)     # Points in different quadrants
    ])
    def test_compare(self, p1, p2, mini, expected):
        g = Graham()
        g.min = mini
        assert g.compare(p1, p2) == expected

    @pytest.mark.parametrize("punkty, expected_hull", [
        ([(0, 0), (1, 1), (2, 0), (1, -1)], [(1,-1),(2, 0), (1, 1), (0,0)]),
        ([(0, 0), (1, 0), (2, 0)], [(2, 0), (1, 0), (0, 0)]),
        ([(0, 0), (2, 2), (3, 1), (1, 3), (-1, 2)], [(0, 0), (3, 1), (2, 2), (1, 3), (-1, 2)]),
        ([(1, 1)], []),
        ([], [])
    ])
    def test_algorytm(self, punkty, expected_hull):
        g = Graham(punkty)
        g.algorytm()
        g.draw()
        assert g.convexHull == expected_hull
