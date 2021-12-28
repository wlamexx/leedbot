from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandPrivacy
from loader import dp, db
from keyboards.inline.oper import operator_menu, restart
from keyboards.inline.moder import moderator_menu
from states.application import OperAccept, ModerAccept
from aiogram.dispatcher.storage import FSMContext
from aiogram.utils.exceptions import CantParseEntities
from utils.misc.formatm import get_data
from data.config import OPERATORS, MODERATORS



@dp.message_handler(commands="get", state='*')
async def get(message: types.Message,  state: FSMContext, chat_id=0):
    if chat_id == 0:
        await message.answer("Вы начали работу, ожидайте заявок, для остановки введите /stop")
        if str(message.from_user.id) in OPERATORS:
            db.upload(db.waiting_operators, {'id':message.from_user.id, 'chat_id':message.chat.id})
            await OperAccept.inwork.set()
        elif str(message.from_user.id) in MODERATORS:
            db.upload(db.waiting_moders, {'id':message.from_user.id, 'chat_id':message.chat.id})
            await ModerAccept.inwork.set()
    elif str(chat_id) in OPERATORS:
        await dp.bot.send_message(chat_id, "Ожидайте новых заявок")
        db.upload(db.waiting_operators, {'id':chat_id, 'chat_id':chat_id})
        await OperAccept.inwork.set()
    elif str(message.from_user.id) in MODERATORS:
        await dp.bot.send_message(chat_id, "Ожидайте новых заявок")
        db.upload(db.waiting_moders, {'id':chat_id, 'chat_id':chat_id})
        await ModerAccept.inwork.set()
    else:
        print('ERROR')

@dp.callback_query_handler(state=ModerAccept.inwork)
async def opered(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    data = data.get("recv")
    if data is not None:
        data['status'] = call.data
        await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                       text="Вы ответили на заявку✅ Номер заявки: {0}".format(data['ids']),
                                       reply_markup=restart)
        if call.data == "yes":
            del data['inwork']
            db.upload(db.users, data)
            db.delete(db.moder_queue, data)
        elif call.data == "no":
            data['inwork'] = False
            db.upload(db.oper_queue, data)
            db.delete(db.moder_queue, data)
    else:
        await dp.bot.send_message(call.message.chat.id, "Ожидайте новых заявок")
        db.upload(db.waiting_moders, {'id':call.message.chat.id, 'chat_id':call.message.chat.id})
        await ModerAccept.inwork.set()


@dp.callback_query_handler(state=OperAccept.inwork)
async def opered(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    data = data.get("recv")
    await state.reset_data()
    if data is not None:
        data['status'] = call.data
        await dp.bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                       text="Вы ответили на заявку✅ Номер заявки: {0}".format(data['ids']),
                                       reply_markup=restart)
        if call.data == "Записан" or call.data == "Перезвон":
            db.upload(db.users, data)
            print(data['_id'])
            db.delete(db.oper_queue, data)
        elif call.data == "Брак" or call.data == "Недозвон":
            data['inwork'] = False
            db.upload(db.moder_queue, data)
            db.delete(db.oper_queue, data)
    else:
        await dp.bot.send_message(call.message.chat.id, "Ожидайте новых заявок")
        db.upload(db.waiting_operators, {'id':call.message.chat.id, 'chat_id':call.message.chat.id})
        await OperAccept.inwork.set()

@dp.callback_query_handler(lambda c: c.data=='restart', state='*')
async def reget(call: types.CallbackQuery, state: FSMContext):
    await get(call.message, state, chat_id=call.message.chat.id)


