

config = {
    'is_diamond': True,
    'size': 4,
    # [[1, 1]] and [[2, 2]] solvable boards
    'empty_nodes': [[1, 1]],
    'number_of_episodes': 1000,
    'reward_win': 1000,
    'reward_lose': -1,
    'critic_table': True,
    'critic_neural_network_dimensions': None,
    'actor_learning_rate': 0.1,
    'critic_learning_rate': 0.05,
    'actor_eligibility_decay_rate': 0.6,
    'critic_eligibility_decay_rate': 0.6,
    'actor_discount_factor': 0.9,
    'critic_discount_factor': 0.9,
    'epsilon': 0.5,
    'epsilon_decay_rate': 0.997,  # number_of_episodes / (number_of_episodes + 2)
    'epsilon_zero_on_last_episode': True,
    'display_delay': 0.1,
    'display_games': "last",  # "all" | "last" | None
    # add animation path to save plots_last_episode, else None
    'output_path': None
}

"""
NoE   -   EDR
4000  -   0.9994
1500  -   0.9985
600   -   0.996
"""


