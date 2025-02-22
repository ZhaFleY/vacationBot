from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


buttons = ["Мои отпуска🌴","Добавить отпуск🏝️","Удалить отпуск🚫","Добавить участника👥"]
datas = ["id1","id2","id3","id4"]

main_menu = InlineKeyboardBuilder(

)




for idx,button in enumerate(buttons):

    main_menu.add(InlineKeyboardButton(text=button, callback_data=datas[idx]))

main_menu.adjust(2)
