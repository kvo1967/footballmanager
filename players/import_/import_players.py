import requests
from bs4 import BeautifulSoup
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from player import Player
from . import import_constants
from clubs.club_registry import club_registry 


def get_players_by_club(club_index: int):
    url = f"https://www.gratisvoetbalmanager.com/statistieken/{club_index}/index.html"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Encoding': 'identity'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    table = soup.find('table', class_='statistics')

    players = []

    if table:
        rows = table.find_all('tr')[1:]

        for row in rows:
            cols = row.find_all('td')
            if len(cols) >= 15:
                club = club_registry.get_by_index(club_index)
                if club is None:
                    raise ValueError(f"No club found for index {club_index}. Player: {cols[1].text.strip()}")

                player = Player(
                    position=cols[0].text.strip(),
                    name=cols[1].text.strip(),
                    price=cols[2].text.strip(),
                    played=cols[3].text.strip(),
                    won=cols[4].text.strip(),
                    draw=cols[5].text.strip(),
                    lost=cols[6].text.strip(),
                    goals_for=cols[7].text.strip(),
                    goals_against=cols[8].text.strip(),
                    clean_sheet=cols[9].text.strip(),
                    assist=cols[10].text.strip(),
                    yellow=cols[11].text.strip(),
                    red=cols[12].text.strip(),
                    og=cols[13].text.strip(),
                    score=cols[14].text.strip(),
                    club=club
                )
                players.append(player)

    return players

def get_players_from_fantasy_game():
    all_players = []
    for club_index in import_constants.ALL_CLUBS:
        club_players = get_players_by_club(club_index)
        all_players.extend(club_players)
    return all_players