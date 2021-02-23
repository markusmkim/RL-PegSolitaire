

config = {
    'is_diamond': True,
    'size': 6,
    'empty_nodes': [[3, 2]],
    'number_of_episodes': 2500,
    'reward_win': 1000000000,
    'reward_lose': -100,
    'critic_table': True,
    'critic_neural_network_dimensions': [60, 1],
    'actor_learning_rate': 0.1,
    'critic_learning_rate': 0.05,
    'actor_eligibility_decay_rate': 0.5,
    'critic_eligibility_decay_rate': 0.5,
    'actor_discount_factor': 0.9,
    'critic_discount_factor': 0.9,
    'epsilon': 0.7,
    'epsilon_decay_rate': 0.998,
    'epsilon_zero_on_last_episode': True,
    'display_delay': 0.1,
    'display_games': "last",  # "all" | "last" | None
    # add output path to save outputs
    'output_path': "images/example_run/"
}
