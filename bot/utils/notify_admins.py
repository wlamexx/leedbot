import logging
import sys

from aiogram import Dispatcher
sys.path.append(sys.path[-1]+'/bot')
print(sys.path)
from data.config import ADMINS


async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)
