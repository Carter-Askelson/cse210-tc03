from ..deal import *


class TestDeal:

    def test_get_card(self):
        deal = Deal()
        deal.current_card = 2
        assert deal.get_card() == 2

    def test_get_next_card(self):
        deal = Deal()
        deal.next_card = 4
        assert deal.get_next_card() == 4

    def test_deal_card(self):
        deal = Deal()
        expected_current_card = deal.deal_card()
        assert deal.get_card() == expected_current_card

    def test_shuffle_deck(self):
        deal = Deal()
        deal.shuffle_deck()
        sequential_deck = [1,2,3,4,5,6,7,8,9,10,11,12,13]

        # check to make sure deck gets initialized when called
        assert deal.deck is not None

        # check to make sure deck max and min numbers are in range of 1-13
        assert max(deal.deck) == 13
        assert min(deal.deck) == 1

        # check to make sure deck is random and not in sequential order
        assert deal.deck is not sequential_deck
