import pytest
from huffman import Huffman

class TestHuffman:

    @pytest.mark.parametrize("texts, expected",[
        ("Kacper","0110100001011001"),
        ("Jakub","000110011001"),
        ("Mareczek","1000001100100110101111"),
        ("Krol lew","1000001100100101101111"),
        ("Dolo","001011")
    ])

    def test_huffman(self, texts, expected):
        h = Huffman(texts)
        
        assert h.huffman() == expected
        h.codesArr.clear()


    @pytest.mark.parametrize("texts, expected",[
        ("kajak", "kajak"),
        ("mama", "mama"),
        ("oko", "oko"),
        ("ciara", "ciara"),
        ("bardzo lubie uczyc sie na umk", "bardzo lubie uczyc sie na umk"),
        ("koszykowka", "koszykowka")
    ])

    def test_dehuffman(self, texts, expected):
        h = Huffman(texts)
        assert h.dehuffman(h.huffman()) == expected
