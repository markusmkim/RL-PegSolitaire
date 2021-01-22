import random


class Critic:

    def __init__(self, states, learning_rate, discount_factor, eligibility_decay_rate):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.eligibility_decay_rate = eligibility_decay_rate

        self.table = {}

        for state in states:
            self.table[state] = {
                'value': random.randrange(5),
                'eligibility': 0
            }

        self.state_history = []


    def reset_eligibilities(self):
        for state in self.table:
            self.table[state]['eligibility'] = 0


    def update_eligibility(self, state):
        self.table[state]['eligibility'] = 1
        self.state_history.append(state)


    def get_TD_error(self, current_state, next_state, reward):
        return reward + self.discount_factor * self.table[next_state]['value'] - self.table[current_state]['value']


    def update_values_and_eligibilities(self, TD_error):
        for state in self.state_history:
            self.table[state] = {
                'value': self.table[state]['value'] + self.learning_rate * TD_error * self.table[state]['eligibility'],
                'eligibility': self.discount_factor * self.eligibility_decay_rate * self.table[state]['eligibility']
            }



