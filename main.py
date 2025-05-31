from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
import asyncio

from config import TOKEN
from handlers import user, admin
from db import init_db


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    init_db()
    dp.include_routers(user.router, admin.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await bot.set_my_commands([
        BotCommand(command="start", description="Botni boshlash"),
        BotCommand(command="natijalar", description="Ovozlar natijasi (admin)"),
    ])
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())