from Agent.actor import Actor
from Agent.critic import Critic
from Agent.network_critic import NetworkCritic
from SimWorld.peg_player import PegPlayer
from SimWorld.peg_board import PegBoard
from Helpers.helpers import get_possible_actions
from Helpers.converters import convert_list_to_string, convert_string_to_list
from Helpers.plotters import BoardVisualizer, plot_values, plot_mean_values
from time import sleep


class ActorCriticAlgorithm:
    def __init__(self, config):

        self.config = config

        # Initialize actor and critic
        self.actor = Actor(get_possible_actions,
                           config['actor_learning_rate'],
                           config['actor_discount_factor'],
                           config['actor_eligibility_decay_rate'],
                           config['epsilon'],
                           config['epsilon_decay_rate'])
        if config['critic_table']:
            self.critic = Critic(config['critic_learning_rate'],
                                 config['critic_discount_factor'],
                                 config['critic_eligibility_decay_rate'])
        else:
            input_dim = config['size'] ** 2 if config['is_diamond'] else (config['size'] * (config['size'] + 1)) // 2
            self.critic = NetworkCritic(input_dim,
                                        config['critic_neural_network_dimensions'],
                                        config['critic_learning_rate'],
                                        config['critic_discount_factor'],
                                        config['critic_eligibility_decay_rate'])

        # history of pegs left after each episode
        self.total_pegs_left_per_episode = []

        # board visualizer for plotting and gif creation
        self.board_visualizer = BoardVisualizer()


    def run(self):
        # reset history of pegs left
        self.total_pegs_left_per_episode = []

        for i in range(self.config['number_of_episodes']):
            print('Episode ', i)
            # initialize SimWorld: PegBoard and PegPlayer
            peg_board = PegBoard(self.config['size'], self.config['is_diamond'], self.config['empty_nodes'])
            peg_player = PegPlayer(peg_board, self.config['reward_win'], self.config['reward_lose'])

            # whether this episode should be displayed or not
            display = self.config['display_games'] == "all" or (
                      self.config['display_games'] == "last" and i == self.config['number_of_episodes'] - 1)

            # set epsilon to zero for last episode if desired
            if self.config['epsilon_zero_on_last_episode'] and i == self.config['number_of_episodes'] - 1:
                self.actor.set_epsilon_to_zero()

            # get initial state
            state = convert_list_to_string(peg_board.grid)

            # Actor: choose first action
            action = self.actor.choose_action(state)

            # if action == None --> no legal actions for this board configuration
            if not action:
                print('No legal actions!')
                break

            if display:
                self.board_visualizer.visualize_board(convert_string_to_list(state))

            # reset eligibilities
            self.actor.reset_episode_parameters()  # this method will also decrease epsilon
            self.critic.reset_episode_parameters()

            while not peg_player.game_over():
                # set eligibilities to 1 for current state (and action for actor). For critic, only if table based.
                self.actor.set_eligibility(state, action)
                if self.config['critic_table']:
                    self.critic.set_eligibility(state)

                # execute action, receive next state and reward from PegPlayer in SimWorld
                next_state, reward = peg_player.execute_action(action)

                # Actor: choose next action if game is not over
                if not peg_player.game_over():
                    next_action = self.actor.choose_action(next_state)
                else:
                    next_action = None

                # Critic: compute TD error and update values/model and eligibilities
                if self.config['critic_table']:
                    td_error = self.critic.get_TD_error(state, next_state, reward)
                    self.critic.update_values_and_eligibilities(td_error)
                else:
                    target, td_error = self.critic.get_target_and_TD_error(state, next_state, reward)
                    self.critic.update_model_and_eligibilities(state, target, td_error)

                # Actor: use TD error to update SAP values and eligibilities
                self.actor.update_values_and_eligibilities(td_error)

                state = next_state
                action = next_action

                # visualize game is display flag is True
                if display:
                    sleep(self.config['display_delay'])
                    self.board_visualizer.visualize_board(convert_string_to_list(state))

            # save result for plotting
            self.total_pegs_left_per_episode.append(peg_board.total_pegs_left)

            # print result if last episode
            if i == self.config['number_of_episodes'] - 1:
                print('Total pegs left last episode - ', peg_board.total_pegs_left)

        if self.config['animation_path'] is not None:
            self.board_visualizer.save_animation(self.config['animation_path'], self.config['display_delay'])


    def plot_results(self):
        plot_values(self.total_pegs_left_per_episode)
        sleep(self.config['display_delay'])
        plot_mean_values(self.total_pegs_left_per_episode)
        sleep(self.config['display_delay'])


    def plot_wins(self):
        episodes_won = []
        episode = 0
        for total_pegs in self.total_pegs_left_per_episode:
            if total_pegs == 1:
                episodes_won.append(episode)
            episode += 1
        print("Antall seire: ", len(episodes_won))
        print("Episoder vunnet: ", episodes_won)


    def evaluate_config(self, runs, number_of_parameter_values=1, parameters=None, parameter_values=None):
        # If parameters are provided, this function aims to compare
        # evaluations with different values for provided parameter.
        # The specific parameters of most interest are:
        # 'actor_learning_rate'
        # 'critic_learning_rate'
        # 'actor_eligibility_decay_rate'
        # 'critic_eligibility_decay_rate'
        # 'actor_discount_factor':
        # 'critic_discount_factor':
        # whose values all range from 0 to 1

        # number_of_parameter_values are the number of provided values per parameter
        # parameters are the parameters of interest given as strings
        # parameter_values is a dictionary with parameters as keys and a list of parameter values as values

        print("Epsilon vil avslutte på",
              self.config['epsilon'] * (self.config['epsilon_decay_rate'] ** self.config['number_of_episodes']))

        for parameter_value in range(number_of_parameter_values):
            if number_of_parameter_values > 1:
                if 'actor_learning_rate' in parameters:
                    self.config['actor_learning_rate'] = parameter_values[
                        'actor_learning_rate'][parameter_value]
                if 'critic_learning_rate' in parameters:
                    self.config['critic_learning_rate'] = parameter_values[
                        'critic_learning_rate'][parameter_value]
                if 'actor_eligibility_decay_rate' in parameters:
                    self.config['actor_eligibility_decay_rate'] = parameter_values[
                        'actor_eligibility_decay_rate'][parameter_value]
                if 'critic_eligibility_decay_rate' in parameters:
                    self.config['critic_eligibility_decay_rate'] = parameter_values[
                        'critic_eligibility_decay_rate'][parameter_value]
                if 'actor_discount_factor' in parameters:
                    self.config['actor_discount_factor'] = parameter_values[
                        'actor_discount_factor'][parameter_value]
                if 'critic_discount_factor' in parameters:
                    self.config['critic_discount_factor'] = parameter_values[
                        'critic_discount_factor'][parameter_value]

            win_history = []
            first_win_history = []
            won_last_history = []
            mean_pegs_last_100_history = []

            for run in range(runs):
                #if number_of_parameter_values == 1:
                print("Run: ", run)

                # number of wins per run
                number_of_wins = 0

                # the episode with the first win of the run
                first_win = self.config['number_of_episodes'] + 1

                # mean number of pegs left for the last 100 episodes
                # tells much of the true performance as epsilon is close to zero
                pegs_last_100 = []

                self.total_pegs_left_per_episode = []

                for i in range(self.config['number_of_episodes']):
                    peg_board = PegBoard(self.config['size'], self.config['is_diamond'], self.config['empty_nodes'])
                    peg_player = PegPlayer(peg_board, self.config['reward_win'], self.config['reward_lose'])

                    # set epsilon to zero for last episode if desired
                    if i == self.config['number_of_episodes'] - 1:
                        self.actor.set_epsilon_to_zero()

                    state = convert_list_to_string(peg_board.grid)
                    action = self.actor.choose_action(state)
                    if not action:
                        print('No legal actions!')
                        break

                    self.actor.reset_episode_parameters()
                    self.critic.reset_episode_parameters()

                    while not peg_player.game_over():
                        self.actor.set_eligibility(state, action)
                        if self.config['critic_table']:
                            self.critic.set_eligibility(state)

                        next_state, reward = peg_player.execute_action(action)
                        if not peg_player.game_over():
                            next_action = self.actor.choose_action(next_state)
                        else:
                            next_action = None

                        if self.config['critic_table']:
                            td_error = self.critic.get_TD_error(state, next_state, reward)
                            self.critic.update_values_and_eligibilities(td_error)
                        else:
                            target, td_error = self.critic.get_target_and_TD_error(state, next_state, reward)
                            self.critic.update_model_and_eligibilities(state, target, td_error)

                        self.actor.update_values_and_eligibilities(td_error)

                        state = next_state
                        action = next_action

                    self.total_pegs_left_per_episode.append(peg_board.total_pegs_left)

                    # checks if game is won
                    if peg_board.total_pegs_left == 1:
                        number_of_wins += 1

                        # checks if this is the first win of the run
                        if first_win == self.config['number_of_episodes'] + 1:
                            first_win = i

                    # adds pegs left for the last 100 runs
                    if i > self.config['number_of_episodes'] - 101:
                        pegs_last_100.append(peg_board.total_pegs_left)

                    # this is the last run
                    if i == self.config['number_of_episodes'] - 1:
                        win_history.append(number_of_wins)
                        first_win_history.append(first_win)

                        # 1 = win  |  0 = loss
                        won_last = 0
                        if peg_board.total_pegs_left == 1:
                            won_last = 1
                        won_last_history.append(won_last)

                        total_pegs_left = 0
                        for pegs_left in pegs_last_100:
                            total_pegs_left += pegs_left
                        mean_pegs_last_100 = total_pegs_left / len(pegs_last_100)
                        mean_pegs_last_100_history.append(mean_pegs_last_100)

                        self.actor.reset_epsilon(self.config['epsilon'])

            total_number_of_wins = 0
            for win in win_history:
                total_number_of_wins += win
            mean_number_of_wins = total_number_of_wins / len(win_history)

            total_first_wins = 0
            for first_win in first_win_history:
                total_first_wins += first_win
            mean_first_win = total_first_wins / len(first_win_history)

            total_last_wins = 0
            for last_win in won_last_history:
                total_last_wins += last_win
            mean_won_last = total_last_wins / len(won_last_history)

            total_mean_pegs_last_100 = 0
            for mean_pegs_last_100 in mean_pegs_last_100_history:
                total_mean_pegs_last_100 += mean_pegs_last_100
            mean_mean_pegs_last_100 = total_mean_pegs_last_100 / len(mean_pegs_last_100_history)

            if number_of_parameter_values == 1:
                print("Evaluering av config:")
                print("")
                print("Gjennomsnittlig antall seire: ", mean_number_of_wins)
                print("")
                print("Gjennomsnittlig første seier: ", mean_first_win)
                print("")
                print("Gjennomsnittlig siste seier: ", mean_won_last)
                print("")
                print("Gjennomsnittlig pegs igjen på siste 100: ", mean_mean_pegs_last_100)
                print("")

            else:
                print("")
                print("Evaluering av config med disse parameterverdiene:")
                for parameter in parameters:
                    print(parameter, ": ", parameter_values[parameter][parameter_value])
                print("Gjennomsnittlig antall seire:  ", mean_number_of_wins)
                print("Gjennomsnittlig siste seier:   ", mean_won_last)
