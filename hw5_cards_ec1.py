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
