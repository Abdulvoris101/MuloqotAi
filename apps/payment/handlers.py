from bot import dp, bot, types
from utils import text
from db.state import Payment
from aiogram.dispatcher.dispatcher import FSMContext
from apps.admin.keyboards import cancel_keyboards
import uuid
from .api import Cheque
from .keyboards import check_payment_menu
from aiogram.dispatcher.filters import Text
from .models import Transaction
from utils import send_event, send_error
from apps.core.managers import CreditManager
from apps.imageai.keyboards import buyCreditMenu
import os
import math

AQSHA_COST = int(os.environ.get("AQSHA_COST"))

@dp.callback_query_handler(text="buy_credit")
async def buy_credit(message: types.Message):
    await message.answer("Sotib olish!")
    await bot.send_message(
        message.message.chat.id, 
        f'Xurmatli <b>{message.from_user.full_name}</b>, {text.AQSHA_TEXT}',
        reply_markup=cancel_keyboards
    )

    await Payment.amount_aqsha.set()


@dp.message_handler(commands=["balance"])
async def buy_credit(message: types.Message):
    await bot.send_message(
        message.chat.id, 
        f'Balansingiz - {CreditManager(message.chat.id).get()[0]} aqsha.\n\nAqsha faqatgina rasm generatsiya uchun ishlatilinadi.\nMuloqotAi bilan suxbatlashish mutlaqo bepul',
        reply_markup=buyCreditMenu
    )


@dp.message_handler(state=Payment.amount_aqsha)
async def get_aqsha(message: types.Message, state=FSMContext):
    if not message.text.isdigit() and not isinstance(message.text, int):
        return await message.answer("Iltimos faqatgina butun son kiriting!")
    
    amount = int(message.text)
    price = int(message.text) * AQSHA_COST
    transaction_id = uuid.uuid4()

    async with state.proxy() as data:
        data["transaction_id"] = transaction_id
        data["amount"] = amount
        data["price"] = price

    await message.answer(text.buy_text(amount, price, transaction_id), reply_markup=check_payment_menu)

    await Payment.next()


@dp.message_handler(Text(equals="✅ To'lovni tekshirish"), state=Payment.is_success)
async def check_payment(message: types.Message, state=FSMContext):    
    if state is None:
        return

    async with state.proxy() as data:
        transaction_id = data["transaction_id"]
        amount = data["amount"]


    sent_message = await message.answer("Biroz kuting...")

    cheque = Cheque.get_transaction(transaction_id)
    is_payed = False if cheque == False else True
    
    await bot.delete_message(message.chat.id, sent_message.message_id)

    if is_payed:
        actual_price = math.ceil(float(cheque.amount / 100))
        
        actual_amount = int(actual_price / AQSHA_COST)

        transaction_obj = Transaction(transaction_id, message.from_user.id, amount, is_success=True)
        transaction_obj.save()

        CreditManager(message.from_user.id).increase(actual_amount)

        await send_event(f"""\n#payment\nchatId: {message.from_user.id},\ntransactionId: {transaction_id},\nexpected amount: {amount},\nactual amount: {actual_amount},\nactual price: {actual_price},\nsuccess: {is_payed}""")

        return await message.answer(f"To'lovingiz muvafiqiyatli o'tdi. Sizning xisobingizga {actual_amount} aqsha tushirib berildi. Balans - /balance")


    await message.answer(text.FAILED_PAYMENT_STEP1, reply_markup=types.ReplyKeyboardRemove())
    await Payment.next()


@dp.message_handler(state=Payment.full_name)
async def failed_payment(message: types.Message, state=FSMContext):

    async with state.proxy() as data:
        transaction_id = data["transaction_id"]
        amount = data["amount"]
        price = data["price"]
        
    cardholder = message.text

    await send_error(f"""#payment failed\nchatId: {message.from_user.id},\ntransactionId: {transaction_id},\ncardholder: {cardholder},\namount: {amount},\nprice: {price},\nsuccess: False""")
    
    transaction_obj = Transaction(transaction_id, message.from_user.id, amount, is_success=False, cardholder=cardholder)
    transaction_obj.save()   

    await message.answer(text.FAILED_PAYMENT_STEP2)

    await state.finish()


