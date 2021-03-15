import unittest
import hw5_cards
import hw5_cards_ec2
import copy


class TestHandDeck(unittest.TestCase):
    def test_remove_pairs(self):
        c1 = hw5_cards.Card(0, 2)
        c2 = hw5_cards.Card(1, 1)
        base_cards = [c1, c2]

        # no pairs in hand
        hand = hw5_cards_ec2.Hand(base_cards)
        num_before = len(hand.cards)
        hand.remove_pairs()
        self.assertEqual(len(hand.cards), num_before)

        # 2 of a kind
        pair = [hw5_cards.Card(i, 10) for i in range(2)]
        hand = hw5_cards_ec2.Hand(base_cards + pair)
        num_before = len(hand.cards)
        hand.remove_pairs()
        self.assertEqual(len(hand.cards), num_before - 2)

        # 3 of a kind
        pair = [hw5_cards.Card(i, 10) for i in range(3)]
        hand = hw5_cards_ec2.Hand(base_cards + pair)
        num_before = len(hand.cards)
        hand.remove_pairs()
        self.assertEqual(len(hand.cards), num_before - 2)

        # 4 of a kind
        pair = [hw5_cards.Card(i, 10) for i in range(4)]
        hand = hw5_cards_ec2.Hand(base_cards + pair)
        num_before = len(hand.cards)
        hand.remove_pairs()
        self.assertEqual(len(hand.cards), num_before - 4)

        # 2 kinds of cards with pairs
        pair1 = [hw5_cards.Card(i, 10) for i in range(2)]
        pair2 = [hw5_cards.Card(i, 12) for i in range(3)]
        hand = hw5_cards_ec2.Hand(base_cards + pair1 + pair2)
        num_before = len(hand.cards)
        hand.remove_pairs()
        self.assertEqual(len(hand.cards), num_before - 4)

    def test_deal(self):
        deck = hw5_cards_ec2.Deck()

        # test deal 5 cards to 3 hand
        dealed_cards = deck.cards[-15:]
        hands = deck.deal(3, 5)
        idx = -1
        self.assertEqual(len(hands), 3)
        for h in hands:
            self.assertEqual(len(h.cards), 5)
            for c in h.cards:
                self.assertEqual(str(c), str(dealed_cards[idx]))
                idx -= 1

        # test deal all cards to 5 hand
        deck = hw5_cards_ec2.Deck()
        dealed_cards = copy.copy(deck.cards)
        hands = deck.deal(5, -1)
        # should be [11,11,10,10,10]
        hand_size = [11, 11, 10, 10, 10]
        idx = -1
        self.assertEqual(len(hands), 5)
        for h, sz in zip(hands, hand_size):
            self.assertEqual(len(h.cards), sz)
            for c in h.cards:
                self.assertEqual(str(c), str(dealed_cards[idx]))
                idx -= 1


if __name__ == "__main__":
    unittest.main()
