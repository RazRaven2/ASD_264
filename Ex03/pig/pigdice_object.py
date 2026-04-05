import random
import doctest

class PigGame:
    def __init__(self):
        self.player_names = {"Player 1": "Player 1", "Player 2": "Player 2"}
        self.scores = {"Player 1": 0, "Player 2": 0}
        self.winning_total = 20

    def request_player_names(self):
        """
        Ask players for display names and store them by player slot.

        A blank response keeps the default slot label.
        Duplicate names are suffixed with a number, e.g. Alex (2).
        """
        used_names = set()
        for player_slot in ["Player 1", "Player 2"]:
            entered_name = input(f"Enter a name for {player_slot}: ").strip()
            base_name = entered_name or player_slot
            candidate_name = base_name
            suffix = 2

            # Ensure displayed player names are unique regardless of case.
            while candidate_name.lower() in used_names:
                candidate_name = f"{base_name} ({suffix})"
                suffix += 1

            self.player_names[player_slot] = candidate_name
            used_names.add(candidate_name.lower())

    def request_winning_score(self):
        """
        Ask whether to customize the winning score and update it.

        Entering blank at the score prompt keeps the current score.
        """
        choice = input("Set the winning score? (y/n) ").strip().lower()
        if choice != 'y':
            return

        while True:
            entered_score = input(
                f"Enter winning score (current: {self.winning_total}): "
            ).strip()
            if entered_score == "":
                return
            if entered_score.isdigit() and int(entered_score) > 0:
                self.winning_total = int(entered_score)
                return
            print("Please enter a whole number greater than 0.")

    def display_rules(self):
        """
        Display the rules of the Pig dice game.
        """
        print("~" * 50)
        print("Pig Dice Game Rules:")
        print("1. The game is played by two players: Player 1 and Player 2.")
        print("2. Players take turns to roll a die as many times as they wish, adding the rolled value to a turn total.")
        print("3. If a player rolls a 1, they score nothing for that turn and it becomes the next player's turn.")
        print("4. A player can choose to hold (stop rolling) to add their turn total to their score.")
        print("5. The first player to reach or exceed 20 points wins the game.")
        print("~" * 50)

    def roll_die(self):
        """
        Roll a six-sided die and return the result.
        
        >>> result = PigGame().roll_die()
        >>> 1 <= result <= 6
        True
        """
        return random.randint(1, 6)

    def print_die(self, roll):
        """
        Print an ASCII representation of a six-sided die with
        the given roll.

        Args:
            roll (int): The number rolled on the die.
            
        Doctest:
        >>> PigGame().print_die(1)
         ------- 
        |       |
        |   *   |
        |       |
         ------- 
        >>> PigGame().print_die(2)
         ------- 
        | *     |
        |       |
        |     * |
         ------- 
        """
        die = [
            " ------- ",
            "|       |",
            "|       |",
            "|       |",
            " ------- "
        ]
        if roll == 1:
            die[2] = "|   *   |"
        elif roll == 2:
            die[1] = "| *     |"
            die[3] = "|     * |"
        elif roll == 3:
            die[1] = "| *     |"
            die[2] = "|   *   |"
            die[3] = "|     * |"
        elif roll == 4:
            die[1] = "| *   * |"
            die[3] = "| *   * |"
        elif roll == 5:
            die[1] = "| *   * |"
            die[2] = "|   *   |"
            die[3] = "| *   * |"
        elif roll == 6:
            die[1] = "| * * * |"
            die[3] = "| * * * |"
        for line in die:
            print(line)

    def print_scoreboard(self):
        """
        Print the current scores of Player 1 and Player 2.
        
        Doctest:
        >>> game = PigGame()
        >>> game.scores = {"Player 1": 10, "Player 2": 15}
        >>> game.print_scoreboard()
        <BLANKLINE>
        *****************
        *  SCOREBOARD   *
        *****************
        Player 1: 10
        Player 2: 15
        *****************
        <BLANKLINE>
        """
        print()
        print("*****************")
        print("*  SCOREBOARD   *")
        print("*****************")
        for player_slot in ["Player 1", "Player 2"]:
            print(f"{self.player_names[player_slot]}: {self.scores[player_slot]}")
        print("*****************")
        print()

    def play_turn(self, player):
        """
        Play a single turn for the given player.

        Args:
            player (str): The name of the player ("Player 1" or "Player 2").

        Returns:
            int: The total points scored by the player in this turn.
        
        Doctest:
        >>> from unittest.mock import patch
        >>> with patch('builtins.input', side_effect=['y', 'y']):
        ...     with patch('random.randint', side_effect=[5, 6, 1]):
        ...         PigGame().play_turn("Player 1")
        PLAYER 1'S TURN
         ------- 
        | *   * |
        |   *   |
        | *   * |
         ------- 
        Total is 5
         ------- 
        | * * * |
        |       |
        | * * * |
         ------- 
        Total is 11
         ------- 
        |       |
        |   *   |
        |       |
         ------- 
        Player 1 rolled a 1! No points earned this turn.
        0
        >>> with patch('builtins.input', side_effect=['n']):
        ...     with patch('random.randint', side_effect=[4]):
        ...         PigGame().play_turn("Player 2")
        PLAYER 2'S TURN
         ------- 
        | *   * |
        |       |
        | *   * |
         ------- 
        Total is 4
        4
        """
        player_name = self.player_names[player]
        print(f"{player_name.upper()}'S TURN")
        turn_total = 0
        roll = self.roll_die()
        while roll != 1:
            self.print_die(roll)
            turn_total += roll
            print(f"Total is {turn_total}")
            choice = input("Roll again? (y/n) ")
            if choice.lower() == 'n':
                return turn_total
            roll = self.roll_die()
        self.print_die(roll)
        print(f"{player_name} rolled a 1! No points earned this turn.")
        return 0

    def play_game(self):
        """
        Play a game of Pig between Player 1 and Player 2.
        Returns:
            bool: True if the game should be played again, 
            False otherwise.
        """
        self.scores = {"Player 1": 0, "Player 2": 0}
        while (self.scores["Player 1"] < self.winning_total and 
               self.scores["Player 2"] < self.winning_total):
            for player in ["Player 1", "Player 2"]:
                self.scores[player] += self.play_turn(player)
                self.print_scoreboard()
                if self.scores[player] >= self.winning_total:
                    print(f"{self.player_names[player]} wins!")
                    again = input("Do you want to play again? (y/n) ").lower()
                    return again == 'y'
        return False

if __name__ == "__main__":
    doctest.testmod(verbose=True)