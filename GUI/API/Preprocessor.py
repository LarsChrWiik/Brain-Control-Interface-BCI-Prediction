
from API.Filter import Filter
from API.Chunker import Chucker
from API.Formater import Formater
from API.Balancer import Balancer

class Preprocessor:

    @staticmethod
    def preprocess(data_raw, with_targets=True, shrink_percent=0):

        # TODO: Needs to be re-implemented. (DICT not np.array)
        # Filter the input data.
        data_filtered = Filter.filter(data_raw)

        # TODO: Use data_filtered when filter is working.
        # Chunk the filtered data.
        data_chunked, targets = Chucker.chunk_train(data_raw)

        # Format the chunked data.
        X, Y = Formater.format_chunked_data(data_chunked, targets)

        # Shrink the data size.
        X = Preprocessor.shrink_data(X, shrink_percent)
        Y = Preprocessor.shrink_data(Y, shrink_percent)

        # Balance the data.
        X, Y = Balancer.balance_equal(X, Y)

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



