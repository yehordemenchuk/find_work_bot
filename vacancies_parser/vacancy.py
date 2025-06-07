# MyProject - A telegram bot for finding jod in Slovakia.
# © 2024 Yehor Demenchuk. All rights reserved.
# Contact: demenchuk1210m@gmail.com
# This code is provided "as is", without warranty of any kind.
import re
from vacancies_parser.redis_client import redis

def replace_diacritics(location_name: str):
    diacritics_table = {
        "ľ": "l", "š": "s", "č": "c", "ť": "t", "ľ": "l", "ž": "z", "ý": "y", "á": "a", "í": "i", "é": "e", "ú": "u", "ä": "a"
    }

    lowered_location_name = location_name
    
    for diacritic in diacritics_table:
        if diacritic in lowered_location_name:
            lowered_location_name = lowered_location_name.replace(diacritic, diacritics_table[diacritic])
    
    return lowered_location_name
class Vacancy:
    def __init__(self, title: str = None, employer: str = None, link: str = None, sallary: str = None, location: str = None):
        self._title = title

        self._employer = employer

        self._link = link

        self._sallary = sallary

        self._location = location
    
    def __eq__(self, other) -> bool:
        return (self._title == other._title and self._employer == other._employer and self._link == other._link and 
                self._sallary == other._sallary and self._location == other._location)

    def __str__(self) -> str:
        return f"{self._title}\nZamestnavateľ: {self._employer}\nMzda: {self._sallary}\nKde: {self._location}\nOdkaz: {self._link}" 

    def get_title(self) -> str: return self._title

    def get_employer(self) -> str: return self._employer

    def get_link(self) -> str: return self._link

    def get_sallary(self) -> str: return self._sallary

    def get_location(self) -> str: return self._location

    def meets_condtions(self, conditions: dict) -> bool:
        return (re.search(rf"({replace_diacritics(conditions["expected_name"])})", replace_diacritics(self._title)) 
                and re.search(r"\d+", self._sallary).group() <= conditions["expected_sallary"] 
                and re.search(rf"({replace_diacritics(conditions["expected_location"])})", replace_diacritics(self._location)))
    
    async def set_to_redis(self, vacancy_id: int):
        vacancy_info = {
                        "title": self._title,
                        "employer": self._employer,
                        "link": self._link,
                        "sallary": self._sallary,
                        "location": self._location
                       }

        await redis.hset(f"id:{vacancy_id}", mapping=vacancy_info)

        await redis.close()

    async def get_from_redis(self, vacancy_id: int):
        vacancy_info = await redis.hgetall(f"id:{vacancy_id}")

        await redis.close()

        self._title = vacancy_info[b"title"].decode()

        self._employer = vacancy_info[b"employer"].decode()

        self._link = vacancy_info[b"link"].decode()

        self._sallary = vacancy_info[b"sallary"].decode()

        self._location = vacancy_info[b"location"].decode()