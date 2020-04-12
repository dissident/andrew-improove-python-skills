from src.learn import arrays
import unittest


class LearnArraysTest(unittest.TestCase):
    def test_add(self):
        array = [1, 2, 3, 4, 5]
        new_item = 6
        self.assertEqual(arrays.add(array, new_item), [1, 2, 3, 4, 5, 6])

    def test_reverse(self):
        array = [1, 2, 3, 4, 5]
        self.assertEqual(arrays.reverse(array), [5, 4, 3, 2, 1])

    def test_five_index(self):
        array = [1, 2, 3, 4, 5]
        new_array = [5, 3, 8, 5, 7, 12]
        self.assertEqual(arrays.five_index(array), 4)
        self.assertEqual(arrays.five_index(new_array), 0)

    def test_add_before_second(self):
        array = [1, 2, 3, 4, 5]
        new_item = 43
        self.assertEqual(arrays.add_before_second(array, new_item), [1, 43, 2, 3, 4, 5])

    def test_remove_duplicates(self):
        array = [1, 2, 2, 3, 4, 5, 2, 1, 6, 7, 88, 8, 2]
        self.assertEqual(arrays.remove_duplicates(array), [1, 2, 3, 4, 5, 6, 7, 88, 8])

