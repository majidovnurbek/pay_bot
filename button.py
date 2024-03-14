    from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btn = [
    [KeyboardButton(text="Category"), KeyboardButton(text="Profile")],
    [KeyboardButton(text="Support"), KeyboardButton(text="Deposit")]

]
menu = ReplyKeyboardMarkup(keyboard=btn, resize_keyboard=True)

btnCat = [
    [KeyboardButton(text="Product 1"), KeyboardButton(text="Products 2")],
    [KeyboardButton(text="Product 3"), KeyboardButton(text="Products 4")],
    [KeyboardButton(text="⬅️Back⬅️")]

]

catMenu = ReplyKeyboardMarkup(keyboard=btnCat, resize_keyboard=True)

inlineBtn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Buy", callback_data="pay_1")]
])

catMenu2 = ReplyKeyboardMarkup(keyboard=btnCat, resize_keyboard=True)

inlineBtn2 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Buy", callback_data="pay_2")]
])

inlineBtn3 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Buy", callback_data="pay_3")]
])
inlineBtn4 = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Buy", callback_data="pay_4")]
])
