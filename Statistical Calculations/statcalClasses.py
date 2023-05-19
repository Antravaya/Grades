#statcalClasses.py

from statistics import mean, median, stdev

class StatSet:
    def __init__(self):
        self.statSet = []

    def addNumber(self, x):
        self.statSet.append(x)

    def mean(self):
        return mean(self.statSet)

    def median(self):
        return median(self.statSet)

    def stdDev(self):
        return stdev(self.statSet)

    def count(self):
        return len(self.statSet)

    def min(self):
        return min(self.statSet)

    def max(self):
        return max(self.statSet)
