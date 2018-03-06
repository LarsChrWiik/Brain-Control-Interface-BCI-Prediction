
# TODO: Might want to shuffle chunks the selection of examples.
"""
Class containing logic for balancing data according to targets.
"""
class Balancer:

    """
    Balance chunked data equally according to targets.
    NB: This will remove information if the data originally was unballanced.
    """
    @staticmethod
    def balance_equal_with_examples(X, Y):

        # Find the minimum target count.
        y_0 = 0
        y_1 = 0
        for example in Y:
            y_0 += len([x for x in example if x == 0])
            y_1 += len([x for x in example if x == 1])
        min_size = min(y_0, y_1)

        """
        Add examples for each targets untill the minimum is reached.
        This will ballance the target output ratio. 
        """
        X_new = []
        x_counter = 0
        Y_new = []
        y_counter = 0
        for i in range(len(Y)):
            X_example = []
            Y_example = []
            for j in range(len(Y[0])):
                if Y[i][j] == 0 and x_counter < min_size:
                    X_example.append(X[i][j])
                    Y_example.append(Y[i][j])
                    x_counter += 1
                elif Y[i][j] == 1 and y_counter < min_size:
                    X_example.append(X[i][j])
                    Y_example.append(Y[i][j])
                    y_counter += 1
            X_new.append(X_example)
            Y_new.append(Y_example)

        return X_new, Y_new

    # TODO: Remove at the end when we know it is not needed.
    """
    @staticmethod
    def balance_equal(X, Y):
        y_0 = [x for x in Y if x == 0]
        y_1 = [x for x in Y if x == 1]

        min_size = min(len(y_0), len(y_1))

        X_new = []
        x_counter = 0
        Y_new = []
        y_counter = 0
        for i in range(len(X)):
            if Y[i] == 0 and x_counter < min_size:
                X_new.append(X[i])
                Y_new.append(Y[i])
                x_counter += 1
            elif Y[i] == 1 and y_counter < min_size:
                X_new.append(X[i])
                Y_new.append(Y[i])
                y_counter += 1

        return X_new, Y_new
    """