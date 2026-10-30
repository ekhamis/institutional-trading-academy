"""Regression checks for the synthetic review-case arithmetic."""
import unittest

class ReviewArithmetic(unittest.TestCase):
    def test_weighted_exit(self):
        self.assertAlmostEqual(.5 * 1 + .5 * 3 - .12, 1.88)

    def test_breakeven_cost(self):
        self.assertAlmostEqual((99.8 - 100) * 50 - 5, -15)

    def test_expectancy(self):
        self.assertAlmostEqual((4 * 2 - 6 - 1) / 10, .1)

    def test_drawdown_recovery(self):
        self.assertAlmostEqual((12000 - 9000) / 12000, .25)
        self.assertAlmostEqual(12000 / 9000 - 1, 1 / 3)

    def test_compounded_losses(self):
        self.assertAlmostEqual(10000 * .99 ** 5, 9509.900499)

if __name__ == '__main__':
    unittest.main()
