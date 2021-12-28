from aiogram.dispatcher.filters.state import StatesGroup, State


class OperAccept(StatesGroup):
    inwork = State()
    waiting = State()

class ModerAccept(StatesGroup):
    inwork = State()
    waiting = State()
