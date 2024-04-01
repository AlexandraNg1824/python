# name: Wingyi Ng 
# SID: 20570785
#CIS 41A Lab2
import convert

def getInput():
    '''to validate if the user input is between 0 and 1,000,000,000 exclusive'''
    valid = False
    while valid == False:
        UserInput = input('Enter a positive integer less than 1 billion: ')
        removedComma = UserInput.replace(",","")
        if removedComma.isnumeric():
            num = int(removedComma)
            if num < 1000000000 and num > 0:
                valid = True
                return num
            else:
                print('positive integer less than 1 billion only')
        else:
            print('positive integer less than 1 billion only')
            
        
def toWords(num):
    '''To convert millions/thousands/ones to a text string'''
    numString = ""
    if num // 1000000 > 0:
        numString = str(convertTriplet(num // 1000000)) + " " + "million " 
    if num % 1000000 // 1000 > 0:
        numString += str(convertTriplet(num % 1000000 // 1000)) + " " + 'thousand '
    if ((num % 1000000) % 1000) > 0:
        numString += str(convertTriplet((num % 1000000) % 1000))
    return numString
        
def convertTriplet(num):
    '''to check if there a hundreds/tens/teens/ones value'''
    totalString = ""
    if num // 100 != 0:
        totalString = (convert.toOnes(num // 100)) + " " + 'hundred '
    if (num % 100) >= 20 and (num % 100) <= 99:
        totalString += convert.toTens(num % 100) 
        if num % 10 != 0:
            totalString += '-' + convert.toOnes(num % 10)
    elif ((num % 100) >= 10 and (num % 100) <= 19):
        totalString += convert.toTeens(num % 100)
    else: #(num % 10) > 0 and (num % 10) <= 9
        totalString += convert.toOnes(num % 10)
    return totalString
    
def main():
    '''main: to call the function getInput and toWords, 
       to transform a positive integer from user's input to a text string'''
    num = getInput()
    print('Number is:', toWords(num))
    userinput = input('Another number? y/n: ')
    while userinput != 'n' and userinput != 'N':
        if userinput == 'y' or userinput == 'Y':
            num = getInput()
            print('Number is:', toWords(num))
            userinput = input('Another number? y/n: ')
        else:
            userinput = input('Error! Do you want another number? y/n: ')

main()
