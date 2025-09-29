import clubs.club

class Match:
    def __init__(self, home_team, away_team):
        self.home_team = home_team
        self.away_team = away_team
        self.home_win = 0.0
        self.draw = 0.0
        self.away_win = 0.0

    def set_odds(self, home_win, draw, away_win):
        self.home_win = home_win
        self.draw = draw
        self.away_win = away_win