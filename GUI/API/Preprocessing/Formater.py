
class Formater:

    """
    Flatten the chunked data.
    Usable for both training and test data, which is chunked.
    """
    @staticmethod
    def format_chunked_data(data_chunked, targets=None):
        X = []
        Y = []
        for i in range(len(data_chunked)):
            # Examples
            for j in range(len(data_chunked[i])):
                # Chunks
                for k in range(len(data_chunked[i][j])):
                    # Sensor
                    X.append(data_chunked[i][j][k])
                    if targets is not None:
                        Y.append(targets[i][j])
        if targets is None:
            return X
        return X, Y

    """
    Flatten the data.
    Usable for both training and test data.
    """
    @staticmethod
    def format(X, Y, with_targets):

        X_new = []
        Y_new = []
        for i in range(len(X)):
            # Examples
            for j in range(len(X[i])):
                # Chunks
                for k in range(len(X[i][j])):
                    # Sensor
                    X_new.append(X[i][j][k])
                    if with_targets:
                        Y_new.append(Y[i][j])
        if Y is None:
            return X_new
        return X_new, Y_new

