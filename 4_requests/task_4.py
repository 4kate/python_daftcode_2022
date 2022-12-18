import requests
import bs4
from typing import Set


def get_recepie_links(keyword: str) -> Set[str]:
    """
    Napisz funkcję która pobierze linki do przepisów z wyszukiwania o zadanym słowie kluczowym
    ze strony https://www.kwestiasmaku.com

    Tips:
        1. Zobacz jak budowane jest zapytanie wyszukujące
        2. Zobacz w jakim kontenerze znajdują się wyniki wyszukiwania
        3. Ugotuj zupe na podstawie przepisu wonsz w sieci :))

    Przykład:
    >>> get_recepie_links("placki")
    {'https://www.kwestiasmaku.com/przepis/placki-kukurydziane',
     'https://www.kwestiasmaku.com/przepis/placki-twarogowe',
     'https://www.kwestiasmaku.com/przepis/placki-z-batatow',
     'https://www.kwestiasmaku.com/przepis/placki-z-ciecierzycy',
     'https://www.kwestiasmaku.com/przepis/placki-z-dyni',
     'https://www.kwestiasmaku.com/przepis/placki-z-kalafiora',
     'https://www.kwestiasmaku.com/przepis/placki-ziemniaczane'}
    """
    
    #open F12 -> Network -> XHR -> use search on www site -> click on new request and find in Headers tab url in Referer
    url = 'https://www.kwestiasmaku.com/szukaj'
    params = {'search_api_views_fulltext': keyword}
    new_set = set()

    r = requests.get(url, params=params)
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    search_result = soup.find(id="block-system-main")

    for a in search_result.find_all('a', href=True):
        if a['href'].startswith('/przepis'):
            new_set.add('https://www.kwestiasmaku.com'+ a['href'])
    
    return new_set
