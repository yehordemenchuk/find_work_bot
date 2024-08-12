# MyProject - A telegram bot for finding jod in Slovakia.
# © 2024 Yehor Demenchuk. All rights reserved.
# Contact: demenchuk1210m@gmail.com
# This code is provided "as is", without warranty of any kind.

import asyncio
from aiogram import Bot, Dispatcher
from bot.config import TOKEN
from bot.handlers import router

bot = Bot(TOKEN)
dp = Dispatcher()

async def main():
    try:
        dp.include_router(router)
        await dp.start_polling(bot)
    
    except KeyboardInterrupt:
        print('Bot was interrupted by host.')

    except:
        print('ERROR.')

if __name__ == "__main__":
    asyncio.run(main())