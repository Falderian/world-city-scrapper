from bs4 import BeautifulSoup
import requests

from helpers import collect_all_cities_links, collect_city_info

main_page_url = "https://www.worldcitydb.com/search-by-country?lang=en_US"

page = requests.get(main_page_url)

cities_links = []
if page.status_code == 200:
    cities_links = collect_all_cities_links(page)

collect_city_info(cities_links[0])
