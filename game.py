from LearningAlgorithm.actor_critic import ActorCriticAlgorithm


is_diamond = True
size = 4
empty_nodes = [[1, 1]]
number_of_episodes = 500

critic_table = True
critic_neural_network_dimensions = 0

actor_learning_rate = 0.1
critic_learning_rate = 0.1

actor_eligibility_decay_rate = 0.9
critic_eligibility_decay_rate = 0.9

actor_discount_factor = 0.9
critic_discount_factor = 0.9

epsilon = 0.5
epsilon_decay_rate = number_of_episodes / (number_of_episodes + 2)

display_all_games = False
display_delay = 1.5  # seconds


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


# run training
algorithm.run(display_all_games, number_of_episodes)

# plot results from training
algorithm.plot_results()

# run one episode with visualization and epsilon = 0
algorithm.run(True, 1)

