import pytest
import sys
sys.path.append('../src')
from graham import Graham

class TestGraham:
    def test_det_1(self):
        g = Graham()
        assert g.det((1, 1), (2, 3), (4, 5)) == -2

    def test_det_2(self):
        g = Graham()
        assert g.det((4, 5), (2, 3), (1, 1)) == 2

    def test_det_3(self):
        g = Graham()
        assert g.det((1, 2), (3, 6), (5, 10)) == 0

    def test_det_4(self):
        g = Graham()
        assert g.det((0, 0), (0, 0), (0, 0)) == 0

    def test_det_5(self):
        g = Graham()
        assert g.det((-1, -2), (-3, -4), (-5, -6)) == 0
    
    def test_det_6(self):
        g = Graham()
        assert g.det((1, 2), (2, 4), (3, 6)) == 0

    def test_det_7(self):
        g = Graham()
        assert g.det((2, 1), (4, 2), (6, 3)) == 0

    