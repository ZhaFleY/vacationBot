from aiogram import Bot,Router,F,Dispatcher
import asyncio
from env_admin import token
from aiogram.filters import Command,CommandStart
from aiogram.types import Message
import logging

logging.basicConfig(level=logging.INFO)
async def main():
    bot = Bot(token=token)
    dp = Dispatcher()


    await dp.start_polling(bot)





if __name__ == '__main__':
    asyncio.run(main())
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

