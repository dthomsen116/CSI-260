# num_countries_for_dict = int(input())
# country_input = []
# for i in range(num_countries_for_dict):
#     country_input.append(input())
    
# num_cities_to_lookup = int(input())
# city_input = []
# for i in range(num_cities_to_lookup):
#     city_input.append(input())

countryDict = {}
numCountries = int(input())


for i in range(0,numCountries):
    CountryList = input()
    Countries = CountryList.split
    Country = Countries[0]
    LengthCities = len(Countries)
    
    for id in range(1, LengthCities):
        C = Countries[id]
        countryDict[C]
        
print(countryDict)
numTowns = int(input())

for i in range(0,numTowns):
    town = input()
    print("The town of ", town, " is in", countryDict[town])
    