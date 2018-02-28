
class Balancer:

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
                x_counter += 1
            elif Y[i] == 1 and y_counter < min_size:
                Y_new.append(Y[i])
                y_counter += 1

        return X_new, Y_new