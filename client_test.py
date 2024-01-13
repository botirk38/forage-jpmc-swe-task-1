import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """
        for quote in quotes:
            data_point = getDataPoint(quote)
            self.assertEqual(
                data_point[3], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
                'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        """ ------------ Add the assertion below ------------ """

        for quote in quotes:
            data_point = getDataPoint(quote)
            self.assertEqual(
                data_point[3], (quote['top_bid']['price'] + quote['top_ask']['price']) / 2)

    """ ------------ Add more unit tests ------------ """

    def test_getRatio_basic(self):
        price_a = 200.0
        price_b = 100.0
        self.assertEqual(getRatio(price_a, price_b), 2.0)

    def test_getRatio_zeroDenominator(self):
        price_a = 150.0
        price_b = 0.0
        self.assertIsNone(getRatio(price_a, price_b))

    def test_getRatio_zeroNumerator(self):
        price_a = 0.0
        price_b = 150.0
        self.assertEqual(getRatio(price_a, price_b), 0.0)

    def test_getRatio_negativePrice(self):
        price_a = -100.0
        price_b = 200.0
        self.assertEqual(getRatio(price_a, price_b), -0.5)


if __name__ == '__main__':
    unittest.main()
