from aiogram import types
from states.application import OperAccept
from aiogram.dispatcher.storage import FSMContext
from loader import dp

@dp.message_handler(commands="stop", state='*')
async def get(message: types.Message, state:FSMContext):
    await message.answer("Вы отлично поработали!")
    await state.finish()