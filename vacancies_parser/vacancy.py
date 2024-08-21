# MyProject - A telegram bot for finding jod in Slovakia.
# © 2024 Yehor Demenchuk. All rights reserved.
# Contact: demenchuk1210m@gmail.com
# This code is provided "as is", without warranty of any kind.
import re

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
    def __init__(self, title: str, employer: str, link: str, sallary: str, location: str):
        self._title = title

        self._employer = employer

        self._link = link

        self._sallary = sallary

        self._location = location
    
    def __eq__(self, other) -> bool:
        return (self._title == other._title and self._employer == other._employer and self._link == other._link and 
                self._sallary == other._sallary and self._location == other._location)

    def __str__(self) -> str:
        return f"{self._title}\nZamestnavateľ: {self._employer}\nMzda: {self._sallary}\nKde: {self._location}\nOdkaz: {self}" 

    def get_title(self) -> str: return self._title

    def get_employer(self) -> str: return self._employer

    def get_link(self) -> str: return self._link

    def get_sallary(self) -> str: return self._sallary

    def get_location(self) -> str: return self._location

    def meets_condtions(self, conditions: dict) -> bool:
        return (re.search(rf"({replace_diacritics(conditions["expected_name"])})", replace_diacritics(self._title)) 
                and re.search(r"\d+", self._sallary).group() <= conditions["expected_sallary"] 
                and re.search(rf"({replace_diacritics(conditions["expected_location"])})", replace_diacritics(self._location)))
    
    def covert_to_dict(self) -> dict:
        return {
                "title": self._title,
                "employer": self._employer,
                "link": self._link,
                "sallary": self._sallary,
                "location": self._location
               }