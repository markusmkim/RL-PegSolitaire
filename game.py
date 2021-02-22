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
config = custom_config

# initialize actor-critic model
algorithm = ActorCriticAlgorithm(config)


# run model
algorithm.run()

# show results
algorithm.plot_results()

