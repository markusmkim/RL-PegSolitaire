from LearningAlgorithm.actor_critic_algorithm import ActorCriticAlgorithm

# --- Configurations --- #
# Task 2
from configs.triangle_5_table import config as triangle_5_table
from configs.triangle_5_network import config as triangle_5_network

# Task 3
from configs.diamond_4_table import config as diamond_4_table
from configs.diamond_4_network import config as diamond_4_network

# Task 4 (extra boards)
from configs.triangle_4_table import config as triangle_4_table
from configs.triangle_4_network import config as triangle_4_network
from configs.custom import config as custom_config


# read config
config = triangle_5_network

# initialize actor-critic model
algorithm = ActorCriticAlgorithm(config)

"""
algorithm.evaluate_config(6, 8, ['actor_learning_rate', 'critic_learning_rate', 'epsilon_decay_rate'], {
    'actor_learning_rate': [0.1, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05],
    'critic_learning_rate': [0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05],
    'epsilon_decay_rate': [0.9999, 0.99985, 0.9998, 0.99975, 0.9997, 0.99965, 0.9996, 0.99955]
})
"""

# run model
algorithm.run()

# show results
algorithm.plot_results()

# plots when and how many times the game is one during the run
# algorithm.plot_wins()

