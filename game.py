import random
import time

class Game():
    def __init__(self):
        self.options = ['ROCK', 'PAPER', 'SCISSORS']
        self.computer_guess = ''
        self.person_guess = ''
        self.point = 0
        self.computer_point = 0
        self.valid_guess = False
    
    # Assign random value from 'self.options' to computer guess
    def computer_choice(self):
        option = random.choice(self.options).upper()
        self.computer_guess = option
    
    # Prompt user to make a guess and asign to person guess
    def person_choice(self):
        try:
            choice = input('Rock, Paper or Scissors?   ').upper()
            if choice.upper() not in self.options:
                self.valid_guess = False
                raise ValueError('You must choose Rock, Paper or Scissors...\n')
        except ValueError as err:
            print('\nThat is not a valid choice! 👎')
            print(f'{err}')
        else:
            self.valid_guess = True
            self.person_guess = choice
 
    # Check user guess against computer guess 
    # Asign points if necessary
    def check_point(self):
        message = 'Well done! You beat the computer and get one point.'
        if self.person_guess.upper() == 'SCISSORS' and self.computer_guess == 'PAPER':
            self.point += 1
            print(message)
        elif self.person_guess.upper() == 'ROCK' and self.computer_guess == 'SCISSORS':
            self.point += 1
            print(message)
        elif self.person_guess.upper() == 'PAPER' and self.computer_guess == 'ROCK':
            self.point += 1
            print(message)
        elif self.person_guess.upper() == self.computer_guess:
            print('You both guessed the same! No point.')
        else: 
            self.computer_point += 1
            print('Computer beat you that round... ')
        print(f'\n🙍 Your points: {self.point}')
        print(f'💻 Computer Points: {self.computer_point}\n')
    
    # After point has been checked, reset guess back to empty string
    def reset_choices(self):
        self.computer_guess = ''
        self.person_guess = ''

    # Check if user has achieved 3 points
    def check_win(self):
        if self.point == 3:
            return True
        else:
            return False
    
    def start_game(self):
        game_running = True
        print('ROCK PAPER SCISSORS... GO... 🤞')
        while game_running:
            self.computer_choice()
            self.person_choice()
            if self.valid_guess:
                print('Rock...')
                time.sleep(0.4)
                print('Paper...')
                time.sleep(0.4)
                print('Scissors...')
                time.sleep(0.4)
                print('Go!')
                self.check_point()
            self.reset_choices()
            if self.check_win():
                print('YOU WON! CONGRATULATIONS 🔥')
                game_running = False
            elif self.computer_point  == 3:
                print('SORRY, YOU LOST. 🤫')
                game_running = False
        
        print('GAME OVER!')


if __name__ == '__main__':
    game = Game()
    game.start_game()