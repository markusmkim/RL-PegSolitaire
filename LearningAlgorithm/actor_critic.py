from Agent.actor import Actor
from Agent.critic import Critic
from Agent.netwrok_critic import NetworkCritic
from SimWorld.peg_player import PegPlayer
from SimWorld.peg_board import PegBoard
from Helpers.helpers import get_possible_actions
from Helpers.converters import convert_list_to_string, convert_string_to_list
from Helpers.plotters import visualize_board, plot_values, plot_mean_values
import numpy as np

from time import sleep


class ActorCriticAlgorithm:
    def __init__(self,
                 is_diamond,
                 size,
                 empty_nodes,
                 critic_table,
                 critic_neural_network_dimensions,
                 actor_learning_rate,
                 critic_learning_rate,
                 actor_eligibility_decay_rate,
                 critic_eligibility_decay_rate,
                 actor_discount_factor,
                 critic_discount_factor,
                 epsilon,
                 epsilon_decay_rate,
                 display_delay):

        self.is_diamond = is_diamond
        self.size = size
        self.empty_nodes = empty_nodes
        self.critic_table = critic_table
        self.critic_neural_network_dimensions = critic_neural_network_dimensions
        self.display_delay = display_delay

        # Initialize actor and critic
        self.actor = Actor(get_possible_actions,
                           actor_learning_rate,
                           actor_discount_factor,
                           actor_eligibility_decay_rate,
                           epsilon,
                           epsilon_decay_rate)
        if critic_table:
            self.critic = Critic(critic_learning_rate,
                                 critic_discount_factor,
                                 critic_eligibility_decay_rate)
        else:
            input_dim = size**2 if is_diamond else (size * (size + 1)) // 2
            self.critic = NetworkCritic(input_dim,
                                        critic_neural_network_dimensions,
                                        critic_learning_rate,
                                        critic_discount_factor,
                                        critic_eligibility_decay_rate)

        # history of pegs left after each episode
        self.total_pegs_left_per_episode = []


    def test_network_critic(self):
        # print(self.critic.model.summary())
        self.critic.reset_eligibilities()
        self.critic.fit(np.arange(16).reshape(1, 16), 5, 2)


    def run(self, display, episodes, epsilon_is_zero=False):
        # set epsilon if needed
        if epsilon_is_zero:
            self.actor.set_epsilon_to_zero()

        # reset history of pegs left after each episode
        self.total_pegs_left_per_episode = []

        for i in range(episodes):
            peg_board = PegBoard(self.size, self.is_diamond, self.empty_nodes)
            peg_player = PegPlayer(peg_board)

            state = convert_list_to_string(peg_board.grid)
            action = self.actor.choose_action(state)

            if display:
                visualize_board(convert_string_to_list(state))

            self.actor.reset_episode_parameters()
            self.critic.reset_episode_parameters()

            while not peg_player.game_over():
                self.actor.set_eligibility(state, action)
                if self.critic_table:
                    self.critic.set_eligibility(state)

                next_state, reward = peg_player.execute_action(action)
                if not peg_player.game_over():
                    next_action = self.actor.choose_action(next_state)
                else:
                    next_action = None

                if self.critic_table:
                    td_error = self.critic.get_TD_error(state, next_state, reward)
                    self.critic.update_values_and_eligibilities(td_error)
                else:
                    target, td_error = self.critic.get_target_and_TD_error(state, next_state, reward)
                    self.critic.update_model_and_eligibilities(state, target, td_error)

                self.actor.update_values_and_eligibilities(td_error)

                state = next_state
                action = next_action

                if display:
                    sleep(1.5)
                    visualize_board(convert_string_to_list(state))

            self.total_pegs_left_per_episode.append(peg_board.total_pegs_left)
            print('Episode ', i, ' done')

    def plot_results(self):
        plot_values(self.total_pegs_left_per_episode)
        sleep(self.display_delay)
        plot_mean_values(self.total_pegs_left_per_episode)
        sleep(self.display_delay)

