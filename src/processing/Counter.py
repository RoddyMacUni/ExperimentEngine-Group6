from typing import Callable

class Counter:
    minorIncrement: int
    majorIncrement: int
    total: int #Never reset

    majorIncrementThreshold: int
    onMajorIncrement: Callable[[int], None]

    def __init__(self, majorIncrementThreshold: int, onMajorIncrement: Callable[[int], None]):
        self.minorIncrement = 0
        self.majorIncrement = 0
        self.total = 0

        self.majorIncrementThreshold = majorIncrementThreshold
        self.onMajorIncrement = onMajorIncrement

    def increment(self):
        self.total += 1
        self.minorIncrement += 1
        if self.minorIncrement >= self.majorIncrementThreshold:
            self.minorIncrement = 0
            self.majorIncrement += 1
            self.onMajorIncrement(self.majorIncrement)

    def reset(self):
        self.minorIncrement = 0
        self.majorIncrement = 0
            

