import pytest
from inverted_index import InvertedIndex

def test_intersect():
    ii = InvertedIndex()
    arr1 = [2, 4, 6, 8, 100]
    arr2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 100, 200]
    res = ii.intersect(arr1, arr2)
    assert res == [2, 4, 6, 8, 100]