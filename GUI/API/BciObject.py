
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
        data_chunked, targets = Chucker.chunk_train(data_raw)

        # Flatten
        X = []
        Y = []
        for i in range(len(data_chunked)):
            example = data_chunked[i]
            for j in range(len(example)):
                chunk = example[j]
                for k in range(len(chunk)):
                    sensor = chunk[k]
                    # Appending.
                    X.append(sensor)
                    Y.append(targets[i][j])

        # Preprocess the data.

        print("len X = " + str(len(X)))
        print("len Y = " + str(len(Y)))

        # Train the classifier.
        self.prediction_model.train(X, Y)


        print("Implementation not finished")

    def predict(self):
        print("Not implemented")