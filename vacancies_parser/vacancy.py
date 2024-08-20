# MyProject - A telegram bot for finding jod in Slovakia.
# © 2024 Yehor Demenchuk. All rights reserved.
# Contact: demenchuk1210m@gmail.com
# This code is provided "as is", without warranty of any kind.

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

first_vacancy = Vacancy("IT", "MICROSOFT", None, "1234", "Slovensko")

second_vacancy = Vacancy("IT", "Microsoft", None, "1234", "Slovensko")

print(first_vacancy == second_vacancy)
    