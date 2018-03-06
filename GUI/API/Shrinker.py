
# TODO: Might want to randomize/shuffle data.
"""
Class containing functions to shrink data.
"""
class Shrinker:

    """
    Shrink data.
    """
    @staticmethod
    def shrink_data(data, percent):
        return data[:int(len(data) - percent * len(data))]

    """
    Shrink data. 
    """
    @staticmethod
    def shrink_data_with_examples(data, percent):
        return [x[:int(len(x) - percent * len(x))] for x in data]