

config = {
    'is_diamond': True,
    'size': 6,
    'empty_nodes': [[2, 2], [3, 1], [0, 0]],
    'number_of_episodes': 1200,
    'reward_win': 100,
    'reward_lose': -1,
    'critic_table': True,
    'critic_neural_network_dimensions': [32, 1],
    'actor_learning_rate': 0.01,
    'critic_learning_rate': 0.001,
    'actor_eligibility_decay_rate': 0.6,
    'critic_eligibility_decay_rate': 0.6,
    'actor_discount_factor': 0.9,
    'critic_discount_factor': 0.9,
    'epsilon': 0.5,
    'epsilon_decay_rate': 0.997,  # number_of_episodes / (number_of_episodes + 2)
    'epsilon_zero_on_last_episode': True,
    'display_delay': 0.1,
    'display_games': "last"  # "all" | "last" | None
}
