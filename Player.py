
class Player:

    def __init__(self, name):
        self.name = name
        self.guesses_chars = {"G": "O", "M": "O", "Pe": "O", "Pl": "O", "S": "O", "W": "O"}
        self.guesses_weopans = {"C": "O", "D": "O", "R": "O", "L": "O", "R": "O", "W": "O"}
        self.guesses_rooms = {"C": "O", "Ba": "O", "K": "D", "Lo": "O", "H": "O", "S": "O", "Li": "O", "Bi": "O"}

        self.cards_char = []
        self.cards_weopans = []
        self.cards_rooms = []

    def add_char_card(self, card):
        self.cards_char += card

    def add_weopan_card(self, card):
        self.cards_weopans += card

    def add_room_card(self, card):
        self.cards_rooms += card
