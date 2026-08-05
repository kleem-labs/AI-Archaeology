import math
import unittest

from implementations.from_scratch import (
    add, attend_one, dot, euclidean_distance, feed_forward, gradient_descent,
    layer_norm, matrix_vector, residual, stable_softmax, subtract,
)


class ExcavationTests(unittest.TestCase):
    def test_change_recovers_destination(self):
        start = [2, 3]
        destination = [7, 1]
        self.assertEqual(add(start, subtract(destination, start)), destination)

    def test_distance_prevents_cancellation(self):
        self.assertEqual(euclidean_distance([0, 0], [3, 4]), 5)

    def test_matrix_allows_inputs_to_interact(self):
        self.assertEqual(matrix_vector([[1, 2], [3, 4]], [5, 6]), [17, 39])

    def test_dot_preserves_negative_evidence(self):
        self.assertEqual(dot([1, 1], [-1, -1]), -2)

    def test_softmax_is_stable_and_normalized(self):
        weights = stable_softmax([1000, 1001, 1002])
        self.assertAlmostEqual(sum(weights), 1)
        self.assertLess(weights[0], weights[1])
        self.assertLess(weights[1], weights[2])

    def test_attention_returns_weights_and_content(self):
        output, weights = attend_one([1, 0], [[1, 0], [0, 1]], [[10, 0], [0, 10]])
        self.assertAlmostEqual(sum(weights), 1)
        self.assertGreater(output[0], output[1])

    def test_gate_makes_stacked_transformations_nonlinear(self):
        expand = [[1, 0], [-1, 0]]
        contract = [[1, -1]]
        self.assertEqual(feed_forward([2, 0], expand, contract), [2])
        self.assertEqual(feed_forward([-2, 0], expand, contract), [-2])

    def test_residual_can_leave_state_unchanged(self):
        self.assertEqual(residual([4, 5], [0, 0]), [4, 5])

    def test_layer_norm_recenters_and_rescales(self):
        normalized = layer_norm([1, 2, 3])
        self.assertAlmostEqual(sum(normalized) / len(normalized), 0)
        variance = sum(value * value for value in normalized) / len(normalized)
        self.assertTrue(math.isclose(variance, 1, rel_tol=2e-5))

    def test_gradient_descent_moves_toward_minimum(self):
        path = gradient_descent(8, lambda x: 2 * (x - 3), 0.2, 8)
        self.assertLess(abs(path[-1] - 3), abs(path[0] - 3))

    def test_mismatched_features_are_rejected(self):
        with self.assertRaises(ValueError):
            dot([1, 2], [1])


if __name__ == "__main__":
    unittest.main()
