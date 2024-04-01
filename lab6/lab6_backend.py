#Name: Wingyi Ng
#lab6 backend

import re
filename = "countries-languages.txt"

def genEverything():
    '''to search and output the entire file'''
    with open("countries-languages.txt", 'r') as infile:
        for line in infile:
            m = ','.join(re.findall(r'\b[\-a-zA-Z\s]+\b(?![^\(]*\))', line))
            m = m.replace(" ,",",")
            yield [m]
              
            
def genLineNum(starting = 1, ending = 198):
    '''to search the file from starting line to ending line'''
    with open("countries-languages.txt", 'r') as infile:
        for num, line in enumerate(infile):
            if starting - 1 <= num < ending:
                m = ','.join(re.findall(r'\b[\-a-zA-Z\s]+\b(?![^\(]*\))', line))
                m = m.replace(" ,",",")            
                yield [m]
                
def genLineLetter(letter = 'A'):
    '''to search the countries from starting letter'''
    with open("countries-languages.txt", 'r') as infile:
        for line in infile:
            if letter.upper() == line[0]:
                m = ','.join(re.findall(r'\b[\-a-zA-Z\s]+\b(?![^\(]*\))', line))
                m = m.replace(" ,",",")
                yield [m]
                
def search(*args, **kwargs):
    '''to accept userInput and gen the corresponding generator'''
    num = len(args) + len(kwargs)
    generators = {
        0: genEverything,
        1: genLineLetter,
        2: genLineNum
    }
    try:
        generatorF = generators[num]
        userInput = str(args) + str(kwargs) 
        return generatorF(*args, **kwargs)
    except KeyError:
        raise ValueError("Incorrect number of arguments.")
    



    

