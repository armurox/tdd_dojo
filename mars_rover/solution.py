class MarsRover:
    DIRECTION_NUM_TO_LETTER = {
        0: 'e',
        1: 's',
    }
    
    DIRECTION_LETTER_TO_NUM = {
            letter: num 
            for num, letter in DIRECTION_NUM_TO_LETTER.items()
    }
    
    MOVEMENT_NUM_TO_LETTER = {
        1: 'f',
    }
    
    MOVEMENT_LETTER_TO_NUM = {
        letter: num
        for num, letter in MOVEMENT_NUM_TO_LETTER.items()
    }
    
    ROTATION_DIRECTION_NUM_TO_LETTER = {
        1: 'r',
    }
    
    ROTATION_DIRECTION_LETTER_TO_NUM = {
                letter: num 
                for num, letter in ROTATION_DIRECTION_NUM_TO_LETTER.items()
        }
    
    def __init__(self, starting_pos: list[int], starting_dir: str, grid_size: list[int]) -> None:
        self.starting_pos = starting_pos
        self.starting_dir = starting_dir
        self.grid_size = grid_size
        self.current_position = starting_pos
        self.current_direction = starting_dir
    
    def move(self, instructions: str) -> None:
        for instruction in instructions:
            if instruction in self.MOVEMENT_LETTER_TO_NUM:
                self.current_position[self.DIRECTION_LETTER_TO_NUM.get(self.current_direction)] += self.MOVEMENT_LETTER_TO_NUM.get(instruction)
            elif instruction in self.ROTATION_DIRECTION_LETTER_TO_NUM:
                self.current_direction = self.DIRECTION_NUM_TO_LETTER.get(self.DIRECTION_LETTER_TO_NUM.get(self.current_direction) + 1)