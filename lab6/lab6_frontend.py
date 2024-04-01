#Name: Wingyi Ng
#lab6 frontend
import lab6_backend

def searchForAll(): #needa call the search function to gen
    '''print one country at a time'''
    print("Data for one country at a time")
    generator = lab6_backend.search()
    userInput = input("Press Enter to get next country: ")
    while userInput == '':
        try:
            country = next(generator)
            print(*country)
            userInput = input("Press Enter to get next country: ")
        except StopIteration:
            print("No more data")
            break
        
        
def searchWithLetter():
    '''print countries begins with specific letter'''
    langCount = {} #dict.k = language, dict.v = number of language
    contriesList = [] #coutries list with specific letter
    countries = {} #dict.k = countries, dict.v = language string
    userInput = input("Enter first letter of country names: ")
    while not userInput.isalpha() or not (len(userInput) == 1):
        userInput = input("Enter first letter of country names: ")
    print("Countries starting with ", userInput.upper())
    generator = lab6_backend.search(letter=userInput)
    yesCountry = False
    for country in generator:
        yesCountry = True
        contriesList.append(str(*country).split(',')[0])
        langList = str(*country).split(',')
        countries[str(*country).split(',')[0]] = tuple(str(*country).split(',')[1:])
        for lang in langList:
            langCount[lang] = langCount.get(lang, 0) + 1
    print(*contriesList, sep=', ')
    if not yesCountry:
        print("No country found.")    
    
    common = False
    for num in langCount.values():
        if num > 1:
            common = True
    if(common):
        print("Popular languages:")
    else:
        print("there is no popular language")

        
    def fct(elem):
        return langCount[elem]
    
    for k in sorted(langCount, key=fct, reverse=True):
        if langCount[k] > 1 and k != "other":
            print(k, end=': ')
            temp = []
            for country, lang in countries.items():
                if k in lang:
                    temp.append(country)
                    #print(country, end=", ")
            print(*temp, sep=', ') #append the a list to avoid the last comma

def searchWithLineNum():
    '''print countries with starting line number and ending line number'''
    def valid (start = 0, end = 0):
        while start < 1:
            start = int(input("Enter starting lline number: "))
        while end < start:
            end = int(input("Enter ending line number: "))
        return start, end
    starting, ending = valid()
    generator = lab6_backend.search(starting, ending)
    for i in range(ending - starting + 1): #for 1.5pts EC2
        try:
            country = next(generator)
            print(*country)
        except StopIteration:
            print("Reached last country")
            break        
  
def run():
    '''ask user for input and call the corresponding function'''
    print("1. All countries")
    print("2. Countries in range of lines")
    print("3. Countries starting with a letter")
    print("4. Quit")
    userInput = input("Enter your choice: ")
    while userInput != '1' and userInput != '2' and userInput != '3' and userInput != '4':
        userInput = input("Enter your choice: ")
    if userInput == '1':
        searchForAll()
    elif userInput == '2':
        searchWithLineNum()
    elif userInput == '3':
        searchWithLetter()
        

        
#searchForAll()
#searchWithLetter()
#searchWithLineNum()
run()