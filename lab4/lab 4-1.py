#Name: Wingyi Ng
#Lab 4
#lab4.py (UI)

import csv
from languages import Languages

class UI:
    filename = "lab4out.csv"
    
    def __init__(self):
        self._choice = Languages()
        self._choice.mostCommon()
        
    def run(self):
        '''to ask user for input'''
        userInput = 0
        outputSet = set()
        while (userInput != 3): 
            try:
                print("\n1. Print languages of a country")
                print("2. Compare languages of 2 countries")
                print("3. Quit")
                print("Please enter 1-3 only")
                userInput = int(input("Enter your choice: "))
                if userInput == 1:
                    output = self._choice.languageOfCountry()
                    if(output != None):
                        outputSet.add(output)
                elif userInput == 2:
                    output2 = self._choice.compare()
                    for i in output2:
                        outputSet.add(i)  
                    ### don't add this, not part of search  -1/2pt
                    
            except ValueError:
                print("Invalid input")
        print("Output of country searches are saved in lab4out.csv")
        self.toOutput(outputSet)
                
    def toOutput(self, outputSet):
        '''to save output to csv'''
        with open(UI.filename, "w", newline="") as outfile:
            writer = csv.writer(outfile)
            for data in outputSet:
                writer.writerow(data)
            ### each data output should be comma separated name and languages
            ### not name and list of languages    -1/2pt
       

                
obj = UI()
obj.run()