class DiceGame:

    def __init__(self, human_player, comp_player):
        self.human_player = human_player
        self.comp_player = comp_player

    def start_game(self):
        round_counter = 1
        print(f"--------------------------------------------------------")
        print(f"--------------------------------------------------------")
        print(f"--------------------------------------------------------")
        print(f"--------------------------------------------------------")
        print(f"--------------Welcome to the Dice Game!!----------------")
        print(f"--------------------------------------------------------")
        print(f"--------------------------------------------------------")
        print(f"--------------------------------------------------------")
        print(f"--------------------------------------------------------")
        print(f"You are the player and will be playing against the computer. You will roll the dice"
              "followed by the computer. The player with the higher roll wins the round.")
        print(f"Your score: {self.human_player.counter} | Computer score: {self.comp_player.counter}")
        
        while self.human_player.counter > 0 and self.comp_player.counter > 0:
            
            print("")
            print(f"Round: {round_counter}")
            self.start_round()
            round_counter = round_counter + 1
            
        if self.human_player.counter == 0:
            print(f"----------------------------------------")
            print(f"----------------------------------------")
            print(f"----------------Game Over---------------")
            print(f"----------------------------------------")
            print(f"----------------------------------------")
            print(f"-->>Congratulations!! You have won the game.")
        elif self.comp_player.counter == 0:
            print(f"----------------------------------------")
            print(f"----------------------------------------")
            print(f"----------------Game Over---------------")
            print(f"----------------------------------------")
            print(f"----------------------------------------")
            print(f"-->>Computer won the game. Better luck next time")
            
    def start_round(self):
        # round_counter = 1
        
        # time.sleep(1.5)
        print(f"Press Enter to roll the dice for the round")
        input()
        self.human_player.roll_die()
        self.comp_player.roll_die()
        print(f"Your scored: {self.human_player.die.die_value} | Computer scored: {self.comp_player.die.die_value}")
        if self.human_player.die.die_value > self.comp_player.die.die_value:
            print(f"You won the round")
            self.human_player.decrement_counter()
            self.comp_player.increment_counter()
        elif self.human_player.die.die_value < self.comp_player.die.die_value:
            print(f"Computer won the round")
            self.human_player.increment_counter()
            self.comp_player.decrement_counter()
        else:
            print(f"This round is a tie")

        # print(f"Latest scores -> Your score: {self.human_player.counter}, Computer score: {self.comp_player.counter}")
        self.show_scores()

    def show_scores(self):
        print(f"Your score: {self.human_player.counter} | Computer score: {self.comp_player.counter}")