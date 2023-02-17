import requests
from bs4 import BeautifulSoup

page = requests.get("https://isport.blesk.cz/vysledky/hokej/liga?action=season&season=3089")

soup = BeautifulSoup(page.text, 'html.parser')

match_rows = soup.find_all('div', 'list-score-structured-wapper')

favorite_team = 'Brno'

for match in match_rows:
    match_date = match.find('div', 'datetime-container').text
    match_date = ' '.join(match_date.split())

    match_container = match.find('div', 'match-container')
    home_team = match_container.find('div', 'team-home').find('div', 'team-name').text
    away_team = match_container.find('div', 'team-away').find('div', 'team-name').text
    looser_team = match.find('div', 'team-looser').text

    if favorite_team == home_team or favorite_team == away_team:
        if favorite_team != looser_team:
            print(match_date + " sme porazili " + looser_team)
