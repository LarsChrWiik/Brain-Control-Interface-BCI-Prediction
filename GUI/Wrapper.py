
from API.BciObject import BciObject

"""
This class is used as wrapper/bridge between the GUI and the API.
The wrapper only contain 1 instance of a BCI-object. 
"""
class Wrapper:

    bciObject = BciObject()

    # TODO: FOR DEVELOPMENT:
    def compare_models(self, data_raw, verbose=False):
        return self.bciObject.compare_models(
            data_raw,
            verbose=verbose
        )

    def train(self, data_raw, with_targets=True, shrink_percent=0, should_balance=True, verbose=False):
        self.bciObject.train(
            data_raw=data_raw,
            with_targets=with_targets,
            shrink_percent=shrink_percent,
            should_balance=should_balance,
            verbose=verbose
        )

        statistics = self.bciObject.preprocessor.preprocess_statistics.raw_signal

        print(statistics)


    def predict(self, data_raw):
        return self.bciObject.predict(data_raw)
