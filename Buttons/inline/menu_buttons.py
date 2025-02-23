from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


buttons = ["Мои отпуска🌴","Добавить отпуск🏝️","Удалить отпуск🚫","Добавить участника👥","Удалить участника"]
datas = ["id1","id2","id3","id4","id5"]

main_menu = InlineKeyboardBuilder(

)




for idx,button in enumerate(buttons):

    main_menu.add(InlineKeyboardButton(text=button, callback_data=datas[idx]))

main_menu.adjust(2)


def cancel_button():
    keyboard = InlineKeyboardBuilder()

    kb= InlineKeyboardButton(text="Отмена", callback_data="cancel")
    keyboard.add(kb)
    return keyboard.as_markup()