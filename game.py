from LearningAlgorithm.actor_critic_algorithm import ActorCriticAlgorithm

# configs
from configs.triangle_5_table import config as triangle_5_table_config
from configs.diamond_4_table import config as diamond_4_table
from configs.diamond_4_network import config as diamond_4_network


config = diamond_4_table

algorithm = ActorCriticAlgorithm(config)

algorithm.evaluate_config(5, 4, ['actor_learning_rate', 'critic_learning_rate'], {
    'actor_learning_rate': [0.1, 0.3, 0.5, 0.7],
    'critic_learning_rate': [0.1, 0.3, 0.5, 0.7]
})

# run training
# algorithm.run()

# plot results from training
# algorithm.plot_results()

# plots when and how many times the game is one during the run
# algorithm.plot_wins()


"""


algorithm = ActorCriticAlgorithm(is_diamond,
                                 size,
                                 empty_nodes,
                                 critic_table,
                                 critic_neural_network_dimensions,
                                 actor_learning_rate,
                                 critic_learning_rate,
                                 actor_eligibility_decay_rate,
                                 critic_eligibility_decay_rate,
                                 actor_discount_factor,
                                 critic_discount_factor,
                                 epsilon,
                                 epsilon_decay_rate,
                                 display_delay)
is_diamond = True
size = 4
empty_nodes = [[1, 1]]
number_of_episodes = 600
critic_table = False
critic_neural_network_dimensions = [32, 1]
actor_learning_rate = 0.2
critic_learning_rate = 0.1 if critic_table else 0.00001
actor_eligibility_decay_rate = 0.9
critic_eligibility_decay_rate = 0.9
actor_discount_factor = 0.9
critic_discount_factor = 0.9 if critic_table else 0.99
epsilon = 0.5
epsilon_decay_rate = number_of_episodes / (number_of_episodes + 2)
display_delay = 1  # seconds
display_all_games = False
"""




