from src.die import Die
from src.player import Player
from src.dicegame import DiceGame

def main():
    die1 = Die()
    die2 = Die()
    p1 = Player(die1, is_computer=False)
    p2 = Player(die2, is_computer=True)
    
    game = DiceGame(p1, p2)
    game.start_game()

if __name__ == "__main__":
    main()