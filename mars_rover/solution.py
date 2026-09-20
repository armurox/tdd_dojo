class MarsRover:
    DIRECTIONS = ['n', 'e', 's', 'w']
    MOVEMENT_INSTRUCTIONS = {
        'f': 'move_forward',
        'r': 'turn_right',
        'l': 'turn_left',
        'b': 'move_backwards',
    }
    
    DIRECTION_TO_VECTOR = {
        'n': (0, -1),
        'e': (1, 0),
        's': (0, 1),
        'w': (-1, 0),
    }
    
    def __init__(self, starting_pos: list[int], starting_dir: str, grid_size: list[int]) -> None:
        self.starting_pos = starting_pos
        self.starting_dir = starting_dir
        self.grid_size = grid_size
        self.current_position = [0, 0]
        self.current_position[0] = starting_pos[0] % grid_size[0]
        self.current_position[1] = starting_pos[1] % grid_size[1]
        self.current_direction = starting_dir.lower()
        if self.current_direction not in self.DIRECTIONS:
            raise AssertionError(f'Starting direction must be one of {self.DIRECTIONS}')
    
    def move(self, instructions: str) -> None:
        for instruction in instructions:
            instruction = instruction.lower()
            if instruction in self.MOVEMENT_INSTRUCTIONS:
                method_name = self.MOVEMENT_INSTRUCTIONS[instruction]
                getattr(self, method_name)()
    
    def move_forward(self):
        self._move(1)
    
    def move_backwards(self):
        self._move(-1)

    def turn_right(self):
        next_direction_index = (self.DIRECTIONS.index(self.current_direction) + 1) % len(self.DIRECTIONS)
        self.current_direction = self.DIRECTIONS[next_direction_index]

    def turn_left(self):
        next_direction_index = (self.DIRECTIONS.index(self.current_direction) - 1) % len(self.DIRECTIONS)
        self.current_direction = self.DIRECTIONS[next_direction_index]

    def _move(self, multiplier: int) -> None:
        dx, dy = self.DIRECTION_TO_VECTOR[self.current_direction]
        self.current_position[0] = (self.current_position[0] + (multiplier * dx)) % self.grid_size[0]
        self.current_position[1] = (self.current_position[1] + (multiplier * dy)) % self.grid_size[1]