class MarsRover:
    DIRECTIONS = ['e', 's']
    MOVEMENT_INSTRUCTIONS = {
        'f': 'move_forward',
        'r': 'turn_right'
    
    }
    
    def __init__(self, starting_pos: list[int], starting_dir: str, grid_size: list[int]) -> None:
        self.starting_pos = starting_pos
        self.starting_dir = starting_dir
        self.grid_size = grid_size
        self.current_position = starting_pos
        self.current_direction = starting_dir
    
    def move(self, instructions: str) -> None:
        for instruction in instructions:
            if instruction in self.MOVEMENT_INSTRUCTIONS:
                method_name = self.MOVEMENT_INSTRUCTIONS[instruction]
                getattr(self, method_name)()
    
    def move_forward(self):
        if self.current_direction == 'e':
            self.current_position[0] += 1
        elif self.current_direction == 's':
            self.current_position[1] += 1
    
    def turn_right(self):
        next_direction_index = self.DIRECTIONS.index(self.current_direction) + 1
        self.current_direction = self.DIRECTIONS[next_direction_index]
