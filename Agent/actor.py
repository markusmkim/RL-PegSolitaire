import random


class Actor:

    def __init__(self, states, get_possible_actions, learning_rate, discount_factor, eligibility_decay_rate, epsilon, epsilon_decay_rate):
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.eligibility_decay_rate = eligibility_decay_rate
        self.epsilon = epsilon
        self.epsilon_decay_rate = epsilon_decay_rate
        self.table = {}

        for state in states:
            self.table[state] = {}

            for action in get_possible_actions(state):
                self.table[state][action] = {
                    'probability': 0,
                    'eligibility': 0
                }

        self.state_action_history = []

    def reset_eligibilities(self):
        for state in self.table:
            for action in state:
                self.table[state][action]['eligibility'] = 0

    def update_eligibility(self, state, action):
        self.table[state][action]['eligibility'] = 1
        self.state_action_history.append([state, action])

    def choose_action(self, state):
        possible_actions = self.table[state].keys()

        if random.random() < self.epsilon:
            random_index = random.randrange(len(self.table[state]))

            return possible_actions[random_index]

        best_action_index = 0
        highest_probability = 0
        for index, action in enumerate(self.table[state]):
            if action['probability'] > highest_probability:
                best_action_index = index
                highest_probability = action['probability']

        return possible_actions[best_action_index]

    def update_values_and_eligibilities(self, TD_error):
        for state_action in self.state_action_history:
            state = state_action[0]
            action = state_action[1]

            self.table[state][action] = {
                'probability': self.table[state][action]['probability'] + self.learning_rate * TD_error * self.table[state][action]['eligibility'],
                'eligibility': self.discount_factor * self.eligibility_decay_rate * self.table[state][action]['eligibility']
            }

            # Normalize probabilities for possible actions from state
            total_prob = 0
            for action in self.table[state]:
                total_prob = self.table[state][action]['probability']

            for action in self.table[state]:
                self.table[state][action]['probability'] = self.table[state][action]['probability'] / total_prob
