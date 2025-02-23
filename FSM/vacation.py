import re
from datetime import datetime, timedelta
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from sqlalchemy.exc import NoResultFound
from sqlalchemy.testing.suite.test_reflection import users

from DataBase.connect_database import Session_local
from DataBase.db_models import Employers, Employers_Vacations
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from Buttons.inline.menu_buttons import cancel_button

router = Router()

class AddVacation(StatesGroup):
    load_start_vacation = State()
    load_end_vacation = State()

# Функция для проверки формата даты
def validate_date(date_str):
    pattern = r"^\d{2}\.\d{2}\.\d{4}$"
    if not re.match(pattern, date_str):
        return False
    try:
        datetime.strptime(date_str, "%d.%m.%Y")
        return True
    except ValueError:
        return False

@router.callback_query(F.data == "id2")
async def id2(callback_query: CallbackQuery, state: FSMContext):
    session = Session_local()
    try:
        user_id = str(callback_query.from_user.id)
        check = session.query(Employers).filter(Employers.telegram_id == user_id).first()
        if not check:
            await state.clear()
            return await callback_query.message.answer(text="Отказано в доступе!")

        await callback_query.message.answer(
            text="Введите начало вашего отпуска в формате (11.02.2025)",
            reply_markup=cancel_button()
        )
        await state.set_state(AddVacation.load_start_vacation)
    except Exception as e:
        print(e)
        await state.clear()
        await callback_query.message.answer(text="Ошибка в базе данных")
    finally:
        session.close()

@router.message(AddVacation.load_start_vacation)
async def load_start_vacation(message: Message, state: FSMContext):
    start_date = message.text.strip()

    # Проверка на корректный формат даты
    if not validate_date(start_date):
        await message.answer("Неверный формат даты! Введите в формате (дд.мм.гггг), например: 11.02.2025")
        return

    await state.update_data(start=start_date)
    await message.answer("Введите конец вашего отпуска в формате (11.02.2025)")
    await state.set_state(AddVacation.load_end_vacation)

@router.message(AddVacation.load_end_vacation)
async def load_end_vacation(message: Message, state: FSMContext):
    session = Session_local()
    data = await state.get_data()
    start_str = data.get("start")
    end_str = message.text.strip()

    # Проверка на корректный формат даты
    if not validate_date(end_str):
        await message.answer("Неверный формат даты! Введите в формате (дд.мм.гггг), например: 11.02.2025")
        return

    start_date = datetime.strptime(start_str, "%d.%m.%Y")
    end_date = datetime.strptime(end_str, "%d.%m.%Y")

    # Проверка, что дата окончания отпуска не раньше даты начала
    if end_date < start_date:
        await message.answer("Ошибка! Дата окончания отпуска не может быть раньше даты начала. Введите заново.")
        return

    # Проверка, что отпуск не превышает 28 дней
    max_vacation_length = timedelta(days=28)
    if end_date - start_date > max_vacation_length:
        await message.answer("Ошибка! Максимальная длина отпуска — 28 дней. Введите другую дату окончания.")
        return

    try:
        user = session.query(Employers).filter(Employers.telegram_id == str(message.from_user.id)).first()
        user_id = user.id
        user_name = user.name
        new_vac = Employers_Vacations(
            id = user_id,
            name = user.name,
            start_vac = start_date,
            end_vac = end_date,
            telegram_id = str(message.from_user.id),
        )
        session.add(new_vac)
        session.commit()
        session.close()
        await message.answer(f"Ваш отпуск записан: с {start_str} по {end_str}.")
        await state.clear()
    except Exception as e:
        print(e)
        await message.answer(text="Произошла неизветная ошибка")
        await state.clear()
