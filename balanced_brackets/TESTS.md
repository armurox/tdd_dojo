# Part 1: Unit Tests
- [x] - "[" -> False
- [x] - "[]" -> True
- [] - "[[]" -> False
- [] - "[][]" -> True
- [] - "][][" -> False

# Part 2: Potential Invalid Inputs
- [] - "{[]}" -> Should give an asserition error
- [] - '()" -> Should give an assertion error

# Part 3: Properties
- [] -> If the function spits out True, then there should be as many closing brackets as opening
