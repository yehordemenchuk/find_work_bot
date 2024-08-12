# MyProject - A telegram bot for finding jod in Slovakia.
# © 2024 Yehor Demenchuk. All rights reserved.
# Contact: demenchuk1210m@gmail.com
# 
# This code is provided "as is", without warranty of any kind.

from vacancy import Vacancy

new_vacancy = Vacancy(123, "Programator", "Praca v IT", 567, "Kosice")

print(str(new_vacancy))