from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


operator_menu = InlineKeyboardMarkup(row_width=2,
                                    inline_keyboard=[
                                        [
                                            InlineKeyboardButton(text='Записан', callback_data='Записан')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Брак', callback_data='Брак')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Недозвон', callback_data='Недозвон')
                                        ],
                                        [
                                            InlineKeyboardButton(text='Перезвон', callback_data='Перезвон')
                                        ]
                                    ])

restart = InlineKeyboardMarkup(inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Получить еще', callback_data='restart')
                                    ]
                                ])