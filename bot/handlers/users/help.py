from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message, state='*'):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            '/get - Начать работу',
            '/stop - Закончить работу')

    await message.answer("\n".join(text))
