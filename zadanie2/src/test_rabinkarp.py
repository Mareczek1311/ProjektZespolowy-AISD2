import pytest
from rabinkarp import Rabin_Karp

class TestRabin:

    @pytest.mark.parametrize("texts, patterns, expected",[
        ("dolo marek kacper", "marek", {'marek': [5]}),
        ("algorytmy i struktury danych", "i", {'i': [10]}),
        ("algorytm algorytm", "algorytm", {"algorytm": [0, 9]}),
        ("chcialbym zdac sesje bez poprawek", "zdac", {"zdac": [10]}),
        ("hej hej hej sokooooly", "hej", {"hej": [0, 4, 8]}),
        ("kocham sie uczyc", " ", {" ": [6, 10]}),
        ("test", "", {})
    ])

    def test_find_pattern(self, texts, patterns, expected):
        r = Rabin_Karp(texts)

        assert r.find_pattern(patterns) == expected