import tensorflow as tf
from tensorflow import keras
import numpy as np
from Helpers.converters import convert_string_to_list


class NetworkCritic:
    def __init__(self, input_dim, layers, learning_rate, discount_factor, eligibility_decay_rate):
        self.input_dim = input_dim
        self.layers = layers
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.eligibility_decay_rate = eligibility_decay_rate
        self.eligibilities = []
        self.model = self.build_model()


    def build_model(self):
        model = keras.Sequential()
        first_layer = self.layers[0]
        model.add(keras.layers.Dense(first_layer, activation='relu', input_shape=(self.input_dim, )))
        for layer in self.layers[1:-1]:
            model.add(keras.layers.Dense(layer, activation='relu'))
        if len(self.layers) > 1:
            last_layer = self.layers[-1]
            model.add(keras.layers.Dense(last_layer))
        loss = keras.losses.MeanSquaredError()
        optimizer = keras.optimizers.Adam(learning_rate=self.learning_rate)
        model.compile(optimizer=optimizer, loss=loss)
        print(model.summary())
        return model


    def reset_episode_parameters(self):
        eligibilities = []
        col_dim = self.input_dim
        for layer in self.layers:
            # input weights
            row_dim = layer
            matrix = np.zeros((col_dim, row_dim))
            eligibilities.append(matrix)

            # bias
            bias = np.zeros(layer)
            eligibilities.append(bias)

            # this layers row dimension is next layers column dimension
            col_dim = row_dim

        self.eligibilities = eligibilities


    def get_target_and_TD_error(self, current_state, next_state, reward):
        target = reward + self.discount_factor * self.find_value(next_state)
        td_error = target - self.find_value(current_state)
        return target, td_error

    # runs state through network and returns prediction
    def find_value(self, state):
        input_state = convert_string_to_list(state.replace(',', ''))[0]
        input_state = np.array([input_state])
        predictions = self.model(input_state)
        return predictions.numpy()[0][0]


    def update_model_and_eligibilities(self, state, target, td_error):
        features = convert_string_to_list(state.replace(',', ''))[0]
        self.fit(features, target, td_error)  # train model

        # decay eligibilities
        for i in range(len(self.eligibilities)):
            self.eligibilities[i] = self.eligibilities[i] * self.eligibility_decay_rate


    def fit(self, features, target, td_error):
        params = self.model.trainable_weights

        with tf.GradientTape() as tape:
            loss = self.gen_loss(features, target, avg=False)
            gradients = tape.gradient(loss, params)
            gradients_2 = self.modify_gradients(gradients, td_error)
            self.model.optimizer.apply_gradients(zip(gradients_2, params))

    # This returns a tensor of losses, OR the value of the averaged tensor.  Note: use .numpy() to get the
    # value of a tensor.
    def gen_loss(self, features, targets, avg=False):
        features = np.array([features])
        predictions = self.model(features)  # Feed-forward pass to produce outputs/predictions
        loss = self.model.loss(targets, predictions)  # model.loss = the loss function
        return tf.reduce_mean(loss).numpy() if avg else loss

    # update eligibilities and modify gradients
    def modify_gradients(self, gradients, td_error):
        modified_gradients = []
        for i in range(len(gradients)):
            # e_i <-- e_i + dV(s)/dw_i
            self.eligibilities[i] = np.add(self.eligibilities[i], gradients[i])

            # modify gradient w_i = -e_i * TD-error, such that update rule becomes
            # w_i <-- w_i - learning_rate * modfied_gradient_i =
            # w_i <-- w_i + learning rate * TD-error * e_i
            modified_gradients_matrix = self.eligibilities[i] * -td_error
            modified_gradients.append(modified_gradients_matrix)

        return modified_gradients



