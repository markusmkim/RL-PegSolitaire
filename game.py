from Agent.actor import Actor
from Agent.critic import Critic
from SimWorld.peg_player import PegPlayer
from SimWorld.peg_board import PegBoard
from Helpers.helpers import get_possible_actions
from Helpers.converters import convert_list_to_string, convert_string_to_list
from Helpers.plotters import visualize_board

from time import sleep


is_diamond = True
size = 5
empty_nodes = [[2, 2]]
number_of_episodes = 4000

critic_table = True
critic_neural_network_dimensions = 0

actor_learning_rate = 0.1
critic_learning_rate = 0.1

actor_eligibility_decay_rate = 0.9
critic_eligibility_decay_rate = 0.9

actor_discount_factor = 0.9
critic_discount_factor = 0.9

epsilon = 0.5
epsilon_decay_rate = number_of_episodes / (number_of_episodes + 2)

display = False
display_delay = 1.5  # seconds

# Initialize actor and critic
actor = Actor(get_possible_actions, actor_learning_rate, actor_discount_factor,
              actor_eligibility_decay_rate, epsilon, epsilon_decay_rate)
critic = Critic(critic_learning_rate, critic_discount_factor, critic_eligibility_decay_rate)

total_pegs_left_list = []


def run(display, episodes):

    for i in range(episodes):
        peg_board = PegBoard(size, is_diamond, empty_nodes)
        peg_player = PegPlayer(peg_board)

        state = convert_list_to_string(peg_board.grid)
        action = actor.choose_action(state)

        if display:
            visualize_board(convert_string_to_list(state))

        actor.reset_eligibilities_and_history()
        critic.reset_eligibilities_and_history()

        while not peg_player.game_over():
            actor.set_eligibility(state, action)
            critic.set_eligibility(state)

            next_state, reward = peg_player.execute_action(action)
            if not peg_player.game_over():
                next_action = actor.choose_action(next_state)
            else:
                next_action = None

            td_error = critic.get_TD_error(state, next_state, reward)
            actor.update_values_and_eligibilities(td_error)
            critic.update_values_and_eligibilities(td_error)

            state = next_state
            action = next_action

            if display:
                sleep(1.5)
                visualize_board(convert_string_to_list(state))

        total_pegs_left_list.append(peg_board.total_pegs_left)

        # print("Episode ", i, " er ferdig!")


run(False, number_of_episodes)

