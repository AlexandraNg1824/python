#Name: Wingyi Ng
#Lab 5
#customGame.py
# I do not know how to run the unit test in lab5_game.py so i did it here
# When I tried to run the game in expert level (on line 72) it created two game windows
# So I commented it out, seem like I was using a wrong method

from lab5_game import Game
import csv
import re

class CustomGame(Game):
    def __init__(self):
        super().__init__()
        self._choiceStr = 'beginner'
        self._highestScore = []
        self._userName = ""
        self._userExist = False
    
    def name(self):
        '''Check if the file exist and if the username is in the file'''
        self._userName = input("Please enter your name: ")
        try:
            with open("players.csv", 'r', newline='') as infile:
                #Read the content inside
                reader = csv.reader(infile, delimiter='\t')
                #skip the first row (name, highest, level, etc)
                header = next(reader, None) #check if header exist
                if header is not None: 
                    for line in reader:
                        data = line[0].split(',')
                        #coz print(lin) = [ng,1,beginner]
                        self._highestScore.append(int(data[1]))
                        if data[0] == self._userName:
                            self._userExist = True
                            print("Welcome to the game, ", self._userName)
                            print("Your highest score so far is ", data[1])
                            print("The game was at the ", data[2])
                            return
                    print("Welcome to the game, ", self._userName)
        except FileNotFoundError:
            with open("players.csv", 'w', newline= "") as outfile:
                writer = csv.writer(outfile, delimiter=',')
                writer.writerow(["name", "highest score", "level"])
                
    def gameLevel(self):
        '''ask the user for gameLevel'''
        print("b.beginner")
        print("e.expert")
        gamelevel = input("Please enter your choice: ")
        valid = False
        level = ""
        while not valid:
            rule1 = re.search(r'\b(b)\b', gamelevel, re.IGNORECASE)
            rule2 = re.search(r'\b(e)\b', gamelevel, re.IGNORECASE)
            if rule1 and not rule2:
                valid = True
                self._choiceStr = 'expert'
            elif rule2 and not rule1:
                valid = True             
            else:
                print("Please choose either 'b' or 'e'")
                print("b.beginner")
                print("e.expert")                
                gamelevel = input("Please enter your choice: ")
        
            
    def play(self):
        '''play the game'''
        self.name()
        self.gameLevel()
        #g = Game(level=self._choiceStr)
        self.mainloop()         
        self._highestScore.append(self._score)
        top = max(self._highestScore)
        if self._score == 0:
            print('good try')
        elif self._score > top:
            print("you’re the top player")
        elif self._score == top:
            count = 0
            for num in self._highestScore:
                if self._score == num:
                    count += 1
            print("you 're the top ", count, " of all players")
        else:
            print("good game")
        self.saveRecord()
            

    def saveRecord(self):
        '''save the record to a csv file'''
        if self._userExist == False:
            with open("players.csv", "a", newline="") as outfile:
                writer = csv.writer(outfile, delimiter=',')
                writer.writerow([self._userName, self._score, self._choiceStr])
        else:
            with open("players.csv", 'r', newline='') as infile:
                        reader = csv.reader(infile, delimiter=',')
                        rows = list(reader)  # Convert reader to list for easy iteration
            #save the info into the list
            for row in rows:
                if row[0] == self._userName and self._score > int(row[1]):
                    row[1] = str(self._score)
                    row[2] = self._choiceStr
            # Write the list to the file
            with open("players.csv", "w", newline="") as outfile:
                writer = csv.writer(outfile, delimiter=',')
                writer.writerows(rows)
#unit test
if __name__ == "__main__":
    game = CustomGame()  # Create an instance of Multigame
    game.play()      