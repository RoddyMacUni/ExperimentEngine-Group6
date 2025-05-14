from typing import Callable

class TimeCounter:
    secondsCount: int
    minutesCount: int
    onMinutesIncrement: Callable[[int], None]

    def __init__(self, onMinutesIncrement: Callable[[int], None]):
        self.secondsCount = 0
        self.minutesCount = 0
        self.onMinutesIncrement = onMinutesIncrement

    def increment(self):
        self.secondsCount += 1
        if self.secondsCount >= 60:
            self.secondsCount = 0
            self.minutesCount += 1
            self.onMinutesIncrement(self.minutesCount)

    def reset(self):
        self.secondsCount = 0
        self.minutesCount = 0
            

