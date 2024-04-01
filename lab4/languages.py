#Name: Wingyi Ng
#Lab 4
#languages.py

from country import Country
import collections

class Languages:
    ''' a container of Country objects, and it provides searches' functions''' 
    filename = "languages.txt"
    
    def __init__(self):
        self._countries, self._count = self.countries()
        
    def getCountries(self):  
        return self._countries

    def countries(self):
        '''read in the file and return two dictionaries'''
        countries = {}
        count = collections.defaultdict(int)
        validfile =  False
        while not validfile:
            try:
                file = input("Enter a filename or press Enter for default file: ")
                ### Languages object can't interact with the user   -1/2pt
                
                if file == "":
                    file = Languages.filename        
                with open(file, "r") as infile:
                    for line in infile: 
                        fields = line.rstrip().split(',')
                        countryName = fields[0]
                        languages = tuple(fields[1:])
                        countries[countryName] = Country(countryName, languages)
                        for lang in fields[1:]:
                            count[lang] += 1
                validfile = True
            except IOError:
                print("No such file or directory:", file)  
                ### Languages object can't interact with the user   -1/2pt
                
        print("There are", len(countries), "countries in the database")
        ### Languages object can't interact with the user   
        
        return (countries, count)
            
    def mostCommon(self):
        '''print the most common langs'''
        topLanguages = {v:k for k,v in self._count.items() if v > 12 and "other" not in k}
        print("The most common languages")
        print(f"{'Language':10s}{'Num of countries':s}")
        for tup in sorted(topLanguages.items(), reverse=True):
            print(f'{tup[1]:10s} {tup[0]:10d}')
        
        
    def languageOfCountry(self):
        '''print the languages of one country'''
        country = input("Name of country: ")
        ### Languages object can't interact with the user   -1/2pt
        
        if country.title() in self._countries:
            print(", ".join(self._countries[country.title()].getLanguages()))
            return (country.title(), ", ".join(self._countries[country.title()].getLanguages()))
        else:
            print(country.title(), "doesn't exist in database") 
            ### Languages object can't interact with the user   -1/2pt
            
            return None
        
    def compare(self):
        '''compare 2 countries' languages'''
        compareSet = set()
        country1string = ""
        country2string = ""
        country1 = input("Name of first country: ")    
        ### Languages object can't interact with the user   -1/2pt
        
        while country1.title() not in self._countries:
            print(country1.title(), "doesn't exist in database")
            ### Languages object can't interact with the user   
            
            country1 = input("Name of first country: ")
            ### Languages object can't interact with the user  
            
        country2 = input("Name of second country: ")
        ### Languages object can't interact with the user   -1/2pt
        
        while country2.title() not in self._countries:
            print(country2.title(), "doesn't exist in database")
            ### Languages object can't interact with the user   
            
            country2 = input("Name of second country: ")
            ### Languages object can't interact with the user  
            
        set1 = set(self._countries[country1.title()].getLanguages())
        set2 = set(self._countries[country2.title()].getLanguages())
        common = set1 & set2
        both = set1 | set2
        if len(common) != 0:
            print("Common language:", ", ".join(common))
            ### Languages object can't interact with the user   
            
        else:
            print("No common language")
            ### Languages object can't interact with the user   
            returnstring = "No common language"
        print("All languages:", ", ".join(sorted(both)))
        ### Languages object can't interact with the user   
        
        country1string = (country1.title(), ", ".join(self._countries[country1.title()].getLanguages()))
        country2string = (country2.title(), ", ".join(self._countries[country2.title()].getLanguages()))
        compareSet.add(country1string)
        compareSet.add(country2string)
        return compareSet
    
    
### there are multiple points deductted because Languages and UI have distinct jobs to do
### as explained in the lab document and in class. This is a main point of OOP
### As written, the code mixed up the jobs of Languages and UI
    
#l=Languages()
#l.mostCommon()
#c = l.compare()