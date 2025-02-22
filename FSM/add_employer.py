from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from DataBase.connect_database import Session_local
from DataBase.db_models import Employers
from aiogram import Router
from aiogram import F
from aiogram.types import Message, CallbackQuery
from Buttons.inline.menu_buttons import cancel_button
import random

session = Session_local()
router = Router()

class LoadEmployer(StatesGroup):
    load_name = State()
    load_lastname = State()
    load_tg_id = State()

@router.callback_query(F.data == "id4")
async def start_load_employer(cb: CallbackQuery, state: FSMContext):
    await cb.message.answer("Введите имя сотрудника:", reply_markup=cancel_button())
    await state.set_state(LoadEmployer.load_name)


@router.message(LoadEmployer.load_name)
async def get_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Теперь введите фамилию сотрудника:", reply_markup=cancel_button())
    await state.set_state(LoadEmployer.load_lastname)


@router.message(LoadEmployer.load_lastname)
async def get_lastname(message: Message, state: FSMContext):
    await state.update_data(lastname=message.text)
    await message.answer("Теперь введите Telegram ID сотрудника:", reply_markup=cancel_button())
    await state.set_state(LoadEmployer.load_tg_id)

@router.message(LoadEmployer.load_tg_id)
async def get_tg_id(message: Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("❌ Ошибка: ID должен содержать только цифры. Попробуйте снова.")
        return

    data = await state.get_data()
    new_employer = Employers(
        id=random.randint(100000, 999999),
        name=data["name"],
        last_name=data["lastname"],
        telegram_id=str(message.text)
    )
    session.add(new_employer)
    session.commit()

    await message.answer("✅ Сотрудник успешно добавлен в базу!")
    await state.clear()
@router.callback_query(F.data == "cancel")
async def cancel(cb: CallbackQuery, state: FSMContext):
    await state.clear()
    await cb.message.answer(text="Произведена отмена")