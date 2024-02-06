import random


class CardDeck:
    class Card:
        def __init__(self, value):
            self.value = value
            self.next = None

        def __repr__(self):
            return "{}".format(self.value)

    def __init__(self):
        self.top = None

    def shuffle(self):
        card_list = 4 * [x for x in range(2, 12)] + 12 * [10]
        random.shuffle(card_list)

        self.top = None

        for card in card_list:
            new_card = self.Card(card)
            new_card.next = self.top
            self.top = new_card

    def __repr__(self):
        curr = self.top
        out = ""
        card_list = []
        while curr is not None:
            card_list.append(str(curr.value))
            curr = curr.next

        return " ".join(card_list)

    def draw(self):
        """
        >>> import random; random.seed(1)
        >>> deck = CardDeck()
        >>> deck.shuffle()
        >>> deck.draw()
        10
        >>> deck.draw()
        8
        >>> deck.draw()
        10
        >>> deck.draw()
        6
        >>> deck
        8 9 3 10 2 10 6 5 8 10 3 10 9 2 10 9 6 10 5 5 2 6 8 7 2 4 10 4 11 10 3 10 10 5 7 10 10 11 7 7 3 11 10 4 4 9 11 10
        """
        if self.top==None:
            return None
        else:
            current=self.top
            self.top=current.next
            current.next=None
            return current.value
         


if __name__ == "__main__":
    import doctest
    doctest.testmod()
