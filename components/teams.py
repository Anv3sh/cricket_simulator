class Teams:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.captain = None
        self.batsmen = []
        self.bowlers = []
        self.next_batsman = 0
        self.next_bowler = 0

        self.select_captain(0)

    def select_captain(self, captain_index):
        self.captain = self.players[captain_index]

    def set_batting_order(self, batting_order):
        for index in batting_order:
            self.batsmen.append(self.players[index])

    def set_bowling_order(self, bowling_order):
        for index in bowling_order:
            self.bowlers.append(self.players[index])

    def get_next_batsman(self):
        batsman = self.batsmen[self.next_batsman]
        self.next_batsman = (self.next_batsman + 1) % len(self.batsmen)
        return batsman

    def get_next_bowler(self):
        if len(self.bowlers) == 0:
            raise ValueError("No bowlers in the team.")
        
        bowler = self.bowlers[self.next_bowler]
        fielders = [player for player in self.players if player != bowler]
        self.next_bowler = (self.next_bowler + 1) % len(self.bowlers)
        
        if self.next_bowler >= len(self.bowlers):
            self.next_bowler = 0
        return bowler,fielders