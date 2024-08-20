# MyProject - A telegram bot for finding jod in Slovakia.
# © 2024 Yehor Demenchuk. All rights reserved.
# Contact: demenchuk1210m@gmail.com
# This code is provided "as is", without warranty of any kind.

import requests
from bs4 import BeautifulSoup, Tag
from vacancy import Vacancy

PROFESIA_SK_URL = "https://www.profesia.sk/praca/"

KARIERA_SK_URL = "https://kariera.zoznam.sk/pracovne-ponuky/za-1-den"

BRIGADA_SK_URL = "https://www.brigada.sk/brigady-na-slovensku"

def get_url(base_url: str, page: int) -> str:
    page_part =  (
        f"page_num={page}" if base_url == PROFESIA_SK_URL else
        f"od={(page - 1) * 30}" if base_url == KARIERA_SK_URL else
        f"page={page}#google_vignette"
    )
  
    return base_url + "?" + page_part

def get_not_parsed_vacancies(headers: dict, base_url: str) -> list:
    not_parsed_vacancies = []

    page = 1

    vacancy_tag_name = "li" if base_url == PROFESIA_SK_URL else "div"

    vacancy_html_class = "list-row" if base_url == PROFESIA_SK_URL else "offer" if base_url == KARIERA_SK_URL else "url"

    while True:
        url = get_url(base_url, page)

        r = requests.get(url=url, headers=headers)

        soup = BeautifulSoup(r.text, "lxml")

        found_vacancies = list(soup.find_all(vacancy_tag_name, class_=vacancy_html_class))

        if not found_vacancies or page == 24 and base_url != PROFESIA_SK_URL:
            break

        not_parsed_vacancies += found_vacancies

        page += 1

    return not_parsed_vacancies

def get_vacancy_tags(not_parsed_vacancy: Tag, base_url: str) -> list:
    title_tag = (
        not_parsed_vacancy.find('h2').find('a') if base_url == PROFESIA_SK_URL else
        not_parsed_vacancy.find('h2', class_='offer-title') if base_url == KARIERA_SK_URL else
        not_parsed_vacancy.find('a')
    )

    link_tag = (
        None if not title_tag else
        title_tag if base_url != KARIERA_SK_URL else
        title_tag.find('a')
    )

    employer_tag = (
        not_parsed_vacancy.find('span', class_='employer') if base_url == PROFESIA_SK_URL else
        not_parsed_vacancy.find('div', class_='offer-employer') if base_url == KARIERA_SK_URL else
        None
    )

    location_tag = (
        not_parsed_vacancy.find('span', class_='job-location') if base_url == PROFESIA_SK_URL else
        not_parsed_vacancy.find('div', class_='offer-locality') if base_url == KARIERA_SK_URL else
        None
    )

    sallary_tag = (
        not_parsed_vacancy.find('span', class_='label label-bordered green half-margin-on-top') if base_url == PROFESIA_SK_URL else
        not_parsed_vacancy.find('ul', class_='offer-info').find('li') if base_url == KARIERA_SK_URL else
        None
    )

    return [title_tag, link_tag, employer_tag, sallary_tag, location_tag]

def get_parsed_vacancy(tags: list, base_url: str) -> Vacancy:
    title = tags[0].get_text(strip=True) if tags[0] else "Nemá mena"

    link_tag = tags[1]

    link_prefix = (
        None if not link_tag else
        "https://www.profesia.sk/" if base_url == PROFESIA_SK_URL else
        "https://kariera.zoznam.sk/" if base_url == KARIERA_SK_URL else
        BRIGADA_SK_URL
    )

    link = link_prefix + link_tag['href'] if link_tag else "Nemá odkazu"

    employer = tags[2].get_text(strip=True) if tags[2] else "Nemá firmy"

    sallary = tags[3].get_text(strip=True) if tags[3] else "Nemá mzdy"

    location = tags[4].get_text(strip=True) if tags[4] else "Nemá lokacií"

    return Vacancy(title, employer, link, sallary, location)

def search_vacancies(base_url: str) -> list:
    headers = { 
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36" 
    }

    not_parsed_vacancies = get_not_parsed_vacancies(headers, base_url)

    parsed_vacancies = []

    for not_parsed_vacancy in not_parsed_vacancies:
        tags = get_vacancy_tags(not_parsed_vacancy, base_url)

        parsed_vacancies.append(get_parsed_vacancy(tags, base_url))
    
    return parsed_vacancies