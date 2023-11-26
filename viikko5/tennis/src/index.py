from tennis_game import TennisGame

def main():
    game = TennisGame("player1", "player2")

    print(game.get_score())

    game.player1.won_point()
    print(game.get_score())

    game.player1.won_point()
    print(game.get_score())

    game.player2.won_point()
    print(game.get_score())

    game.player1.won_point()
    print(game.get_score())

    game.player1.won_point()
    print(game.get_score())


if __name__ == "__main__":
    main()
