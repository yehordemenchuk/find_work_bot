class Vacancy:
    def __init__(self, id, name, description, sallary, location):
        self._id = id

        self._name = name

        self._description = description

        self._sallary = sallary

        self._location = location

    def get_id(self) -> int: return self._id    

    def get_name(self) -> str: return self._name

    def get_descrption(self) -> str: return self._description

    def get_sallary(self) -> int: return self._sallary

    def get_location(self) -> str: return self._location

    def __str__(self) -> str:
        return f"{self._name}\nPopis: {self._description}\nMzda: {self._sallary}\nKde: {self._location}"
    




