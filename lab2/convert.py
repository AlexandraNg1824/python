# Convert module
# Functions to convert numeric ones, teens, and tens to strings


def toOnes(digit) :
   ''' Turn a digit into an equivalent word ''' 
   if digit == 1 : return "one"
   if digit == 2 : return "two"
   if digit == 3 : return "three"
   if digit == 4 : return "four"
   if digit == 5 : return "five"
   if digit == 6 : return "six"
   if digit == 7 : return "seven"
   if digit == 8 : return "eight"
   if digit == 9 : return "nine"
   return ""

def toTeens(number) :
   ''' Turn a number between 10 and 19 into an equivalent word '''  
   if number == 10 : return "ten"
   if number == 11 : return "eleven"
   if number == 12 : return "twelve"
   if number == 13 : return "thirteen"
   if number == 14 : return "fourteen"
   if number == 15 : return "fifteen"
   if number == 16 : return "sixteen"
   if number == 17 : return "seventeen"
   if number == 18 : return "eighteen"
   if number == 19 : return "nineteen"
   return ""

def toTens(number) :
   ''' Turn a number between 20 and 99 into an equivalent word ''' 
   if number >= 90 : return "ninety"
   if number >= 80 : return "eighty"
   if number >= 70 : return "seventy"
   if number >= 60 : return "sixty"
   if number >= 50 : return "fifty"
   if number >= 40 : return "forty"
   if number >= 30 : return "thirty"
   if number >= 20 : return "twenty"
   return ""

