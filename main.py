import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message, user
from aiogram.filters.command import CommandStart
from root import Token
from button import *
from Payments import *
from db import Database

db = Database("database.db")
import os

dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    db.add_users(message.from_user.id, message.from_user.full_name)
    # a = os.getenv(db.get_all_users())
    # # a = db.get_all_users()
    # await message.answer(f"{a.count()} ")
    await message.answer("Hello", reply_markup=menu)
    await message.answer("salom Damir")
    await message.answer("salom damir")
    await message.answer("salom nurbek")


@dp.message(F.text == "Category")
async def category(message: Message):
    await message.answer("Choose", reply_markup=catMenu)


@dp.message(F.text == "Product 1")
async def product_1(message: Message):
    await message.answer_photo(photo="https://images.uzum.uz/ck9sgvbk9fq1var6o9h0/original.jpg",
                               caption="Iphone 14 Pro Max\n"
                                       "Battery Level: 100%\n", reply_markup=inlineBtn)


dp.callback_query.register(order_1, F.data == "pay_1")
dp.pre_checkout_query.register(pre_checkout_query)
dp.message.register(successful_payment, F.successful_payment)


########################################################################################
@dp.message(F.text == "⬅️Back⬅️")
async def back(message: Message):
    await message.answer("choose", reply_markup=menu)


###########################################################################################
@dp.message(F.text == "Products 2")
async def product_1(message: Message):
    await message.answer_photo(photo="https://i.ytimg.com/vi/OEFsVK7A7R0/maxresdefault.jpg",
                               caption="Macbook air M3\nPrice:30 000 000"
                                       "\nBattery Level: 100%\n", reply_markup=inlineBtn2)


dp.callback_query.register(order_2, F.data == "pay_2")
dp.pre_checkout_query.register(pre_checkout_querys)
dp.message.register(successful_payments, F.successful_payment)


###########################################################################################
@dp.message(F.text == "Product 3")
async def product_1(message: Message):
    await message.answer_photo(
        photo="https://assets.asaxiy.uz/product/items/desktop/d4c2e4a3297fe25a71d030b67eb83bfc2023092315141223825BJDBz9NaNi.png.webp",
        caption="Ihone 15 pro max\nPrice:15 000 000"
                "\nBattery Level: 100%", reply_markup=inlineBtn3)


dp.callback_query.register(order_3, F.data == "pay_3")
dp.pre_checkout_query.register(pre_checkout_query_3)
dp.message.register(successful_payment_3, F.successful_payment)


##############################################################################################
@dp.message(F.text == "Products 4")
async def product_1(message: Message):
    await message.answer_photo(
        photo="https://imageio.forbes.com/specials-images/imageserve/5fbab8d308c94ab54adca19a/0x0.jpg?format=jpg&height=900&width=1600&fit=bounds",
        caption="Ipad air 2023\nPrice:15 000 000"
                "\nBattery Level: 100%", reply_markup=inlineBtn4)


dp.callback_query.register(order_4, F.data == "pay_4")
dp.pre_checkout_query.register(pre_checkout_query_4)
dp.message.register(successful_payment_4, F.successful_payment)


#############################################################################################



async def main() -> None:
    bot = Bot(token=Token)
    await dp.start_polling(bot)



if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
