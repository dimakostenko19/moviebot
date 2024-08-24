from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types.input_file import FSInputFile

import keyboards.admin_keyboard as akb
import data.db as db
from config import Admin_ID

import os


router = Router()

class Admin(StatesGroup):
    auth = State()
    send_mess = State()
    add_film = State()
    del_film = State()
    upd_old_film = State()
    upd_new_code = State()

# Admin menu
@router.message(Command("admin"))
async def admin_command(message: types.Message, state: FSMContext):
    if(message.from_user.id == Admin_ID):
        await message.answer(
            text="Админ меню",
            reply_markup=akb.markup_admin
            )
        await state.set_state(Admin.auth)

# Рассылка
@router.callback_query(F.data=="spam")
async def spam(call: types.callback_query, state: FSMContext):
    await call.message.edit_text(
        text="Отправьте пост 📷"
    )
    await state.set_state(Admin.send_mess)

@router.message(StateFilter(Admin.send_mess))
async def get_post(message: types.Message, state: FSMContext):
    from main import bot

    await state.update_data(caption_spam=message.caption, path="E:\\DimaPy\\kino_bot\\photo\\1.png")
    path = "E:\\DimaPy\\kino_bot\\photo\\1.png"
    file_id = message.photo[-1].file_id
    
    await bot.download(file=file_id, destination=path)

    await message.answer_photo(
        photo=FSInputFile(path),
        caption=message.caption,
        reply_markup=akb.markup_spam
        )

@router.callback_query(F.data=="send_spam")
async def send_spam(call: types.callback_query, state: FSMContext):
    from main import bot

    data = await state.get_data()
    caption = data.get("caption_spam")
    path = data.get("path")

    with open("chat_id.txt", "r") as f:
        for i in range(1):
            chat = f.readline().strip()
            chat_id = int(chat)
            await bot.send_photo(
                chat_id=chat_id,
                photo=FSInputFile(path),
                caption=caption
                )
    os.remove(path)
    
    await call.message.delete()
    await call.message.answer(
        text="Админ меню",
        reply_markup=akb.markup_admin
    )
# Назад к меню
@router.callback_query(F.data=="back")
async def back_to_menu(call: types.callback_query):
    await call.message.delete()
    await call.message.answer(
        text="Админ меню",
        reply_markup=akb.markup_admin
    )


# Добавление фильма
@router.callback_query(F.data=="add_film")
async def create_film(call: types.callback_query, state: FSMContext):
    await call.message.edit_text(
        text="""Введите код и название фильма через двоеточие
<i>Пример: 127:Мстители</i>
""",
        reply_markup=akb.markup_back
    )
    await state.set_state(Admin.add_film)

@router.message(StateFilter(Admin.add_film))
async def get_name(message: types.Message, state: FSMContext):
    data = message.text
    arr = data.split(":")
    await db.add_film(films_code=int(arr[0]), films_name=arr[1])
    await message.answer(
        text="Админ меню",
        reply_markup=akb.markup_admin
    )

# Список фильмов
@router.callback_query(F.data=="list")
async def show_all(call: types.callback_query, state: FSMContext):
    films = await db.get_Allfilms()
    res = "Список фильмов\n\n"
    for film in films:
        res += f"Код: {film[0]} Название: {film[1]}\n"
    
    await call.message.edit_text(
        text=res,
        reply_markup=akb.markup_back
    )


# Удаление фильма
@router.callback_query(F.data=="del_film")
async def delete_film(call: types.callback_query, state: FSMContext):
    await call.message.answer(
        text="Введите код фильма"
    )
    await state.set_state(Admin.del_film)

@router.message(StateFilter(Admin.del_film))
async def del_by_code(message: types.Message, state: FSMContext):
    await db.delete_film(int(message.text))
    
    await message.answer(
        text="Админ меню",
        reply_markup=akb.markup_admin
    )

# Обновление фильма
@router.callback_query(F.data=="update_film")
async def update_film(call: types.callback_query, state: FSMContext):
    await call.message.answer(
        text="""Введите старый_код:новый_код:название
<i>Пример: 123:245:Мстители</i>"""
    )
    await state.set_state(Admin.upd_old_film)

@router.message(StateFilter(Admin.upd_old_film))
async def old_film_code(message: types.Message, state: FSMContext):
    data = message.text
    
    arr = data.split(":")
    
    old_code = int(arr[0])
    new_code = int(arr[1])
    new_name = arr[2]

    await db.update_film(code=old_code, new_code=new_code, name=new_name)
    await message.answer(
        text="Админ меню",
        reply_markup=akb.markup_admin
    )

    