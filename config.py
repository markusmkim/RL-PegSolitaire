"""
def get_params(is_diamond, size, number_of_episodes, critic_table):
    number_of_nodes = size**2 if is_diamond else (size * (size + 1)) // 2

    actor_learning_rate = 0.1
    critic_learning_rate = 0.1 if critic_table else 0.00001

    actor_eligibility_decay_rate = 0.9
    critic_eligibility_decay_rate = 0.9

    actor_discount_factor = 0.9
    critic_discount_factor = 0.9 if critic_table else 0.99

    epsilon = 0.5
    epsilon_decay_rate = number_of_episodes / (number_of_episodes + 2)


    critic_neural_network_dimensions = [32, 1] if not critic_table else None


    return epsilon, \
           epsilon_decay_rate, \
           actor_learning_rate, \
           critic_learning_rate, \
           actor_eligibility_decay_rate, \
           critic_eligibility_decay_rate, \
           actor_discount_factor, \
           critic_discount_factor, \
           critic_neural_network_dimensions
"""