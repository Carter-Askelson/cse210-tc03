import unittest
from deal import *


class Test(unittest.TestCase):

    def test_get_card(self):
        deal = Deal()
        deal.current_card = 2
        self.assertEqual(deal.current_card, 2)

    def test_get_next_card(self):
        deal = Deal()
        deal.next_card = 4
        self.assertEqual(deal.next_card, 4)

    def test_deal_card(self):
        deal = Deal()

        self.assertEqual(deal.shuffle_deck(), deal.get_card())

    def test_shuffle_deck(self):
        deal = Deal()
        deal.shuffle_deck()
        sequential_deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]

        # check to make sure deck gets initialized when called
        self.assertIsNot(None, deal.deck)

        # check to make sure deck max and min numbers are in range of 1-13
        self.assertEqual(max(deal.deck), 13)
        self.assertEqual(min(deal.deck), 1)

        # check to make sure deck is random and not in sequential order
        self.assertIsNot(sequential_deck, deal.deck)

if __name__ == '__main__':
    unittest.main()
