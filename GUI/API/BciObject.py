
from API.Filter import Filter
from API.PredictionModel import PredictionModel

class BciObject:

    prediction_model = PredictionModel()

    def get_statistics(self):
        print("Not implemented")

    def train(self, data_raw):
        data_filtered = Filter.filter(data_raw)

        # Send to model.
        print("Not implemented")

    def predict():
        print("Not implemented")