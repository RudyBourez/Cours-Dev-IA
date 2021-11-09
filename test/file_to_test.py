import pytest
from fonction import my_sort

def test_my_sort():
    assert my_sort([1, 5, 9, 10, 2, 3, 7]) == [1, 2, 3, 5, 7, 9, 10]
    assert my_sort(["z", "c", "f", "b", "d"]) == ["b", "c", "d", "f", "z"]
    assert my_sort([1.0, 3.0, 22.5, 33.6, 12.9, 10.2 ]) == [1.0, 3.0, 10.2, 12.9, 22.5, 33.6]
    assert my_sort([True, False, False, True, True]) == [False, False, True, True, True]
    with pytest.raises(TypeError):
        my_sort([True, False, False, True, 0])
        my_sort([1, 5.0, 9.6, 10, 2, 3, 7])
    