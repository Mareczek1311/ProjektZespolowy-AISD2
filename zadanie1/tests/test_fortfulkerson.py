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

    def test_ford_fulkerson_one(self):
        punkty = [
        (0, 0),
        (1, 1),
        (1, 0),
        (1, -1),
        (2, 1),
        (2, 0),
        (2, -1),
        (3, 1),
        (3, 0),
        (3, -1),
        (4, 0)
        ]

        adjList = {(0, 0): [((1,1), 7), ((1,0), 2), ((1,-1), 1)], 
                (1,1):[((2,1), 2), ((2,0), 4)],  (1,0):[((2,0),5), ((2,-1),6)], (1,-1):[((2,1),4), ((3,0),8)],
                (2,1):[((3,1),7), ((3,0), 1)], (2,0):[((3,1),3), ((2,-1),8), ((3,-1),3)], (2,-1):[((3,-1),3)],
                (3,1):[((4,0),1)], (3,0):[((4,0),3)], (3,-1):[((4,0),4)],
                (4,0):[]}

        start = (0, 0)
        end = (4, 0)

        n = len(punkty)

        solver = FordFulkerson(n, start, end, punkty)
        solver.config(start, end, adjList)

        assert solver.getMaxFlow() == 7



