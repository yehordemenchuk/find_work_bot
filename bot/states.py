# MyProject - A telegram bot for finding jod in Slovakia.
# © 2024 Yehor Demenchuk. All rights reserved.
# Contact: demenchuk1210m@gmail.com
# This code is provided "as is", without warranty of any kind.

from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class Conditions(StatesGroup):
    expected_name = State()
    expected_sallary = State()
    expected_location = State()