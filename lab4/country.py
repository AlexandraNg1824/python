#Name: Wingyi Ng
#Lab 4
#country.py

class Country:
    '''Store the Country name and the Country's languages'''
    def __init__(self, countryName, languages):
        self._countryName = countryName
        self._languages = tuple(languages)
        
    def getCountryName(self):      ### docstring for each public method   -1/4pt
        return self._countryName
    
    def getLanguages(self):
        return self._languages   
        
