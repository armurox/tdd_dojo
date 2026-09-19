# Part 1: Valid inputs
- [x] MarsRover([0, 0], 'e', [2, 2]) + '' -> final_position: 0, 0 + final direction: 'e'
- [x] ([0, 0], 'e', [50, 50]) + 'ff' -> fp: [2, 0] + fd: 'e'
- [x] ([0, 0], 'e', [50, 50]) + 'ffrff' -> fp: [2,2] + fd: 's'
- [x] ([0, 0], 'e', [50, 50]) + 'ffrrff' -> fp: [0,0] + fd: 'w'
- [x] ([0, 0], 'e', [50, 50]) + 'ffrrffrfflffr' -> fp: [48,48] + fd: 'n'
- [x] ([0, 0], 'e', [50, 50]) + 'ffrrffrfflfbr' -> fp: [48,489] + fd: 'n'


# Part 2: Handling weirder inputs
- [x] ([0, 0], 'e', [50, 50]) + 'FfrrffrfflfFr' -> fp: [48,48] + fd: 'n'



# Part 3: Properties