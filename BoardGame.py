import Player
from GameObjs.BlankDeck import BlankDeck

class BoardGame:

    def __init__(self):
        self.env_char, self.env_weopan, self.env_room = self.assign_cards()
        self.players = self.configure_players()
        self.deck = BlankDeck(self.players)

    def configure_players(self):
        num_players = input("How many players would you like?")
        players = []

        for i in range(len(num_players)):
            players += Player(input("Enter player " + i + " name:\n"))

        return players


