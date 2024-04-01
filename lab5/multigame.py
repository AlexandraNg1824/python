#Name: Wingyi Ng
#Lab 5
#multigame.py
# I do not know how to run the unit test in lab5_game.py so i did it here
# I when I tried to run the game in expert level (on line 37) it created two game windows
# So I commented it out, seem like I was using a wrong method
import re
from lab5_game import Game

class Multigame(Game):
    def __init__(self):
        super().__init__()
        self._choiceStr = 'beginner'
    
    def userChoice(self):
        '''to get user's choice'''
        choice = ""
        choiceStr = ""
        print("1. beginner")
        print("2. expert")
        while(choice != '1' and choice != '2'):
            choice = input("Please enter a level: ")
        if choice == '2':
            self._choiceStr = "expert"
        elif choice == '1':
            self._choiceStr = "beginner"
        return choice
            
    def play(self):
        '''to validate user input then create the game and output their scores'''
        print("Welcome to the color memory game")
        userInput = input("Ready to play? ")
        valid = re.match(r'\b[\s\w]*y[eau]*[ahps]*[h*s*]\b', userInput.lower())
        gameplayed = 0
        while valid:
            choice = self.userChoice()
            print('Level ',choice)
            #g = Game(level=self._choiceStr)
            #(i was trying to set the game level in here, but it created two game window instead)
            self.mainloop() 
            userInput = input("Ready to play? ")
            valid = re.match(r'\b[\s\w]*y[eau]*[ahps]*[h*s*]\b', userInput.lower())
            gameplayed += 1
        print('Goodbye') 
        if gameplayed > 0: 
            print("You've played ", gameplayed, " game(s)")
            print("Highest score ", self.getScore())
            print("Average score ", f'{self.getScore()/gameplayed: .1f}')
        
#unit test
if __name__ == "__main__":
    game = Multigame()  # Create an instance of Multigame
    game.play()       
        
        