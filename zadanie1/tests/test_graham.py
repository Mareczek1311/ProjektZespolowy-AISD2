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

    