from Agent.actor import Actor
from Agent.critic import Critic
from Agent.network_critic import NetworkCritic
from SimWorld.peg_player import PegPlayer
from SimWorld.peg_board import PegBoard
from Helpers.helpers import get_possible_actions
from Helpers.converters import convert_list_to_string, convert_string_to_list
from Helpers.plotters import visualize_board, plot_values, plot_mean_values
import numpy as np

from time import sleep


class ActorCriticAlgorithm:
    def __init__(self, config):

        self.config = config

        # Initialize actor and critic
        self.actor = Actor(get_possible_actions,
                           config['actor_learning_rate'],
                           config['actor_discount_factor'],
                           config['actor_eligibility_decay_rate'],
                           config['epsilon'],
                           config['epsilon_decay_rate'])
        if config['critic_table']:
            self.critic = Critic(config['critic_learning_rate'],
                                 config['critic_discount_factor'],
                                 config['critic_eligibility_decay_rate'])
        else:
            input_dim = config['size'] ** 2 if config['is_diamond'] else (config['size'] * (config['size'] + 1)) // 2
            self.critic = NetworkCritic(input_dim,
                                        config['critic_neural_network_dimensions'],
                                        config['critic_learning_rate'],
                                        config['critic_discount_factor'],
                                        config['critic_eligibility_decay_rate'])

        # history of pegs left after each episode
        self.total_pegs_left_per_episode = []


    def run(self):
        # reset history of pegs left after each episode
        self.total_pegs_left_per_episode = []

        for i in range(self.config['number_of_episodes']):
            print(self.actor.epsilon)
            peg_board = PegBoard(self.config['size'], self.config['is_diamond'], self.config['empty_nodes'])
            peg_player = PegPlayer(peg_board)

            # whether this episode should be displayed or not
            display = self.config['display_games'] == "all" or (
                      self.config['display_games'] == "last" and i == self.config['number_of_episodes'] - 1)

            # set epsilon to zero for last episode if desired
            if self.config['epsilon_zero_on_last_episode'] and i == self.config['number_of_episodes'] - 1:
                self.actor.set_epsilon_to_zero()

            state = convert_list_to_string(peg_board.grid)
            action = self.actor.choose_action(state)
            if not action:
                print('No legal actions!')
                break

            if display:
                visualize_board(convert_string_to_list(state))

            self.actor.reset_episode_parameters()
            self.critic.reset_episode_parameters()

            while not peg_player.game_over():
                self.actor.set_eligibility(state, action)
                if self.config['critic_table']:
                    self.critic.set_eligibility(state)

                next_state, reward = peg_player.execute_action(action)
                if not peg_player.game_over():
                    next_action = self.actor.choose_action(next_state)
                else:
                    next_action = None

                if self.config['critic_table']:
                    td_error = self.critic.get_TD_error(state, next_state, reward)
                    self.critic.update_values_and_eligibilities(td_error)
                else:
                    target, td_error = self.critic.get_target_and_TD_error(state, next_state, reward)
                    self.critic.update_model_and_eligibilities(state, target, td_error)

                self.actor.update_values_and_eligibilities(td_error)

                state = next_state
                action = next_action

                if display:
                    sleep(self.config['display_delay'])
                    visualize_board(convert_string_to_list(state))

            self.total_pegs_left_per_episode.append(peg_board.total_pegs_left)
            if i == self.config['number_of_episodes'] - 1:
                print('total pegs left last episode - ', peg_board.total_pegs_left)
            # print('Episode ', i, ' done')


    def plot_results(self):
        plot_values(self.total_pegs_left_per_episode)
        sleep(self.config['display_delay'])
        plot_mean_values(self.total_pegs_left_per_episode)
        sleep(self.config['display_delay'])
