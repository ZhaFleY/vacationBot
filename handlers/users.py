from aiogram import Router,F
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()

@router.message(CommandStart)
async def cmd_start(message: Message):
    await message.send_message(message.chat.id, message.text)