from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

spam = InlineKeyboardButton(
    text="Сделать рассылку 📫",
    callback_data="spam"
)
add_film = InlineKeyboardButton(
    text="Добавить фильм 📌",
    callback_data="add_film"
)
delete_film = InlineKeyboardButton(
    text="Удалить фильм 🗑",
    callback_data="del_film"
)
list_film = InlineKeyboardButton(
    text="Список фильмов 🗒",
    callback_data="list"
)
update = InlineKeyboardButton(
    text="Обновить фильм 🔄",
    callback_data="update_film"
)

row1 = [spam]
row2 = [add_film, delete_film]
row3 = [update]
row4 = [list_film]

rows = [row1, row2, row3, row4]

markup_admin = InlineKeyboardMarkup(inline_keyboard=rows)


send = InlineKeyboardButton(
    text="Отправить пост",
    callback_data="send_spam"
)
back = InlineKeyboardButton(
    text="Назад 🔙",
    callback_data="back"
)
row1 = [send]
row2 = [back]
rows = [row1, row2]

markup_spam = InlineKeyboardMarkup(inline_keyboard=rows)


back = InlineKeyboardButton(
    text="Назад 🔙",
    callback_data="back"
)
row = [back]
rows = [row]
markup_back = InlineKeyboardMarkup(inline_keyboard=rows)
