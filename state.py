import random
import unittest
from collections import defaultdict


class State:
    def __init__(self):
        # state (str) -> weight (int)
        self.choices = defaultdict(int)

    def addTransition(self, next):
        self.choices[next] += 1

    # http://stackoverflow.com/a/3679747
    def next(self):
        total = sum(self.choices.values())
        randNum = random.uniform(0, total)
        upto = 0
        for state, weight in self.choices.items():
            if upto + weight >= randNum:
                return state
            upto += weight
        assert False, "Shouldn't get here"


class UnitTest(unittest.TestCase):
    def test(self):
        # This is...
        test1 = State()
        test1.addTransition("a test")
        self.assertEqual(test1.next(), "a test")

        for i in range(499):
            test1.addTransition("a test")
        for i in range(250):
            test1.addTransition("not a test")
            test1.addTransition("something else")

        results = defaultdict(int)
        for i in range(1000):
            results[test1.next()] += 1

        self.assertAlmostEqual(results["a test"] / 1000, 0.5, 1)
        self.assertAlmostEqual(results["not a test"] / 1000, 0.25, 1)
        self.assertAlmostEqual(results["something else"] / 1000, 0.25, 1)
        self.assertEqual(len(results), 3)
