from aiogram import Router,F
from aiogram.filters import CommandStart
from aiogram.types import Message
from Buttons.inline.menu_buttons import main_menu
router = Router()

@router.message(CommandStart)
async def cmd_start(message: Message):
    await message.answer(text="Менеджер отпусков компании ОнИн🌴",reply_markup=main_menu.as_markup())


