
class Critic:

    def __init__(self, learning_rate, discount_factor, eligibility_decay_rate):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.eligibility_decay_rate = eligibility_decay_rate
        self.table = {}
        self.state_history = []

    def reset_eligibilities_and_history(self):
        self.state_history = []
        for state in self.table:
            self.table[state]['eligibility'] = 0

    def set_eligibility(self, state):
        if state not in self.table:
            self.table[state] = {
                "value": 0
            }
        self.table[state]['eligibility'] = 1
        self.state_history.append(state)

    def get_TD_error(self, current_state, next_state, reward):
        if next_state not in self.table:
            self.table[next_state] = {
                "value": 0
            }
        return reward + self.discount_factor * self.table[next_state]['value'] - self.table[current_state]['value']

    def update_values_and_eligibilities(self, td_error):
        for state in self.state_history:
            self.table[state] = {
                'value': self.table[state]['value'] + self.learning_rate * td_error * self.table[state]['eligibility'],
                'eligibility': self.discount_factor * self.eligibility_decay_rate * self.table[state]['eligibility']
            }
