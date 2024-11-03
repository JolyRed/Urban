from config import TOKEN
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api_bot = TOKEN
bot = Bot(token=api_bot)
dp = Dispatcher(bot, storage=MemoryStorage())

# Основная клавиатура
kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить')
kb.add(button1).add(button2).add(button3)

# Inline клавиатура для покупок
inline_kb = InlineKeyboardMarkup(row_width=2)
products = ['Product1', 'Product2', 'Product3', 'Product4']
for product in products:
    inline_kb.insert(InlineKeyboardButton(text=product, callback_data='product_buying'))

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def start_work(message: types.Message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью. Для начала рассчёта нажмите на кнопку 'Рассчитать'", reply_markup=kb)

@dp.message_handler(text=['Информация'])
async def show_info(message: types.Message):
    await message.answer('Информация о боте')

@dp.message_handler(text=['Рассчитать'])
async def main_menu(message: types.Message):
    await message.answer("Выберите опцию:", reply_markup=inline_kb)

@dp.message_handler(text=['Купить'])
async def get_buying_list(message: types.Message):
    products_info = [
        "name": "Product1", "description": "Описание продукта 1", "price": 100, "image": "product/молоко.png",
        "name": "Product2", "description": "Описание продукта 2", "price": 200, "image": "product/картошка.png",
        "name": "Product3", "description": "Описание продукта 3", "price": 300, "image": "product/сыр.png",
        "name": "Product4", "description": "Описание продукта 4", "price": 400, "image": "product/сосиски.png",
    ]
  
    for product in products_info:
        await message.answer(f'Название: product["name"] | Описание: product["description"] | Цена: product["price"]')
        await message.answer_photo(open(product["image"], 'rb'))

    await message.answer("Выберите продукт для покупки:", reply_markup=inline_kb)

@dp.callback_query_handler(lambda c: c.data == 'product_buying')
async def send_confirm_message(call: types.CallbackQuery):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
