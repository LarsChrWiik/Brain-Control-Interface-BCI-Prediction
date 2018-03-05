
from API.Filter import Filter
from API.Chunker import Chucker
from API.Formater import Formater
from API.Balancer import Balancer
from API.PLV import PLV
from API.PLI import PLI
from API.Phase import Phase
from sklearn.preprocessing import MinMaxScaler

class Preprocessor:

    @staticmethod
    def preprocess(data_raw, with_targets=True, shrink_percent=0):

        # TODO: Needs to be re-implemented. (DICT not np.array)
        # Filter the input data.
        data_filtered = Filter.filter(data_raw)

        # TODO: Use data_filtered when filter is working.
        # Chunk the filtered data.
        X, Y = Chucker.chunk_train(data_filtered)

        # Shrink the data size.
        X = Preprocessor.shrink_data_2(X, shrink_percent)
        Y = Preprocessor.shrink_data_2(Y, shrink_percent)

        # Balance the data.
        X, Y = Balancer.balance_equal_2(X, Y)

        # Applying metric (Phase)
        #X = Phase.apply(X)

        # Applying metric (PLV)
        #X = PLV.apply(X)

        # Applying metric (PLI)
        X = PLI.apply(X)

        # Format the chunked data.
        X, Y = Formater.format(X, Y)

        # Normalization between 0 and 1.
        scaler = MinMaxScaler()
        scaler.fit(X)
        X = scaler.transform(X)

        # Returns
        if not with_targets:
            return X
        return X, Y

    """
    Shrink data. 
    """
    @staticmethod
    def shrink_data(data, percent):
        return data[:int(len(data) - percent * len(data))]

    """
    Shrink data. 
    """
    @staticmethod
    def shrink_data_2(data, percent):
        return [x[:int(len(x) - percent * len(x))] for x in data]



