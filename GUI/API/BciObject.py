
from API.Filter import Filter
from API.PredictionModel import PredictionModel
from API.Chunker import Chucker
import numpy as np

class BciObject:

    prediction_model = PredictionModel()

    def get_statistics(self):
        print("Not implemented")

    # Under process.
    def train(self, data_raw):

        # TODO: Needs to be re-implemented.
        # Filter the input data.
        #data_filtered = Filter.filter(data_raw)

        # Chunk the filtered data.
        data_chunked, targets = Chucker.chunk_train(data_raw)


        print(data_raw.keys())



        # TODO: just for testing.
        # Preprocess the data (Flatten)
        X = []
        Y = []
        for i in range(len(data_chunked)):
            # Examples
            for j in range(len(data_chunked[i])):
                # Chunks
                for k in range(len(data_chunked[i][j])):
                    # Sensor
                    X.append(data_chunked[i][j][k])
                    Y.append(targets[i][j])

        print(len(X))
        print("len = " + str(len(X[0])) + ": " + str(X[0]) + ", target = " + str(Y[0]))
        print(len(Y))

        # TODO: just for testing.
        # Reduce the size.
        train_size = 2000
        X2 = X[:train_size]
        Y2 = Y[:train_size]
        X3 = X[-train_size:]
        Y3 = Y[-train_size:]

        a = len([x for x in Y3 if x == 0])
        b = len([x for x in Y3 if x == 1])
        print("ratio = " + str(a / (a+b)))
        print("a = " + str(a))
        print("b = " + str(b))

        # Train the classifier.
        self.prediction_model.train(X2, Y2)

        # TODO: just for testing.
        # Calculate score from the classifier.
        s = self.prediction_model.score(X3, Y3)
        print(s)

    def predict(self):
        print("Not implemented")