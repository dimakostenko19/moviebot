from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.client.bot import DefaultBotProperties

import asyncio
import logging

from handlers import user_handlers, admin_handlers
from config import TOKEN


dp = Dispatcher()

bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML)
    )

async def main():
    logging.basicConfig(level=logging.INFO)

    dp.include_router(user_handlers.router)
    dp.include_router(admin_handlers.router)
    
    await dp.start_polling(bot)

if __name__=="__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")