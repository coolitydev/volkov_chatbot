from aiogram import Router
from aiogram.types import Message

from keyboards import nikita_kb, denist_kb, pavel_kb, ivan_kb

message_router = Router()


@message_router.message()
async def message_handler(message: Message) -> None:
    words = message.text.lower().split()
    for word in words:
        if word in ["иван", "полушин", "ваня", "вань"]:
            await message.answer("Позвать Ваню?", reply_markup=ivan_kb)
        elif word in ["павел", "федоров", "паша", "паш"]:
            await message.answer("Позвать Пашу?", reply_markup=pavel_kb)
        elif word in ["денис", "истомин", "ден", "денист", "denist", "den"]:
            await message.answer("Позвать Дениса?", reply_markup=denist_kb)
        elif word in ["никита", "власов", "некит"]:
            await message.answer("Позвать Никиту?", reply_markup=nikita_kb)
        elif word == "@all":
            await message.answer('@zunaaav, @ne_piwite_mne, @istomin14, @qwefurion')



