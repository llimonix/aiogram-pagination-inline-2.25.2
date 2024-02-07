# AiogramPaginationInline 2.25.2

## Description

A simple library for aiogram 2.25.2 that allows you to easily do pagination for any Inline keyboards.

Install for pip:

```shell
pip install aiogram2252-page
```

## Create paginations object

```python
from aiogram2252_page.paginator import Paginator
from aiogram import types

kb = types.InlineKeyboardMarkup()
paginator = Paginator(data=kb, size=5)
```

### Params

**data**: Any ready-to-use keyboard InlineKeyboardMarkup or any iterable object with InlineKeyboardButton.

**size**: The number of rows of buttons on one page, excluding the navigation bar.

### Return

A paginator object that, when called, returns a ready-made keyboard with pagination.

## Get data for registrations handler paginator

```python
from aiogram2252_page.paginator import Paginator
from aiogram import types

kb = types.InlineKeyboardMarkup()
paginator = Paginator(data=kb, size=5)


@dp.message_handler()
async def some_func(message: types.Message):
    await message.answer(
        text='Pagination ',
        reply_markup=paginator()
    )
```

### Return paginator_handler()

Data for registrations paginator.

## Example

```python
import random

from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters import CommandStart
from aiogram.utils.executor import Executor

from aiogram2252_page.paginator import Paginator

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

```

## Screenshots

First page:

![image](https://github.com/llimonix/aiogram-pagination-inline-2.15.2/assets/58168234/9ea3ecb7-5541-4025-993a-09e66cd3bc6d)

Second page:

![image](https://github.com/llimonix/aiogram-pagination-inline-2.15.2/assets/58168234/a3b3183d-5fb4-44eb-a439-287789af864b)

Last page:

![image](https://github.com/llimonix/aiogram-pagination-inline-2.15.2/assets/58168234/4eba05a3-0fc3-41bb-b5d8-71d6c9e4fed9)

Clicking on the current page number returns to the first page

![image](https://github.com/llimonix/aiogram-pagination-inline-2.15.2/assets/58168234/a0b32c00-2f31-459e-90ff-ef5548982d48)

*The order of entries is not lost.*

## License MIT
