
import random


"""
Class containing logic for randomizing. 
"""
class Randomizer:

    @staticmethod
    def shuffle_two_lists(list1, list2):
        combined = list(zip(list1, list2))
        random.shuffle(combined)
        list1[:], list2[:] = zip(*combined)
        return list1, list2
