
from API.Randomizer import Randomizer

class PreprocessStatistics:

    raw_signal = None
    filtered_signal = None
    chunked_X = None
    chunked_Y = None

    number_of_chunks = 10

    def fill(self, raw_data, filtered_data, chunked_X, chunked_Y):
        # Choosing statistics.

        # RAW_DATA
        self.raw_signal = raw_data["Signal"]
        self.filtered_signal = filtered_data["Signal"]

        # Randomize
        chunked_X, chunked_Y = Randomizer.shuffle_two_lists(chunked_X[0], chunked_Y[0])
        self.chunked_X = chunked_X[:self.number_of_chunks]
        self.chunked_Y = chunked_Y[:self.number_of_chunks]

    def clear_statistics(self):
        self.raw_signal = None
        self.filtered_signal = None
        self.chunked_X = None
        self.chunked_Y = None
