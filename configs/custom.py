

config = {
    'is_diamond': True,
    'size': 6,
    'empty_nodes': [[3, 2]],
    'number_of_episodes': 3200,
    'reward_win': 1000000000,
    'reward_lose': -100,
    'critic_table': True,
    'critic_neural_network_dimensions': [60, 1],
    'actor_learning_rate': 0.1,
    'critic_learning_rate': 0.05,
    'actor_eligibility_decay_rate': 0.6,
    'critic_eligibility_decay_rate': 0.6,
    'actor_discount_factor': 0.9,
    'critic_discount_factor': 0.9,
    'epsilon': 0.8,
    'epsilon_decay_rate': 0.997,
    'epsilon_zero_on_last_episode': True,
    'display_delay': 0.1,
    'display_games': "last",  # "all" | "last" | None
    # add output path to save outputs
    'output_path': None,  # "images/example_run/"
}
