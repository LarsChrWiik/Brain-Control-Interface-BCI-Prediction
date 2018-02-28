
from API.Filter import Filter
from API.Chunker import Chucker
from API.Formater import Formater

class Preprocessor:

    @staticmethod
    def preprocess(data_raw, with_targets=True):

        # TODO: Needs to be re-implemented. (DICT not np.array)
        # Filter the input data.
        # data_filtered = Filter.filter(data_raw)

        # TODO: Use data_filtered when filter is working.
        # Chunk the filtered data.
        data_chunked, targets = Chucker.chunk_train(data_raw)

        # Format the chunked data.
        X, Y = Formater.format_chunked_data(data_chunked, targets)

        # Returns
        if not with_targets:
            return X
        return X, Y



