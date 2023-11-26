from player import Player

class TennisGame:
    def __init__(self, player1, player2):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
    
    def tennis_translation(self, score):
        match score:
            case 0:
                return "Love"
            case 1:
                return "Fifteen"
            case 2: 
                return "Thirty"
            case 3:
                return "Forty"
    
    def get_score(self):
        if self.player1.score == self.player2.score:
            if self.player1.score >= 3:
                return "Deuce"
            else:
                return f"{self.tennis_translation(self.player1.score)}-All"
        elif self.player1.score >= 4 or self.player2.score >= 4:
            temp = (self.player1.score - self.player2.score)
            match temp:
                case 1:
                    return "Advantage player1"
                case -1:
                    return "Advantage player2"
                case 2:
                    return "Win for player1"
                case -2:
                    return "Win for player2"
                case 3:
                    return "Win for player1"
                case -3:
                    return "Win for player2"
                case 4:
                    return "Win for player1"
                case -4:
                    return "Win for player2"
        else:
            return f"{self.tennis_translation(self.player1.score)}-{self.tennis_translation(self.player2.score)}"  
