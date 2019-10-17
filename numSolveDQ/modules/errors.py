class LengthError(Exception):
    def __init__(self):
        super().__init__("The lengths of xlist and ylist must be the same. In this case they were not.")

class FunctionVariableInputError(Exception):
    def __init__(self):
        super().__init__("The function as typed must include x. This was not the case. Try again.")
class OutofSpecifiedRangeError(Exception):
    def __init__(self):
        super().__init__("You are only allowed to find values of the function in the range you specified when numerically solving the differential equation. You can (a) value(s) out of range. ")