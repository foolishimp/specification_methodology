import unittest
from subject import positive_square_total


class PureHelperTests(unittest.TestCase):
    def test_empty(self) -> None:
        self.assertEqual(positive_square_total(()), 0)

    def test_nonpositive(self) -> None:
        self.assertEqual(positive_square_total((-8, -1, 0)), 0)

    def test_mixed_and_repeated(self) -> None:
        self.assertEqual(positive_square_total((-3, 0, 2, 2, 5)), 33)

    def test_large_integer(self) -> None:
        value = 10 ** 80
        self.assertEqual(positive_square_total((value, -value, 1)), value * value + 1)


if __name__ == "__main__":
    unittest.main()
