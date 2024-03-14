from aiogram import Bot, types
from aiogram.types import LabeledPrice, PreCheckoutQuery
from root import pay_token

channel = -1002114845403


async def order_1(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="iPhone 14 Pro",
                           description="iPhone 14 Pro max 256GB Deep Purple ",
                           provider_token=pay_token,
                           currency='UZS',
                           photo_url="https://images.uzum.uz/ck9sgvbk9fq1var6o9h0/original.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=160_000_00),
                               LabeledPrice(label="QQS", amount=19_200_00),
                               LabeledPrice(label="Skidka", amount=-30_200_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Iphone 14 Pro',
                           request_timeout=15
                           )


async def pre_checkout_query(pre_checkout_query: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


async def successful_payment(message: types.Message, bot: Bot):
    msg = f"""
    Payment Done ✅ 
    Product name : {message.successful_payment.invoice_payload}
    Price: {message.successful_payment.total_amount // 100} {message.successful_payment.currency} 💸
    Status Done :  ✅ 
    """

    await message.answer(msg)
    await bot.send_message(chat_id=channel, text=msg)


###############################################################################################
async def order_2(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Macbook air M3\nPrice:30 000 000",
                           description="Macbook air M3 1tb xotira",
                           provider_token=pay_token,
                           currency='UZS',
                           photo_url="https://i.ytimg.com/vi/OEFsVK7A7R0/maxresdefault.jpg",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=30_000_000_00),
                               LabeledPrice(label="QQS", amount=19_200_00),
                               LabeledPrice(label="Skidka", amount=-30_200_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='acbook air M3',
                           request_timeout=15
                           )


async def pre_checkout_querys(pre_checkout_querys: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_querys.id, ok=True)


async def successful_payments(message: types.Message, bot: Bot):
    msg2 = f"""
    Payment Done ✅ 2 product
    Product name : {message.successful_payments.invoice_payload}
    Price: {message.successful_payments.total_amount // 100} {message.successful_payments.currency} 💸
    Status Done :  ✅ 
    """

    await message.answer(msg2)
    await bot.send_message(chat_id=channel, text=msg2)


########################################################################################################
async def order_3(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="iPhone 15 Pro max",
                           description="iPhone 15 Pro max 512GB Deep Purple ",
                           provider_token=pay_token,
                           currency='UZS',
                           photo_url="https://store.storeimages.cdn-apple.com/4668/as-images.apple.com/is/iphone-15-pro-finish-select-202309-6-1inch_GEO_EMEA?wid=5120&hei=2880&fmt=p-jpg&qlt=80&.v=1693009279096",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=15_000_000_00),
                               LabeledPrice(label="QQS", amount=19_200_00),
                               LabeledPrice(label="Skidka", amount=-30_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Iphone 15 Pro max',
                           request_timeout=15
                           )


async def pre_checkout_query_3(pre_checkout_query_3: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query_3.id, ok=True)


async def successful_payment_3(message: types.Message, bot: Bot):
    msg = f"""
    Payment Done ✅ 
    Product name : {message.successful_payment_3.invoice_payload}
    Price: {message.successful_payment_3.total_amount // 100} {message.successful_payment_3.currency} 💸
    Status Done :  ✅ 
    """

    await message.answer(msg)
    await bot.send_message(chat_id=channel, text=msg)

########################################################################################################
async def order_4(call: types.CallbackQuery, bot: Bot):
    await bot.send_invoice(call.from_user.id,
                           title="Ipad air 2023",
                           description="Ipad air 2023 256gb Deep Purple ",
                           provider_token=pay_token,
                           currency='UZS',
                           photo_url="https://store.storeimages.cdn-apple.com/4982/as-images.apple.com/is/ipad-air-finish-unselect-gallery-1-202207_FMT_WHH?wid=1280&hei=720&fmt=p-jpg&qlt=95&.v=1654902970705",
                           photo_height=800,
                           photo_width=1000,
                           photo_size=100,
                           is_flexible=False,
                           prices=[
                               LabeledPrice(label="Narxi", amount=15_000_000_00),
                               LabeledPrice(label="QQS", amount=19_200_00),
                               LabeledPrice(label="Skidka", amount=-30_000_00)
                           ],
                           start_parameter='time-machine-example',
                           payload='Ipad air 2023',
                           request_timeout=15
                           )


async def pre_checkout_query_4(pre_checkout_query_4: PreCheckoutQuery, bot: Bot):
    await bot.answer_pre_checkout_query(pre_checkout_query_4.id, ok=True)


async def successful_payment_4(message: types.Message, bot: Bot):
    msg = f"""
    Payment Done ✅ 
    Product name : {message.successful_payment_4.invoice_payload}
    Price: {message.successful_payment_4.total_amount // 100} {message.successful_payment_4.currency} 💸
    Status Done :  ✅ 
    """

    await message.answer(msg)
    await bot.send_message(chat_id=channel, text=msg)

###################################################################################################
