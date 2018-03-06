
from sklearn.preprocessing import MinMaxScaler

from API.Filter import Filter
from API.Chunker import Chucker
from API.Formater import Formater
from API.Balancer import Balancer
from API.Shrinker import Shrinker
from API.PLV import PLV
from API.PLI import PLI
from API.Phase import Phase


class Preprocessor:

    """
    Pre-process raw data.
    Usable for both labelled and non-labelled data.

    X = Input.
    Y = Targets.
    """
    @staticmethod
    def preprocess(
            data_raw,
            with_targets=True,
            shrink_percent=0,
            should_balance=True
    ):
        # Filter the input data.
        data_filtered = Filter.filter(data_raw)

        # Chunk the filtered data.
        X, Y = Chucker.chunk_train(data_filtered)

        # Shrink the data by a given percent.
        X = Shrinker.shrink_data_with_examples(X, shrink_percent)
        Y = Shrinker.shrink_data_with_examples(Y, shrink_percent)

        # Balance the data according to targets (0 or 1).
        if with_targets and should_balance:
            X, Y = Balancer.balance_equal_with_examples(X, Y)

        # Applying metric (Phase)
        #X = Phase.apply(X)

        # Applying metric (PLV)
        #X = PLV.apply(X)

        # Applying metric (PLI)
        X = PLI.apply(X)

        # Format the data into a usable format for classifiers.
        X, Y = Formater.format(X, Y)

        # Normalize the data. (Between 0 and 1)
        scaler = MinMaxScaler()
        scaler.fit(X)
        X = scaler.transform(X)

        if with_targets:
            return X, Y
        return X
