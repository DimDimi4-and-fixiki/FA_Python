from parser import Parser

url = "https://en.wikipedia.org/wiki/List_of_Pobeda_destinations"
parser = Parser(url=url)
data = parser.get_data()
country = data[0]
city = data[1]
airport = data[-1]
print(country)
print(city)
print(airport)