# MyProject - A telegram bot for finding jod in Slovakia.
# © 2024 Yehor Demenchuk. All rights reserved.
# Contact: demenchuk1210m@gmail.com
# This code is provided "as is", without warranty of any kind.

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_keyboard = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='hladať')]], resize_keyboard=True)