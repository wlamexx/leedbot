from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.mongo import MongoStorage
from data import config
import sys
try:
    from dbapi.dbapi import DatabaseAPI
except:
    sys.path.append(sys.path[0].replace('/bot', ''))
    from dbapi.dbapi import DatabaseAPI

db = DatabaseAPI()
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
storage = MongoStorage(uri="mongodb+srv://shodan:ssyYvLdkXKqMRoph@cluster0.jqvnr.mongodb.net/fsm?retryWrites=true&w=majority",)
dp = Dispatcher(bot, storage=storage)


