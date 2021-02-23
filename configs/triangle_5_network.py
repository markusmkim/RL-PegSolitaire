

config = {
    'is_diamond': False,
    'size': 5,
    'empty_nodes': [[3, 1]],
    'number_of_episodes': 1200,  # 1400,
    'reward_win': 1000000000,
    'reward_lose': -100,
    'critic_table': False,
    'critic_neural_network_dimensions': [60, 1],
    'actor_learning_rate': 0.01,  # 0.00006
    'critic_learning_rate': 0.00001,  # 0.000005
    'actor_eligibility_decay_rate': 0.5,  # 0.9
    'critic_eligibility_decay_rate': 0.1,  # 0.9
    'actor_discount_factor': 0.9,
    'critic_discount_factor': 0.9,
    'epsilon': 0.5,
    'epsilon_decay_rate': 0.998,  # 0.998,  # 9977
    'epsilon_zero_on_last_episode': True,
    'display_delay': 0.1,
    'display_games': "last",  # "all" | "last" | None
    # add animation path to save plots_last_episode, else None
    'output_path': None
}
