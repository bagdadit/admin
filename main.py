from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message
from aiogram.types.reply_keyboard import ReplyKeyboardMarkup, KeyboardButton


api = '7072077495:AAGH0gPXa_QdnyZhFbTXF0dOMNk57Cfr8ro'

knopka = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="O‘zbek")]
    ],
    resize_keyboard=True
)
knopka1 = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="Inspektorning harakatlari/harakatsizligi to‘g‘risidagi shikoyat")],
        [KeyboardButton(text='Murojaat holatini tekshirish')],
        [KeyboardButton(text='Mening murojaatlarim')],
        [KeyboardButton(text='Murojaat jo‘natish')],
        [KeyboardButton(text='❌Bekor qilish')]
    ],
    resize_keyboard=True
)
inspektr = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='🏛 Bosh Menyu')]
    ],
    resize_keyboard=True
)
murojat = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='🏛 Bosh Menyu')]
    ],
    resize_keyboard=True
)
meningmurojatim = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text='🏛 Bosh Menyu')],
        [KeyboardButton(text='Sizda arizalar mavjudmas')]
    ],
    resize_keyboard=True
)
murojatjonatish = ReplyKeyboardMarkup(
    [
        [KeyboardButton(text="F.I.SH")],
        [KeyboardButton(text="🏛 Bosh Menyu")]
    ],
    resize_keyboard=True
)


bot = Bot(api)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(messaeg: Message):
    chatid = messaeg.chat.id
    await bot.send_message(chat_id=chatid, text='Assalomu Alaykum Iltimos tilni tanlang!', reply_markup=knopka)

@dp.message_handler(text='O‘zbek')
async def orqagwa(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🏛 Bosh Menyu', reply_markup=knopka1)


@dp.message_handler(text='Inspektorning harakatlari/harakatsizligi to‘g‘risidagi shikoyat')
async def orqagqa(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Iltimos ariza raqamini kiriting', reply_markup=inspektr)


@dp.message_handler(text='Murojaat holatini tekshirish')
async def orqagea(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Iltimos ariza raqamini kiriting', reply_markup=murojat)

@dp.message_handler(text='Mening murojaatlarim')
async def orqarga(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Iltimos ariza raqamini tanlang', reply_markup=meningmurojatim)

@dp.message_handler(text='Murojaat jo‘natish')
async def orqatga(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Iltimos, to‘liq F.I.Sh.ni kiriting.', reply_markup=murojatjonatish)

@dp.message_handler(text='🏛 Bosh Menyu')
async def orqatga(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='🏛 Bosh Menyu', reply_markup=knopka1)

@dp.message_handler(text='❌Bekor qilish')
async def orqaga(message: Message):
    chatid = message.chat.id
    await bot.send_message(chat_id=chatid, text='Assalomu Alaykum Iltimos tilni tanlang!', reply_markup=knopka)

executor.start_polling(dp, skip_updates=True)