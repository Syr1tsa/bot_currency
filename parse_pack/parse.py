import requests
from bs4 import BeautifulSoup as BS
class Parse():
    
    def __init__(self, url):
        self.url = url
        self.values = []
        source = requests.get(self.url)
        self.html = BS(source.text, 'lxml')

    def get_content(self):
        table = self.html.find('table', {'id': 'courses-main'})
        tbody = table.find('tbody')
        for tr in tbody.find_all('tr'): 
            td = tr.find_all('td', {'class':''})
            for el in td:
                if el.text != '':
                    self.values.append(el.text.strip())
            
        return self.values[4:]
        

