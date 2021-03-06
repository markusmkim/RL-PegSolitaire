import random


class Actor:
    def __init__(self, get_possible_actions, learning_rate, discount_factor,
                 eligibility_decay_rate, epsilon, epsilon_decay_rate):
        self.get_possible_actions = get_possible_actions
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.eligibility_decay_rate = eligibility_decay_rate
        self.epsilon = epsilon
        self.epsilon_decay_rate = epsilon_decay_rate
        self.table = {}
        self.state_action_history = []


    def reset_episode_parameters(self):
        # Epsilon decay
        self.epsilon = self.epsilon * self.epsilon_decay_rate
        self.state_action_history = []
        for state in self.table:
            for action in self.table[state]:
                self.table[state][action]['eligibility'] = 0


    def set_eligibility(self, state, action):
        self.table[state][action]['eligibility'] = 1
        self.state_action_history.append([state, action])


    def set_epsilon_to_zero(self):
        self.epsilon = 0


    def reset_epsilon(self, epsilon):
        self.epsilon = epsilon


    def choose_action(self, state):
        # if state is not visited before, initialize values for all state-action pairs from state
        if state not in self.table:
            self.table[state] = {}
            for action in self.get_possible_actions(state):
                self.table[state][action] = {
                    'probability': 0,
                    'eligibility': 0
                }

        possible_actions = list(self.table[state].keys())

        # if no possible actions, return None
        if len(possible_actions) == 0:
            return None

        # do random action by chance, where the probability is decided by epsilon
        if random.random() < self.epsilon:
            random_index = random.randrange(len(self.table[state]))
            return possible_actions[random_index]

        # else, find best action
        best_action_index = 0
        highest_probability = -100000000
        for index, action in enumerate(self.table[state]):
            if self.table[state][action]['probability'] > highest_probability:
                best_action_index = index
                highest_probability = self.table[state][action]['probability']

        return possible_actions[best_action_index]


    def update_values_and_eligibilities(self, td_error):
        # loop through all state action pairs visited in this episode so far, and update values and elegibilities
        for state_action in self.state_action_history:
            state = state_action[0]
            action = state_action[1]

            self.table[state][action] = {
                'probability':
                    self.table[state][action]['probability'] +
                    self.learning_rate * td_error *
                    self.table[state][action]['eligibility'],
                'eligibility':
                    self.discount_factor *
                    self.eligibility_decay_rate *
                    self.table[state][action]['eligibility']
            }
