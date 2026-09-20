class Solver:
    def solve(self, brackets: str) -> bool:
        # Loop through every element, adding
        # Open brackets to the stack
        # and popping them off
        # when a closed bracket is encountered
        bracket_stack = []
        for bracket in brackets:
            if bracket == '[':
                bracket_stack.append(bracket)
            elif bracket == ']':
                if len(bracket_stack) > 0:
                    bracket_stack.pop()
                else:
                    return False
        return False if len(bracket_stack) else True
