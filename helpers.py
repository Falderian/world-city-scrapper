from bs4 import BeautifulSoup
import requests

base_url = "https://www.worldcitydb.com/"


def parse_table_row(row):
    return row


def collect_all_cities_links(page):
    soup = BeautifulSoup(page.text, "html.parser")
    all_links = soup.findAll("a", class_="link")
    cities_links = []

    for link in all_links:
        cities_links.append(link["href"])
    return cities_links


def collect_regions_stats(region_link):
    page = requests.get(base_url + region_link)
    soup = BeautifulSoup(page.text, "html.parser")
    region_name = soup.find("h2").text
    region_name = region_name[(region_name.index("in ") + 3) :]
    region_links = collect_all_cities_links(page)
    print(region_links)


def collect_city_info(city_link):
    city_info = []
    url = base_url + city_link

    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    heading = soup.find("h1")
    [region, subergion] = [link.text for link in heading.findAll("a")][1:]

    table_country = soup.find("table", class_="table-country")
    name = table_country.find("a").text
    table_rows = table_country.find_all("tr")

    city_info = [name, region, subergion]

    for row in table_rows:
        if not table_rows.index(row):
            continue
        info = row.findAll("td")[1].text
        city_info.append(info)

    striped_table = soup.find("table", class_="table-country table-striped")

    striped_table_rows = striped_table.findAll("tr")

    for row in striped_table_rows:
        cells = row.findAll("td")
        city_info.append(cells[1].text)
        city_info.append(cells[3].text)

    city_regions_links = collect_all_cities_links(page)
    collect_regions_stats(city_regions_links[0])
