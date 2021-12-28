import sys
import asyncio
from aiogram.utils.exceptions import CantParseEntities
from misc.formatm import get_data
from aiogram.dispatcher.storage import FSMContext
try:
    from loader import dp, db
except:
    sys.path.append(sys.path[0].replace('/bot/utils', ''))
    sys.path.append(sys.path[0].replace('/utils', ''))
    from bot.loader import dp, db, storage
    from keyboards.inline.oper import operator_menu
    from states.application import OperAccept


async def parse_opers():
    applications = [x for x in db.get_collection(db.oper_queue)]
    application = None
    shield = "{0}\nЗаявка №{1}\nИсточник №{2}\n‼️‼️‼️‼️‼️\nтел. {3}\n\nФИО: {4}\n\n{5}\n\n"
    while True:
        while applications == []:
            applications = [x for x in db.get_collection(db.oper_queue)]
        for appl in applications:
            if not appl['inwork']:
                application = appl
                break
            else:
                continue
            break
        try:
            data = get_data(application["message"])
            waiting_oper = None
            waiting_opers = [x for x in db.get_collection(db.waiting_operators)]
            if waiting_opers != []:
                waiting_oper = waiting_opers[0]
            if waiting_oper is not None:
                print(applications)
                message = shield.format(data['city'],application['ids'],1,data['number'],data['name'],data['question'])
                state = FSMContext(storage, waiting_oper['chat_id'], waiting_oper['id'])
                application['inwork'] = True

                await state.update_data(recv=application)
                await dp.bot.send_message(chat_id=waiting_oper['chat_id'], text=message, reply_markup=operator_menu)
                db.delete(db.waiting_operators, waiting_oper)
                applications.remove(application)
                db.delete(db.oper_queue, application)
        except CantParseEntities:
            db.delete(db.oper_queue,application)
            applications.remove(application)



asyncio.run(parse_opers())