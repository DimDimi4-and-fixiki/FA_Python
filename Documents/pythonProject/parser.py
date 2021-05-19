from bs4 import BeautifulSoup
import requests
import re


class Parser(object):
    def __init__(self, url: str):
        self.url = url
        self.countries = ["Country"]
        self.cities = ["City"]
        self.airports = ["Airport"]
        self.soup = None
        self.links = []
        self.texts = []
        self.all_text = ""  # all text in one line

    def get_name(self):
        pass

    def put_spaces(self, line: str):
        return re.sub(r"\B([A-Z])", r" \1", line)


    def get_data(self):
        page = requests.get(self.url).text
        self.soup = BeautifulSoup(page, "lxml")
        rows = self.soup.findAll('td')  # All <td/>

        for row in rows:
            for column in row:
                try:
                    text = str(column.text)  # text in the link
                    self.all_text += " " + text.replace(" ", '')
                except Exception:
                    pass
        words = re.split('Airport', re.sub(r'[0-9]', '', self.all_text.replace('\d+', '').replace("[", "").replace("]", "").replace("Seasonal", "")
                       .replace("Terminated", "").replace("Airport Closed", "").replace("Focus city", "")))
        cur_country = "Armenia"
        for elem in words:
            r_item = ''  # We need to remove all ''
            line = list(elem.split(" "))
            while r_item in line:
                line.remove(r_item)
            if len(line) == 3:
                cur_country = line[0]
                self.countries.append(self.put_spaces(line[0]))
                self.cities.append(self.put_spaces(line[1]))
                self.airports.append(self.put_spaces(line[-1] + "Airport"))
            elif len(line) == 2:
                self.countries.append(self.put_spaces(cur_country))
                self.cities.append(self.put_spaces(line[0]))
                self.airports.append(self.put_spaces(line[-1] + "Airport"))
        return [self.countries, self.cities, self.airports]
