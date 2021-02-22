

config = {
    'is_diamond': False,
    'size': 4,
    'empty_nodes': [[1, 1]],
    'number_of_episodes': 1200,
    'reward_win': 1000000000,
    'reward_lose': -100,
    'critic_table': False,
    'critic_neural_network_dimensions': [60, 1],
    'actor_learning_rate': 0.01,
    'critic_learning_rate': 0.00001,
    'actor_eligibility_decay_rate': 0.5,
    'critic_eligibility_decay_rate': 0.1,
    'actor_discount_factor': 0.9,
    'critic_discount_factor': 0.9,
    'epsilon': 0.5,
    'epsilon_decay_rate': 0.998,
    'epsilon_zero_on_last_episode': True,
    'display_delay': 0.1,
    'display_games': "last",  # "all" | "last" | None
    # add animation path to save plots as animation, else None
    'animation_path': None
}
