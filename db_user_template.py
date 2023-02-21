class User:
    def __init__(self, username='', games=['']) -> None:
        self.username = username
        self.games = games

    def set_username(self, username) -> None:
        self.username = username
    
    def set_games(self, game) -> None:
        self.games = game

    def print_profile(self) -> str:
        print(f"Username: {self.username}\n")
        no_games = len(self.games)
        print(f"Number of Games: {no_games}\n")
        for i in range(no_games):
            print(f"Game {i+1}: {self.games[i].name}")
            print(f"Games Played: {self.games[i].get_games_played()}")
            print(f"Wins: {self.games[i].get_wins()}")
            print(f"Losses: {self.games[i].get_losses()}")
            print(f"Win Rate: {self.games[i].get_win_rate()}")
            print()


    class Game:
        def __init__(self, name='', games_played='0', wins='0', losses='0', win_rate='0.00') -> None:
            self.name = name
            self.games_played = games_played
            self.wins = wins
            self.losses = losses
            self.win_rate = win_rate

        def set_games_played(self, games_played) -> None:
            self.games_played = games_played

        def set_wins(self, wins) -> None:
            self.wins = wins
        
        def set_losses(self, losses) -> None:
            self.losses = losses

        def set_win_rate(self, win_rate) -> None:
            win_rate = self.wins / self.games_played * 100
            self.win_rate = win_rate
        
        def get_games_played(self) -> str:
            return self.games_played
        
        def get_wins(self) -> str:
            return self.wins
        
        def get_losses(self) -> str:
            return self.losses
        
        def get_win_rate(self) -> str:
            return self.win_rate

# Use for testing
x = User('nax')
x.set_games([User.Game('tekken'), User.Game('smash')])
x.games[0].set_games_played('8')
x.games[0].set_wins('5')
x.games[0].set_losses('3')
x.games[1].set_games_played('10')
x.games[1].set_wins('7')
x.games[1].set_losses('3')
x.print_profile()