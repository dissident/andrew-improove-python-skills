from src.learn import cart
import unittest


class LearnArraysTest(unittest.TestCase):
    def test_buy(self):
        cart.buy('apple', 1)
        self.assertEqual(cart.cart, { 'apple': 1 })

    def test_items_list(self):
        result = cart.items_list()
        self.assertEqual(result, "apple: 50$, banana: 75$, bread: 15$, water: 10$\n")

    def test_check(self):
        cart.buy('banana', 2)
        result = cart.check()
        self.assertEqual(result, "banana: 2\n total: 150$\n")

    def test_cancel(self):
        cart.buy('banana', 2)
        cart.cancel('banana', 1)
        self.assertEqual(cart.cart, { 'banana': 1 })
