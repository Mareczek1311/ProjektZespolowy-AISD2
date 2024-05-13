import pytest
import sys
sys.path.append('../src')
from fordfulkerson import Edge, FordFulkerson

class Test_FordFulkerson_and_Edge:
    @pytest.mark.parametrize("fr, to, capacity, expected",
    [
        (1, 2, 3, False),
        (2, 1, 0, True),
        (3, 4, 0, True),
        (4, 3, 3, False),
        (5, 6, 0, True),
        (6, 5, 0, True)
    ])
    def test_isResidual(self, fr, to, capacity, expected):
        edge = Edge(fr, to, capacity)
        assert edge.isResidual() == expected

    @pytest.mark.parametrize("fr, to, capacity, flow, expected", 
    [
        (1, 2, 3, 1, 2),
        (2, 1, 1, 1, 0),
        (3, 4, 0, 0, 0),
        (4, 3, 3, 2, 1),
    ])
    def test_remainingCapacity(self, fr, to, capacity, flow, expected):
        edge = Edge(fr, to, capacity, flow)
        assert edge.remainingCapacity() == expected

    
    @pytest.mark.parametrize("fr, to, capacity, flow, newFlow, expected",
    [
        (1, 2, 3, 1, 1, 2),
        (2, 1, 1, 1, 2, 3),
        (3, 4, 0, 0, 0, 0),
        (4, 3, 3, 2, 1, 3),
    ])
    def test_augment(self, fr, to, capacity, flow, newFlow, expected):
        edge = Edge(fr, to, capacity, flow)
        edge.reverse = Edge(to, fr, 0)
        edge.augment(newFlow)
        assert edge.flow == expected
