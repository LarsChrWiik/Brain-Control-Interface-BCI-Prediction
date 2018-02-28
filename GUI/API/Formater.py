
class Formater:

    """
    Flatten the chunked data.
    Usable for both training and test data, which is chunked.
    """
    @staticmethod
    def format_chunked_data(data_chunked: dict, targets=None):
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
