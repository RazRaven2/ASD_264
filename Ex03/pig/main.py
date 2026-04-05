from pigdice_object import PigGame

def main():
    game = PigGame()
    game.display_rules()
    game.request_player_names()
    game.request_winning_score()
    print("\nLet's play Pig!\n")
    while game.play_game():
        pass
    print("Thanks for playing!")

if __name__ == "__main__":
    main()