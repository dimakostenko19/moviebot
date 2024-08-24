from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

first_channel = InlineKeyboardButton(
    text="ПОДПИСАТЬСЯ",
    url="https://t.me/test_sub_01"
)

check_sub = InlineKeyboardButton(
    text="Проверить подписку",
    callback_data="check_sub"
)
row1 = [first_channel]
row2 = [check_sub]
rows = [row1, row2]

markup_sub = InlineKeyboardMarkup(inline_keyboard=rows)