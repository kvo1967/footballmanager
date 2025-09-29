import requests
from bs4 import BeautifulSoup
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from unavailable import Unavailable
from clubs.club_registry import club_registry


def get_unavailable_players():
    url = "https://www.blessuresenschorsingen.nl/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept-Encoding': 'identity'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, 'html.parser')
    unavailable_list = []

    sections = soup.find_all('section', class_='mb-2')

    for section in sections:
        club_header = section.find('h2')
        if club_header and club_header.find('a'):
            club_name_text = club_header.find('a').text.strip()
            club = club_registry.get_by_name(club_name_text)
            if not club:
                continue

            players = section.find_all('a', class_='group')
            for player in players:
                player_name_elem = player.find('strong')
                description_elem = player.find('span', class_='text-sm')

                expected_return = "niet bekend"
                return_img = player.find('img', title='Verwachte terugkeer')
                if return_img:
                    return_span = return_img.find_next('span')
                    if return_span:
                        date_span = return_span.find_next('span')
                        if date_span:
                            expected_return = date_span.text.strip()

                if player_name_elem and description_elem:
                    player_name = player_name_elem.text.strip()
                    description = description_elem.text.strip()

                    unavailable = Unavailable(
                        player_name=player_name,
                        club=club,
                        description=description,
                        expected_return=expected_return
                    )
                    unavailable_list.append(unavailable)

    return unavailable_list