from Agent.actor import Actor
from Agent.critic import Critic
from SimWorld.peg_player import PegPlayer
from SimWorld.peg_board import PegBoard
from SimWorld.helpers import get_all_possible_states_from_initial_state, convert_list_to_string, get_possible_actions, get_all_possible_states
from SimWorld.board_visualizer import visualize_board

from time import sleep


is_diamond = False
size = 4
empty_nodes = [[0, 0]]
number_of_episodes = 1000

critic_table = True
critic_neural_network_dimensions = 0

actor_learning_rate = 0.1
critic_learning_rate = 0.1

actor_eligibility_decay_rate = 0.9
critic_eligibility_decay_rate = 0.9

actor_discount_factor = 0.9
critic_discount_factor = 0.9

epsilon = 0.5
epsilon_decay_rate = 0.9

display = False
display_delay = 1.5  # seconds


# Run
peg_board = PegBoard(size, is_diamond, empty_nodes)
peg_player = PegPlayer(peg_board)

# s = get_all_possible_states_from_initial_state(convert_list_to_string(peg_board.grid))
# print('Antall mulige states: ', len(s))
# print(get_possible_actions(convert_list_to_string(peg_board.grid)))
"""
for grid in s:
    visualize_board(grid)
    # print('main- grid: ', grid)
    sleep(1.5)
"""

print(len(get_all_possible_states(True, 4)))
# Initialize actor and critic
# actor = Actor()
# critic = Critic()
# actor = Actor(states, get_possible_actions, actor_learning_rate, actor_discount_factor, actor_eligibility_decay_rate, epsilon, epsilon_decay_rate)
# critic = Critic(states, critic_learning_rate, critic_discount_factor, critic_eligibility_decay_rate)
