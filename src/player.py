class Player:

    def __init__(self, die, is_computer, counter = 5):
        self.die = die
        self.is_computer = is_computer
        self.counter = counter

    def roll_die(self):
        self.die.roll()

    def increment_counter(self):
        self.counter = self.counter + 1

    def decrement_counter(self):
        self.counter = self.counter - 1