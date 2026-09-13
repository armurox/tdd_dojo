from solution import open_doors
import pytest
from hypothesis import given
from hypothesis import strategies as st
import math

# 0 -> ""
@pytest.mark.parametrize("num_doors, expected", [
    (0, ""),
    (1, "@"),
    (2, "@#"),
    (3, "@##"),
    (10, "@##@####@#"),
])
def test_important_doors(num_doors, expected):
    assert open_doors(num_doors) == expected, f"{num_doors} doors should give {expected}"
    
@given(st.integers(min_value=0, max_value=100))
def test_property_door_length_equality(num_doors):
    result = open_doors(num_doors)
    assert len(result) == num_doors

@given(st.integers(min_value=0, max_value=100))
def test_property_perfect_squares_are_open(num_doors):
    result = open_doors(num_doors)
    for i in range(num_doors):
        index = i + 1
        sqrt = math.isqrt(index)
        if sqrt * sqrt == index:
            assert result[i] == "@", f"perfect square door must be open!"
        else:
            assert result[i] == "#", f"non-perfect sqaure doors must be closed"
