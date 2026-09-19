import pytest
from solution import MarsRover

@pytest.mark.parametrize(
    "starting_pos, starting_dir, grid_size, instructions, expected_final_pos, expected_final_dir",
    [
        ([0, 0], 'e', [2, 2], '', [0, 0], 'e'),
        ([0, 0], 'e', [50, 50], 'ff', [2, 0], 'e'),
        ([0, 0], 'e', [50, 50], 'ffrff', [2, 2], 's'),
        ([0, 0], 'e', [50, 50], 'ffrrff', [0, 0], 'w'),
        ([0, 0], 'e', [50, 50], 'ffrrffrfflffr', [48, 48], 'n'),
        ([0, 0], 'e', [50, 50], 'b', [49, 0], 'e'),
        ([0, 0], 'e', [50, 50], 'FfRrfFrfflfFr', [48, 48], 'n'),        
    ]
)
def test_move_mars_rover(starting_pos, starting_dir, grid_size, instructions, expected_final_pos, expected_final_dir):
    rover = MarsRover(starting_pos, starting_dir, grid_size)
    rover.move(instructions)
    assert rover.current_position == expected_final_pos
    assert rover.current_direction == expected_final_dir