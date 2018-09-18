from typing import List
import requests
from collections import namedtuple

Search_Data = namedtuple('Search_Data', 'title')


def search_training_site(search_term: str) -> List[Search_Data]:
    search_term = search_term.replace(" ", "-")
    url = f'http://search.talkpython.fm/api/search?q={search_term}'

    search_response = requests.get(url)
    search_response.raise_for_status()

    data = search_response.json()
    search_data = []
    for d in data['results']:
        search_data.append(Search_Data(d.get('title')))

    return search_data
