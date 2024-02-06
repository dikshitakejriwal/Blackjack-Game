for self.player in self.player_list:#everyone plays round
                if self.dealer.card_sum!=21:#natural blackjack for player
                    self.player.card_sum==21:
                        self.player.record_win()
                    else:
                        self.player.play_round()
                    #natural_list.append(self.player)
                    print("1")
        
                elif self.dealer.card_sum==21:#both player and dealer has a natural blackjack
                    if self.player.card_sum==21:
                        self.player.record_tie()
                    else:
                        self.player.record_loss()

        >>> import random; random.seed(963)
        >>> game = BlackjackGame(["one","two","three","four","five","six"])
        >>> print(game.play_rounds(5))
        '''
        Round 1
        Dealer: [4, 10, 3] 0/0/0
        one: [6, 10] 0/0/1
        two: [11, 8] 1/0/0
        three: [5, 8, 9] 0/0/1
        four: [2, 11, 11] 0/0/1
        five: [10, 10, 3] 0/0/1
        six: [3, 10] 0/0/1

        Round 2
        Dealer: [10, 11] 0/0/0
        one: [2, 10, 10] 0/0/2
        two: [2, 6, 6, 8] 1/0/1
        three: [6, 7] 0/0/2
        four: [2, 7] 0/0/2
        five: [10, 10, 6] 0/0/2
        six: [5, 5] 0/0/2

        Round 3
        Dealer: [4, 10, 3] 0/0/0
        one: [9, 7, 8] 0/0/3
        two: [10, 10, 9] 1/0/2
        three: [10, 8, 9] 0/0/3
        four: [5, 4] 0/0/3
        five: [10, 5] 0/0/3
        six: [8, 3, 11] 0/0/3

        Round 4
        Dealer: [3, 10, 3, 9] 0/0/0
        one: [11, 4, 11] 0/0/4
        two: [6, 10, 9] 1/0/3
        three: [10, 7, 6] 0/0/4
        four: [7, 4, 8, 8] 0/0/4
        five: [9, 7] 1/0/3
        six: [10, 4, 3] 1/0/3

        Round 5
        Dealer: [3, 10, 8] 0/0/0
        one: [10, 7] 0/0/5
        two: [7, 3] 1/0/4
        three: [10, 8] 0/0/5
        four: [11, 2, 9] 0/0/5
        five: [10, 10] 1/0/4
        six: [11, 6] 1/0/4
        """