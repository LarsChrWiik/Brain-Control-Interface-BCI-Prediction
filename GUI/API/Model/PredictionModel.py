from sklearn.model_selection import train_test_split


from API.Statistics.PredictionModelStatistics import PredictionModelStatistics


class PredictionModel:

    def __init__(self):
        self.model_statistics = PredictionModelStatistics()

    def train(self, classifiers, X, Y, test_size=0.3):
        predictions = []
        # Divide into training and test set.
        training_input, testing_input, training_target, testing_target = train_test_split(
            X,
            Y,
            test_size=test_size
        )
        i = 0
        # Train
        while(i < len(classifiers)):
            classifiers[i].fit(training_input, training_target)
            i+=1

        i = 0
        # Test
        while(i < len(classifiers)):
            predictions.append(classifiers[i].predict(testing_input))
            i+=1
        # Combine
        prediction_final = self.combine(predictions)
        # Add statistics
        self.model_statistics.fill(testing_target, prediction_final)

    def predict(self, classifiers, X):
        predictions = []
        i = 0
        while(i < len(classifiers)):
           predictions.append(classifiers[i].predict(X))
           i+=1
        return self.combine(predictions)


    def combine(self, predictions):
        ans = []
        i = 0
        j = 0
        zero = 0
        one = 0
        while(j < len(predictions[i])):
            while (i < len(predictions)):
               if(predictions[i][j] == 0):
                   zero +=1
               else:
                   one += 1
               i += 1
            if(zero > one):
                ans.append(0.0)
            else:
                ans.append(1.0)
            i = 0
            j+=1
        return ans