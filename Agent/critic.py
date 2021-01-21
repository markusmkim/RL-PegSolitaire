import random


class Critic:

    def __init__(self, states):
        self.state_table = {}

        for state in states:
            self.state_table[state] = random.randrange(5)
