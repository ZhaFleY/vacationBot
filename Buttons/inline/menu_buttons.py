from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


buttons = ["Мои отпуска🌴","Добавить отпуск🏝️","Удалить отпуск🚫","Добавить участника👥"]


main_menu = InlineKeyboardBuilder(

)




for button in buttons:
    main_menu.add(InlineKeyboardButton(text=button, callback_data=button))

main_menu.adjust(2)
