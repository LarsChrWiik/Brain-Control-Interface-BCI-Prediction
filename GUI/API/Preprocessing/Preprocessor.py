
from sklearn.preprocessing import MinMaxScaler

from API.Filter import Filter
from API.Preprocessing.Chunker import Chucker
from API.Preprocessing.Formater import Formater
from API.Preprocessing.Balancer import Balancer
from API.Shrinker import Shrinker
from API.Preprocessing.PLI import PLI
from API.Statistics.PreprocessStatistics import PreprocessStatistics

"""
This class contain the logic behind the pre-processing step of BCI. 
"""
class Preprocessor:

    preprocess_statistics = PreprocessStatistics()
    """
    Pre-process raw data.
    Usable for both labelled and non-labelled data.

    X = Input.
    Y = Targets.
    """
    def preprocess(
            self,
            data_raw,
            with_targets=True,
            shrink_percent=0,
            should_balance=True,
            verbose=False
    ):
        if verbose: print("Started pre-processing")

        if verbose: print("Started Filtering")

        # Filter the input data.
        data_filtered = Filter.filter(data_raw)

        if verbose: print("Started Chunking")

        # Chunk the filtered data.
        X_chunked, Y_chunked = Chucker.chunk_train(data_filtered)

        if verbose: print("Started Shrinking")

        # Shrink the data by a given percent.
        X = Shrinker.shrink_data_with_examples(X_chunked, shrink_percent)
        Y = Shrinker.shrink_data_with_examples(Y_chunked, shrink_percent)

        if verbose: print("Started Balancing")

        # Balance the data according to targets (0 or 1).
        if with_targets and should_balance:
            X, Y = Balancer.balance_equal_with_examples(X, Y)

        if verbose: print("Started Metrics")

        # Applying metric (Phase)
        #X = Phase.apply(X)

        # Applying metric (PLV)
        #X = PLV.apply(X)

        # Applying metric (PLI)
        X = PLI.apply(X)

        if verbose: print("Started Formating")

        # Format the data into a usable format for classifiers.
        X, Y = Formater.format(X, Y)

        if verbose: print("Started MinMaxScaler")

        # Normalize the data. (Between 0 and 1)
        scaler = MinMaxScaler()
        scaler.fit(X)
        X = scaler.transform(X)

        self.preprocess_statistics.fill(
            raw_data=data_raw,
            filtered_data = data_filtered,
            chunked_X = X_chunked,
            chunked_Y = Y_chunked
        )

        if with_targets:
            return X, Y
        return X

    """
    Clear saved statistics. 
    """
    def clear_statistics(self):
        self.preprocess_statistics.clear_statistics()
