import pytest
from hypothesis import given
from hypothesis import strategies as st
from solution import Solver

@pytest.mark.parametrize(
    "input, expected",[
        ("[", False),
        ("[]", True),
        ("[[]", False),
        ("[][]", True),
        ("][][", False),
    ]
)
def test_brackets(input: str, expected: bool) -> None:
    solver = Solver()
    output = solver.solve(input)
    assert output == expected

