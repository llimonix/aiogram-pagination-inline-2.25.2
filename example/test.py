import random

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.executor import Executor

from aiogram2152_page.paginator import Paginator

token = ''

storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(CommandStart(), state='*')
async def start(message: types.Message):
    await message.answer('Hello world!')

    '''row_width - this parameter indicates the number of columns in the pagination'''
    kb = types.InlineKeyboardMarkup(row_width=2)


    kb.add(
        *[
            types.InlineKeyboardButton(
                text=str(random.randint(1000000, 10000000)),
                callback_data='pass'
            ) for i in range(100)
        ]
    )
    '''size is a parameter that indicates the number of rows in a column'''
    paginator = Paginator(data=kb, size=5, dp=dp, callback_startswith="page:")
    await message.answer(
        text='Paginator',
        reply_markup=paginator()
    )


if __name__ == '__main__':
    Executor(dp).start_polling()
