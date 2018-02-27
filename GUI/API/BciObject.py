
from API.Filter import Filter
from API.PredictionModel import PredictionModel
from API.Chunker import Chucker

class BciObject:

    prediction_model = PredictionModel()

    def get_statistics(self):
        print("Not implemented")

    # Under process.
    def train(self, data_raw):

        # Filter the input data.
        #data_filtered = Filter.filter(data_raw)

        # Chunk the filtered data.
        data_chunked = Chucker.chunk_test(data_raw)

        # Preprocess the data.

        # Train the classifier.

        print("Implementation not finished")

    def predict(self):
        print("Not implemented")