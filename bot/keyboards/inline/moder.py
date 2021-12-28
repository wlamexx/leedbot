from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


moderator_menu = InlineKeyboardMarkup(row_width=2,
                                      inline_keyboard=[
                                          [
                                              InlineKeyboardButton(text='Подтвердить', callback_data='yes')
                                          ],
                                          [
                                              InlineKeyboardButton(text='Отменить', callback_data='no')
                                          ]
                                      ])