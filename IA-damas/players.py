class player():
    def __init__(self,side):
        self.side=side

        self.complet_move=False

    def create_event_lister(self):
        pass

class human_player(player):
    def __init__(self,side):
        player.__init__(self,side)
        self.piece_move=None

    def create_event_lister(self):
        pass

class IA_player(player):
    def __init__(self,side):
        player.__init__(self,side)

    def create_event_lister(self):
        pass