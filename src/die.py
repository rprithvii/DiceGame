import numpy as np


class Die:

    
    def __init__(self, die_value = None):
        self._die_value = die_value

    @property
    def die_value(self):
        return self._die_value

    def roll(self):
        # print(f"Rolling the die...")
        # time.sleep(2)
        self._die_value = np.random.randint(low = 1, high = 7)