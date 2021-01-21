import random


class Actor:

    def __init__(self, states, get_possible_actions):
        self.state_action_map = {}

        for state in states:
            self.state_action_map[state] = {}

            for action in get_possible_actions(state):
                self.state_action_map[state][action] = 0
