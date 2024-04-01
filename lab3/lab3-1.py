#Name: Wingyi Ng
#Lab 3

def main():
    '''to call functions and prompt the user to choose from a menu'''
    countryDict = readFile()  #only read once
    mostCommon(countryDict)
    userInput = 0
    while (userInput != '1' and userInput != '2' and userInput != '3'):   
        print("1. Print languages of a country")
        print("2. Compare languages of 2 countries")
        print("3. Quit")
        print("Please enter 1-3 only")
        userInput = input("Enter your choice: ")
        
    ### should be part of the loop so user can keep searching   -1pt
    if userInput == '1':
        languageOfCountry(countryDict)
    elif userInput == '2':
        compare(countryDict)

def readFile():
    '''to read in and calculate the total countries of a file'''
    countryDict = {}
    filename = input("Enter a filename or press Enter for default file: ")
    if filename == "":
        filename = "languages.txt"
    with open ("languages.txt", "r") as infile: #or copy the file path if it didn't work
        for line in infile: 
            #keys = country, values the rest of the line
            endOfCountry = line.find(",")    ### easier to use split and indexing
            #ignore the first comma
            countryDict[line[:endOfCountry]] = line[endOfCountry + 1:] 
    print("There are", len(countryDict), "countries in the database")
    return countryDict
    
def mostCommon(countryDict):
    '''to find and print the most common languages in the world'''
    countCommon = {}
    listAscending = []
    print("The most common languages")
    print(f"{'Language':12}{'Num of countries':10}")
    for languages in countryDict.values():
        #removing the \n
        languages = languages.strip() 
        #separate each language by","
        language = languages.split(',') 
        for word in language:
            countCommon[word] = countCommon.get(word, 0) + 1
    #removing the non-language
    del countCommon["other"] 
    for x,y in countCommon.items():
        if y >= 12:
            listAscending.append(y)
    listAscending.sort()
    for i in range(len(listAscending)-1, -1, -1):
        for x,y in countCommon.items():
            if listAscending[i] == y:      ### reverse dictionary as discussed in class
                                           ### should not have to use a for loop to search in a dictionary  -1/2pt
                print(f"{x:10}{y:10}")
                
def languageOfCountry(countryDict):
    '''allow the user to check the languages of a country'''
    country = input("Name of country: ")
    if country.title() in countryDict:
        print(countryDict[country.title()])
    else:
        print(country.title(), "doesn't exist in database")

def compare(countryDict):
    '''let the user compare 2 countries' languages'''
    #prompt the user for two countries in the database
    firstCountry = input("Name of first country: ")    
    while firstCountry.title() not in countryDict:
        print(firstCountry.title(), "doesn't exist in database")
        firstCountry = input("Name of first country: ")
    secondCountry = input("Name of second country: ")
    while secondCountry.title() not in countryDict:
        print(secondCountry.title(), "doesn't exist in database")
        secondCountry = input("Name of second country: ")
    #convert user's input to match the dict's key
    firstlanguages = countryDict[firstCountry.title()] 
    secondlanguages = countryDict[secondCountry.title()]
    #separate each language by , then put them to a set
    first = set(firstlanguages.split(',')) 
    second = set(secondlanguages.split(','))
    #find the item which appear in both set
    common = first & second
    #put the common item to a list so they can be sorted
    commonlist = sorted([str(item) for item in common if item]) 
    if len(common) == 0:
        print("No common languages")
    else:
        print("Common language: ", end='')
        print(*commonlist, sep=',')
    allLang = first | second 
    allLanglist = sorted([str(item) for item in allLang if item])
    print("All languages:", end='')
    print(*allLanglist, sep=',')
    ### languages are not always printed on same line  -1/4pt
    ### sample test run:
    '''
    Name of first country: france
    Name of second country: germnay
    Germnay doesn't exist in database
    Name of second country: germany
    No common languages
    All languages:French,German
    ,rapidly declining regional dialects 
'''
        
main()
