import numpy as np
import ai


def weight_creator(n_first_layer, n_second_layer):
    weights = []
    for i in range(n_second_layer):
        weights.append([])
        for j in range(n_first_layer + 1):
            weights[i].append(2 * np.random.randint(1, 100) / 100 - 1)

    weight_matrix = np.array(weights)
    return weight_matrix


class Neuralnet:

    def __init__(self, n_input, n_hidden_l, n_hidden_n, n_output):
        self.n_input = n_input
        self.n_hidden_n = n_hidden_n
        self.n_hidden_l = n_hidden_l
        self.n_output = n_output
        self.sigmoid_matrix_h1_i = np.array([])
        self.sigmoid_matrix_o_h1 = np.array([])
        self.weight_h1_i = weight_creator(self.n_input - 1, self.n_hidden_n)
        self.weight_o_hn = weight_creator(self.n_hidden_n, self.n_output)

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    def sigmoid_creator(self, weight_matrix, inputs):
        try:
            weighted_sum_array = weight_matrix.dot(inputs)
            c = 0
            for k in weighted_sum_array:
                result = list(map(self.sigmoid, k))
                weighted_sum_array[c] = result
                c += 1

            return weighted_sum_array

        except IndexError:
            print('please input correct number of input')

    def feed_forward(self, input_list):
        input_list = np.array(input_list)
        input_list = np.reshape(np.array(input_list), (len(input_list), 1))
        self.sigmoid_matrix_h1_i = self.sigmoid_creator(self.weight_h1_i, input_list)
        self.sigmoid_matrix_h1_i = np.concatenate((self.sigmoid_matrix_h1_i, np.array([[1]])), axis=0)
        self.sigmoid_matrix_o_h1 = self.sigmoid_creator(self.weight_o_hn, self.sigmoid_matrix_h1_i)
        return self.sigmoid_matrix_o_h1

    @staticmethod
    def weight_corrector(weight_matrix, lr, error_2, output, input1):
        error = np.multiply(error_2, output * np.subtract(1, output))
        delta_weight = lr * error * input1
        weight_matrix = weight_matrix + delta_weight
        return weight_matrix

    def training(self, inputs, targets, lr):
        inputs = np.array(inputs)
        targets = np.reshape(targets, (len(targets), 1))
        self.feed_forward(inputs)
        error_o = targets - self.sigmoid_matrix_o_h1
        error_h1 = np.matmul(self.weight_o_hn.transpose(), error_o)
        self.weight_o_hn = self.weight_corrector(self.weight_o_hn, lr, error_o, self.sigmoid_matrix_o_h1,
                                                 self.sigmoid_matrix_h1_i.reshape((1, len(self.sigmoid_matrix_h1_i))))
        self.sigmoid_matrix_h1_i = np.delete(self.sigmoid_matrix_h1_i, -1, axis=0)
        error_h1 = np.delete(error_h1, -1, axis=0)
        self.weight_h1_i = self.weight_corrector(self.weight_h1_i, lr, error_h1, self.sigmoid_matrix_h1_i,
                                                 inputs.reshape((1, len(inputs))))


neural = Neuralnet(9, 1, 10, 9)

current_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
probabilities = [0, 0, 0, 0, 0, 0, 0, 0, 0]
input1 = []
input2 = []
t = 1
for i in range(20000):
    print('repeated : ', i)
    pos = ai.best_position_selector(current_board, input1, input2, t)
    probabilities[pos] = 1
    if t == 1:
        input1.append(pos)
        t = 2
    else:
        input2.append(pos)
        t = 1
    if ai.game_checker(current_board, input1, input2):
        current_board = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        input1 = []
        input2 = []
        probabilities = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        t = 1
        break
    neural.training(current_board, probabilities, 0.4)
    current_board[pos] = t
    probabilities = [0, 0, 0, 0, 0, 0, 0, 0, 0]

'''training_data = np.array([[[0, 0, 0], [0]],
                          [[1, 0, 0], [0]],
                          [[0, 1, 0], [0]],
                          [[1, 1, 1], [1]]])

for j in range(10000):
    for i in training_data:
        neural.training(i[0], i[1], 0.4)'''

test_data = [[1, 0, 0, 0, 0, 0, 0, 0, 0],
             [1, 0, 2, 0, 0, 0, 0, 0, 0],
             [1, 0, 2, 0, 0, 0, 1, 0, 0],
             [1, 0, 2, 2, 0, 0, 1, 0, 0],
             [1, 0, 2, 2, 0, 0, 1, 0, 1],
             [1, 0, 2, 2, 2, 0, 1, 0, 1]]

for i in test_data:
    print(neural.feed_forward(i))
