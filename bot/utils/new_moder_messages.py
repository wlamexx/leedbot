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
    from keyboards.inline.moder import moderator_menu
    from states.application import ModerAccept


async def parse_moders():
    applications = [x for x in db.get_collection(db.moder_queue)]
    application = None
    shield = "{0}\nЗаявка №{1}\nИсточник №{2}\n‼️‼️‼️‼️‼️\nтел. {3}\n\nФИО: {4}\n\n{5}\n\n"
    while True:
        while applications == []:
            applications = [x for x in db.get_collection(db.moder_queue)]
        for appl in applications:
            if not appl['inwork']:
                application = appl
                break
            else:
                continue
            break
        try:
            data = get_data(application["message"])
            waiting_moder = None
            waiting_moders = [x for x in db.get_collection(db.waiting_moders)]
            if waiting_moders != []:
                waiting_moder = waiting_moders[0]
            if waiting_moder is not None:
                print(applications)
                print(waiting_moder)
                message = shield.format(data['city'],application['ids'],1,data['number'],data['name'],data['question'])
                state = FSMContext(storage, waiting_moder['chat_id'], waiting_moder['id'])
                application['inwork'] = True

                await state.update_data(recv=application)
                await dp.bot.send_message(chat_id=waiting_moder['chat_id'], text=message, reply_markup=moderator_menu)
                db.delete(db.waiting_moders, waiting_moder)
                applications.remove(application)
                db.delete(db.moder_queue, application)
        except CantParseEntities:
            db.delete(db.moder_queue,application)
            applications.remove(application)



asyncio.run(parse_moders())