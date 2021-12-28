from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.inline.oper import operator_menu
from loader import dp
from states.application import OperAccept
from data.config import MODERATORS, OPERATORS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, state='*'):
    if str(message.from_user.id) in OPERATORS:
        await message.answer(f"Привет, {message.from_user.full_name}! Для получения заявок используй команду /get")
    elif str(message.from_user.id) in MODERATORS:
        await message.answer(f"Привет, {message.from_user.full_name}! Для модерации заявок используй команду /get")

