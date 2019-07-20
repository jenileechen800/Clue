import random

class BlankDeck:

    def __init__(self, players):
        self.all_chars = ["G", "M", "Pe", "Pl", "S", "W"]
        self.all_rooms = ["C", "Ba", "K", "D", "Lo", "H", "S", "Li", "Bi"]
        self.all_weopans = ["C", "D", "R", "L", "R", "W"]
        self.players = players

    def assign_cards(self):
        self.pick_chars()
        self.pick_rooms()
        self.pick_weopans()

    def pick_chars(self):
        env_char = self.all_chars[random.randrange(0, len(self.all_chars))]
        self.all_chars.remove(env_char)

        for char_card in self.all_chars:
            random.shuffle(self.all_chars)

            for player in self.players:
                player.add_char_card(char_card)

    def pick_rooms(self):
        env_room = self.all_rooms[random.randrange(0, len(self.all_rooms))]
        self.all_rooms.remove(env_room)

        for room_card in self.all_rooms:
            random.shuffle(self.all_rooms)

            for player in self.players:
                player.add_room_card(room_card)

    def pick_weopans(self):
        env_weopan = self.all_weopans[random.randrange(0, len(self.all_weopans))]
        self.all_weopans.remove(env_weopan)

        for weopan_card in self.all_weopans:
            random.shuffle(self.all_weopans)

            for player in self.players:
                player.add_weopan_card(weopan_card)
























