import pytest
from solution import MarsRover
from hypothesis import given 
from hypothesis import strategies as st

@pytest.mark.parametrize(
    "starting_pos, starting_dir, grid_size, instructions, expected_final_pos, expected_final_dir",
    [
        ([0, 0], 'e', [2, 2], '', [0, 0], 'e'),
        ([0, 0], 'e', [50, 50], 'ff', [2, 0], 'e'),
        ([0, 0], 'e', [50, 50], 'ffrff', [2, 2], 's'),
        ([0, 0], 'e', [50, 50], 'ffrrff', [0, 0], 'w'),
        ([0, 0], 'e', [50, 50], 'ffrrffrfflffr', [48, 48], 'n'),
        ([0, 0], 'e', [50, 50], 'FfRrfFrfflfFr', [48, 48], 'n'),   
        ([0, 0], 'n', [1, 1], '', [0, 0], 'n'), 
        ([0, 0], 'n', [1, 1], 'R', [0, 0], 'e'),        
    ]
)
def test_move_mars_rover(starting_pos, starting_dir, grid_size, instructions, expected_final_pos, expected_final_dir):
    rover = MarsRover(starting_pos, starting_dir, grid_size)
    rover.move(instructions)
    assert rover.current_position == expected_final_pos
    assert rover.current_direction == expected_final_dir

directions = st.sampled_from(['n', 'e', 's', 'w'])
invalid_directions = st.text(min_size=1).filter(lambda d: d not in ['n', 'e', 's', 'w'])
instructions = st.text()

@given(
    x=st.integers(),
    y=st.integers(),
    direction=directions,
)
def test_forward_then_backward_returns_to_same_position(x, y, direction):
    rover = MarsRover([x, y], direction, [50, 50])

    rover.move("fb")

    assert rover.current_position == [x % 50, y % 50]
    assert rover.current_direction == direction.lower()

@given(
    x=st.integers(),
    y=st.integers(),
    direction=directions,
)
def test_forward_then_backward_returns_to_same_position(x, y, direction):
    rover = MarsRover([x, y], direction, [50, 50])

    rover.move("rl")

    assert rover.current_position == [x % 50, y % 50]
    assert rover.current_direction == direction.lower()

@given(
    x=st.integers(),
    y=st.integers(),
    direction=directions,
    instructions=instructions,
    grid_x=st.integers(min_value=1),
    grid_y=st.integers(min_value=1),
)
def test_final_position_always_inside_grid(x, y, direction, instructions, grid_x, grid_y):
    rover = MarsRover([x,y], direction, [grid_x, grid_y])
    rover.move(instructions)
    assert 0 <= rover.current_position[0] < grid_x
    assert 0 <= rover.current_position[1] < grid_y

@given(
    x=st.integers(),
    y=st.integers(),
    direction=invalid_directions,
    instructions=instructions,
    grid_x=st.integers(min_value=1),
    grid_y=st.integers(min_value=1),
)
def test_invalid_directions(x, y, direction, instructions, grid_x, grid_y):
    with pytest.raises(AssertionError):
        rover = MarsRover([x,y], direction, [grid_x, grid_y])