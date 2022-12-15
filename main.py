from requests import get    
from bs4 import BeautifulSoup
import json

respons = get('https://en.wikipedia.org/wiki/Khabib_Nurmagomedov')
print(respons.status_code)

soup = BeautifulSoup(respons.text, 'html.parser')

print(soup.title.string)
tables = soup.find_all('table', attrs={'class':'wikitable'})
matches = tables[1]
trs = matches.find_all('tr')

opponents = []

for tr in trs:
    tds = tr.find_all('td')
    if not tds :
        continue

    opponents_node = tds[2]
    opponents_name = opponents_node.string
    if opponents_name is None:
        opponents.append(opponents_name)
        opponents_name = opponents_node.a.string

    opponents.append(opponents_name.strip('\n'))

print(opponents)

opponents_json = json.dumps(opponents)
print(opponents_json)

with open('khabib_opponents.json', 'w', encoding='utf-8') as f:
    f.write(opponents_json)
   
# with open('khabib_2.html', 'w', encoding='utf-8') as f:
#     f.write(respons.text)
   


# with open('khabib.html', 'r', encoding='utf-8') as f:
#     content = f.read()
#     print(content)