# filename: rugby_world_cup.py
import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Rugby_World_Cup"
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})
for row in table.find_all('tr'):
    cells = row.find_all('td')
    if len(cells) > 0 and cells[0].text.strip() == "South Africa":
        print(cells[1].text.strip())