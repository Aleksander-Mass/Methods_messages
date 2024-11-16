from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = "Согласно примечания в задании, ключ управления ботом убран"
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(text=['Vika', 'ff'])
async def vika_message(message: types.Message):
    await message.answer("Vika message!")

@dp.message_handler(commands=['start'])
async def start_message(message: types.Message):
    # Вместо печати в консоль отправляем сообщение пользователю
    await message.answer("Привет! Я бот, помогающий твоему здоровью.")

@dp.message_handler()
async def all_message(message: types.Message):
    # Вместо печати в консоль отправляем сообщение пользователю
    await message.answer("Введите команду /start, чтобы начать общение.")

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)

###    Вывод в чате телеграмм канала, после запуска программы:
"""
Alex, [15.11.2024 12:40]
Привет

Vika, [15.11.2024 12:40]
Введите команду /start, чтобы начать общение.

Alex, [15.11.2024 12:40]
/start

Vika, [15.11.2024 12:40]
Привет! Я бот, помогающий твоему здоровью.
"""