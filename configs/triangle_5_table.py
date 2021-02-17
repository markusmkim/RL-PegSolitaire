
config = {
    'is_diamond': False,
    'size': 5,
    'empty_nodes': [[3, 1]],
    'number_of_episodes': 2000,
    'reward_win': 100,
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
    'epsilon_decay_rate': 0.997,
    'epsilon_zero_on_last_episode': True,
    'display_delay': 0.1,
    'display_games': "last"  # all | last | none
}
