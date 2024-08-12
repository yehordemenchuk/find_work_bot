# MyProject - A telegram bot for finding jod in Slovakia.
# © 2024 Yehor Demenchuk. All rights reserved.
# Contact: demenchuk1210m@gmail.com
# This code is provided "as is", without warranty of any kind.

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

router = Router()

@router.message(CommandStart)
async def cmd_start(message: Message):
    await message.answer("Ahoj! 👋 Som PracaSK bot, váš spoľahlivý sprievodca pri hľadaní voľných pracovných miest na Slovensku.\nPomôžem vám rýchlo a jednoducho nájsť tie najlepšie ponuky práce, ktoré zodpovedajú vašim kritériám. \n\nPoužite príkaz /search pre hľadanie.")