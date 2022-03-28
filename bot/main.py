"""
The basis for working with a telegram.
Commands are registered to which the bot will respond.

DO NOT USE FOR BASIC LOGIC.
"""
import logging
from asyncio import get_event_loop

from aiogram import executor
from aiogram.types import Message
from asyncpgsa import pg

from configs import DataBaseConfig
from misc import dp
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)


@dp.message_handler()
async def echo(message: Message) -> None:
    """
    :param message: Telegram message
    """
    await message.answer(message.text)


async def init_connection():
    db_config = DataBaseConfig()
    await pg.init(
        host=db_config.host,
        port=db_config.port,
        database=db_config.name,
        user=db_config.user,
        password=db_config.password.get_secret_value(),
        min_size=5,
        max_size=10
    )


@dp.message_handler(lambda message: types.Message)
async def show_items(message: types.Message):
    await message.answer(text="Есть?", reply_markup=choice)


@dp.callback_query_handler(yes_no_choice_callback.filter(item="Yes"))
async def choice_yes(call: CallbackQuery):
    # Пользователя устроил ответ => ДА заносится в бд
    #user_id = message.from_user.id
    #get_or_create(feedback, user_id, Yes)
    pass
    await call.message.answer("Отлично")


@dp.callback_query_handler(yes_no_choice_callback.filter(item="No"))
async def choice_no(call: CallbackQuery):
    # Пользователя не устроил ответ => НЕТ заносится в бд
    # user_id = message.from_user.id
    # get_or_create(feedback, user_id, No)
    pass
    await call.message.answer("Жаль")


if __name__ == '__main__':
    event_loop = get_event_loop()
    event_loop.run_until_complete(init_connection())
    executor.start_polling(dp, loop=event_loop, skip_updates=True)
