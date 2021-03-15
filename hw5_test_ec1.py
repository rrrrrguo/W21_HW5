import unittest
import hw5_cards
import hw5_cards_ec1


class TestHand(unittest.TestCase):

    def test_construct_hand(self):
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)

        hand = hw5_cards_ec1.Hand([c1, c2])

        self.assertEqual(len(hand.cards), 2)

        self.assertEqual(hand.cards[0].suit, 0)
        self.assertEqual(hand.cards[0].suit_name, "Diamonds")
        self.assertEqual(hand.cards[0].rank, 2)
        self.assertEqual(hand.cards[0].rank_name, "2")

        self.assertIsInstance(hand.cards[0].suit, int)
        self.assertIsInstance(hand.cards[0].suit_name, str)
        self.assertIsInstance(hand.cards[0].rank, int)
        self.assertIsInstance(hand.cards[0].rank_name, str)

        self.assertEqual(hand.cards[1].suit, 1)
        self.assertEqual(hand.cards[1].suit_name, "Clubs")
        self.assertEqual(hand.cards[1].rank, 1)
        self.assertEqual(hand.cards[1].rank_name, "Ace")

    def test_add_and_remove(self):
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)
        c3 = hw5_cards.Card(2, 10)
        c4 = hw5_cards.Card(3, 6)
        c5 = hw5_cards.Card(1, 8)
        hand = hw5_cards_ec1.Hand([c1, c2, c3, c4])

        # add card not in the hand
        hand.add_card(c5)
        self.assertEqual(len(hand.cards), 5)
        # add a card in the hand
        hand.add_card(c1)
        self.assertEqual(len(hand.cards), 5)
        # remove a card in the hand
        removed = hand.remove_card(c1)
        self.assertEqual(len(hand.cards), 4)
        self.assertEqual(str(removed), str(c1))
        # remove a card not in the hand
        removed = hand.remove_card(c1)
        self.assertEqual(len(hand.cards), 4)
        self.assertIsNone(removed)

    def test_draw(self):
        deck = hw5_cards.Deck()
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)
        hand = hw5_cards_ec1.Hand([c1, c2])
        num_card = len(deck.cards)
        hand.draw(deck)
        # number of cards in hand is increased
        self.assertEqual(len(hand.cards), 3)
        # number of cards in deck is decreased
        self.assertEqual(len(deck.cards), num_card - 1)


if __name__ == "__main__":
    unittest.main()
