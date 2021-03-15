from hw5_cards import Card


# create the Hand with an initial set of cards
class Hand:
    '''a hand for playing card 

    Class Attributes
    ---------------- 
    None 

    Instance Attributes
    ------------------- 
    init_card: list
        a list of cards

    '''

    def __init__(self, init_cards):
        self.cards = init_cards

    def add_card(self, card):
        '''add a card 
        add a card to the hand 
        silently fails if the card is already in the hand 
        
        Parameters 
        ------------------- 
        card: instance a card to add 
        Returns
        ------- 
        None
        
        '''
        card_strs = []  # forming an empty list
        for c in self.cards:  # each card in self.cards (the initial list)
            card_strs.append(c.__str__())  # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs:  # if the string representing this card is not in the list already
            self.cards.append(card)  # append it to the list

    def remove_card(self, card):
        '''remove a card from the hand 

        Parameters 
        ------------------- 
        card: instance 
            a card to remove
        Returns
        ------- 
        the card, or None if the card was not in the Hand

        '''
        card_str = str(card)
        for i, c in enumerate(self.cards):
            if card_str == str(c):
                return self.cards.pop(i)
        return None

    def draw(self, deck):
        '''draw a card 
        draw a card from a deck and add it to the hand 
        side effect: the deck will be depleted by one card 
        
        Parameters 
        ------------------- 
        deck: instance 
            a deck from which to draw 
        Returns
        ------- 
        None

        '''
        card = deck.deal_card()
        self.cards.append(card)

    def remove_pairs(self):
        '''remove pairs in hand
        find pairs of cards in a hand and removes them
        if there are 4 cards, remove all of them
        if there are 3 cards, remove any two of them

        Parameters 
        ------------------- 
        None

        Returns
        ------- 
        None

        '''
        existing_faces = dict()
        for c in self.cards:
            if c.rank not in existing_faces:
                existing_faces[c.rank] = [c]
            else:
                existing_faces[c.rank].append(c)
        for f in existing_faces:
            if len(existing_faces[f]) == 4:
                self.remove_card(existing_faces[f][0])
                self.remove_card(existing_faces[f][1])
                self.remove_card(existing_faces[f][2])
                self.remove_card(existing_faces[f][3])
            elif len(existing_faces[f]) >= 2:
                self.remove_card(existing_faces[f][0])
                self.remove_card(existing_faces[f][1])


class Deck:
    '''a deck of Cards
    Instance Attributes
    -------------------
    cards: list
        the list of Cards currently in the Deck. Initialized to contain
        all 52 cards in a standard deck
    '''

    def __init__(self):

        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)  # appends in a sorted order

    def deal_card(self, i=-1):
        '''remove a card from the Deck
        Parameters  
        -------------------
        i: int (optional)
            the index of the ard to remove. Default (-1) will remove the "top" card
        Returns
        -------
        Card
            the Card that was removed
        '''
        return self.cards.pop(i)

    def shuffle(self):
        '''shuffles (randomizes the order) of the Cards
        self.cards is modified in place
        Parameters  
        ----------
        None
        Returns
        -------
        None
        '''
        random.shuffle(self.cards)

    def replace_card(self, card):
        card_strs = []  # forming an empty list
        for c in self.cards:  # each card in self.cards (the initial list)
            card_strs.append(c.__str__())  # appends the string that represents that card to the empty list
        if card.__str__() not in card_strs:  # if the string representing this card is not in the list already
            self.cards.append(card)  # append it to the list

    def sort_cards(self):
        '''returns the Deck to its original order
        
        Cards will be in the same order as when Deck was constructed.
        self.cards is modified in place.
        Parameters  
        ----------
        None
        Returns
        -------
        None
        '''
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)

    def deal_hand(self, hand_size):
        '''removes and returns hand_size cards from the Deck
        
        self.cards is modified in place. Deck size will be reduced
        by hand_size
        Parameters  
        -------------------
        hand_size: int
            the number of cards to deal
        Returns
        -------
        list
            the top hand_size cards from the Deck

        '''
        hand_cards = []
        for i in range(hand_size):
            hand_cards.append(self.deal_card())
        return hand_cards

    def deal(self, num_hand, card_per_hand=-1):
        '''deal the cards
        The deck will deal the cards according to number of hands
        and number of card per hand.
        Parameters  
        -------------------
        num_hand: int
            the number of hands to deal
        card_per_hand: int
            the number of cards in each hand, -1 represent dealing 
            all cards. The first several Hand will receive 1 more 
            cards if necessary.
        Returns
        -------
        list
            list of all hands, with length equal to num_hand

        '''
        if card_per_hand == -1:
            card_per_hand = len(self.cards) // num_hand
            hand_size = [card_per_hand] * num_hand
            for i in range(len(self.cards) % num_hand):
                hand_size[i] += 1
        else:
            hand_size = [card_per_hand] * num_hand
        return [Hand(self.deal_hand(s)) for s in hand_size]
