from dataclasses import dataclass
import requests
import bs4

@dataclass
class Contact:
    email: str
    phone: str
    address: str
    instagram: str


def get_daftcode_contact_info() -> Contact:
    """
    Napisz funkcję która pobierze z głównej strony Dafta (https://daftcode.pl/)
    dane:
        * Adres email
        * Telefon
        * Adres
        * Link do instagrama
    Tips:
        1. Ugotuj zupę
    """
    r = requests.get('https://daftcode.pl/')
    soup = bs4.BeautifulSoup(r.text, 'html.parser')
    list_all_a = soup.find_all('a')
    href_tags = soup.find_all(href=True)

    email = list_all_a[18].get_text()
    phone = list_all_a[19].get_text()
    address = list_all_a[20].get_text()
    instagram = href_tags[22]['href']

    return Contact(email, phone, address, instagram)
