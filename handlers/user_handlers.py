from aiogram import Router, types, F
from aiogram.filters.command import Command
from aiogram.filters import StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from main import bot
import keyboards.keyboard as kb
import data.db as db

router = Router()

class Start(StatesGroup):
    search = State()


@router.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        text="💬 Для доступа к боту, подпишись на наши телеграм каналы:",
        reply_markup=kb.markup_sub
    )
    with open("chat_id.txt", "a") as f:
        f.write(str(message.chat.id)+"\n")

@router.callback_query(F.data=="check_sub")
async def check_subscribe(call: types.callback_query, state: FSMContext):
    member = await bot.get_chat_member(chat_id="@test_sub_01", user_id=call.from_user.id)
    if (member.status in ["member", "administrator", "creator"]):
        await call.message.answer(
            text="""У вас все получилось🎉
Введите код фильма"""
        )
    else:
        await call.message.answer(
            text="Вы не подписаны"
        )
    await state.set_state(Start.search)

@router.message(StateFilter(Start.search))
async def search(message: types.Message, state: FSMContext):
    code = int(message.text)
    film = await db.get_films(code=code)
    
    if film:
        if(film[0][0]==code):
            await message.answer(film[0][1])
        else:
            await message.answer("""Фмльма с таким кодом нет
Повторите попытку""")
    else:
            await message.answer("""Фмльма с таким кодом нет
Повторите попытку""")