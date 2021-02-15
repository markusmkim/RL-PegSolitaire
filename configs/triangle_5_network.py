

config = {
    'is_diamond': False,
    'size': 5,
    'empty_nodes': [[3, 1]],
    'number_of_episodes': 2500,
    'reward_win': 100000,
    'reward_lose': -10,
    'critic_table': False,
    'critic_neural_network_dimensions': [30, 20, 10, 1],  # 60-60-1
    'actor_learning_rate': 0.0001,  # 0.001
    'critic_learning_rate': 0.000002,  # 0.000001
    'actor_eligibility_decay_rate': 0.4,  # 0.9
    'critic_eligibility_decay_rate': 0.4,  # 0.9
    'actor_discount_factor': 0.9,
    'critic_discount_factor': 0.9,
    'epsilon': 0.7,
    'epsilon_decay_rate': 0.999,  # 9996
    'epsilon_zero_on_last_episode': True,
    'display_delay': 0.1,
    'display_games': "last"  # all | last | none
}
