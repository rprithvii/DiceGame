class Player:
    def __init__(self, die, is_computer, counter = 5):
        self._die = die
        self._is_computer = is_computer
        self._counter = counter

    @property
    def die(self):
        return self._die
    @property
    def is_computer(self):
        return self._is_computer
    @property
    def counter(self):
        return self._counter

    def roll_die(self):
        self.die.roll()

    def increment_counter(self):
        self.counter = self.counter + 1

    def decrement_counter(self):
        self.counter = self.counter - 1