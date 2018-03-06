
import random


"""
Class containing logic for randomizing. 
"""
class Randomizer:

    @staticmethod
    def shuffle_two_lists(list1, list2):
        z = list(zip(list1, list2))
        random.shuffle(z)
        a, b = zip(*z)
        return a, b
