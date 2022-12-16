from bs4 import BeautifulSoup

def get_opponents(html):
    soup = BeautifulSoup(html, 'html.parser')

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

    return opponents
