from aiogram import Router,F
from aiogram.filters import CommandStart
from aiogram.types import Message, InlineQuery, CallbackQuery
from Buttons.inline.menu_buttons import main_menu
from DataBase.connect_database import  Session_local

#Инициализация классов
router = Router()
session = Session_local()





@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(text="Менеджер отпусков компании ОнИн🌴",reply_markup=main_menu.as_markup())



@router.callback_query(F.data=="id1")
async def get_vac(cb: CallbackQuery):
    print(1111)
    await cb.message.answer(text="Ваши отпуска")



@router.callback_query(F.data == "id2")
async def add_vac(cb: CallbackQuery):
    pass



