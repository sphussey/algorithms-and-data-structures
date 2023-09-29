# Creator - Shane Hussey Ds5010spring2023

class Perceptron:
    """
    A perceptron is a simple supervised learning algorithm
    that performs binary classification and is the basis
    for neural networks, serving as an artificial neuron.
    """

    def __init__(self, weights=None):
        """Initialize the perceptron with given weights (default is None)"""
        self.weights = weights

    def _set_autoweights(self, length):
        self.weights = [0 for l in range(length)]

    # Problem 1

    def predict1(self, x):
        """
        Predict a single input/output from the perceptron model.
        param x: A list or tuple giving the input vector
        returns: The predicted output (0 or 1), or None if not trained yet
        """

        if self.weights is not None:
            activation = 0
            input = [1] + list(x)
            for pair in list(zip(input, self.weights)):
                activation += pair[0] * pair[1]
            if activation < 0:
                return 0
            else:
                return 1
        else:
            print("model has not been trained yet")



    # Problem 2

    def predict(self, X):
        """
        Predict a list of input/outputs from the perceptron model.
        param X: An iterable containing lists/tuples of input vectors
        returns: A list containing the predicted outputs (each 0 or 1)
        """

        prediction = []
        for i in X:
            prediction.append(self.predict1(i))
        return prediction


    # Problem 3

    def update(self, x, y):
        """
        Updates the perceptron weights from a single sample input/output pair.
        param x: A list or tuple giving the input vector
        param y: The observed output (0 or 1)
        returns: None
        """
        # initialize list of zeros if None of length len(Y)
        if self.weights is None:
            self._set_autoweights(len(x)+1)
        # create empty variable to store new weights
        new_weights = []
        # append 1 to the beginning of x and ensure the type is list
        input = [1] + list(x)
        # merge the two lists into a 2-d nested list [[weights[0], x[0]], [weights[i], x[i]]
        merged_xy = list(zip(self.weights,input))
        y_pred = self.predict1(x)
        for i in range(len(self.weights)):
            # w(i,new) = w(i,old) + (y − ypred) xi
            new_weights.append(self.weights[i] + (y - y_pred) * input[i])
        self.weights = new_weights



    # Problem 4

    def fit(self, X, Y, num_iter=100):
        """
        Updates the perceptron weights from a list of sample input/output pairs.
        param X: An iterable containing lists/tuples of input vectors
        param Y: An iterable containing the observed outputs (each 0 or 1)
        param num_iter: The number of training iterations over all samples
        returns: None
        """


        # perform update to weights num_iter times
        for iter in range(num_iter):
            # loop through all sample input/output pairs and perform a training update for each pair
            for i in range(len(Y)):
                self.update(X[i], Y[i])



    # Problem 5

    def score(self, X, Y):
        """
        Calculates the prediction accuracy for a list of sample input/output pairs.
        param X: An iterable containing lists/tuples of input vectors
        param Y: An iterable containing the observed outputs (each 0 or 1)
        returns: The predictive accuracy (proportion of correct predictions)
        """

        prediction  = self.predict(X)
        correct = 0
        for pair in list(zip(prediction,Y)):
            if pair[0] is pair[1]:
                correct += 1
        return correct / len(Y)


