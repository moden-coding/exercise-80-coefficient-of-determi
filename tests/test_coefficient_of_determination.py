#!/usr/bin/env python3

import unittest

from src.coefficient_of_determination import coefficient_of_determination


class TestCoefficientOfDetermination(unittest.TestCase):

    def test_all_features(self):
        scores = coefficient_of_determination()
        self.assertAlmostEqual(
            scores[0], 1.0,
            msg="With all five features X1-X5 in the model, the R2 score "
                "against the training data should be (essentially) 1.0. "
                "Got %r." % (scores[0],))

    def test_individual_features(self):
        scores = coefficient_of_determination()

        sums = [0.0258828579115, 0.0968186306153, 0.0881564161891,
                0.868276772892]
        for i in range(1, 5):
            self.assertAlmostEqual(
                sums[i - 1], sum(scores[i:i + 2]),
                msg="The R2 scores for the single-feature models "
                    "(scores[%d] and scores[%d]) don't sum to the expected "
                    "value %r. Got %r." % (i, i + 1, sums[i - 1],
                                            sum(scores[i:i + 2])))


if __name__ == '__main__':
    unittest.main()
