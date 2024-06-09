from aiogram import Router, F
from aiogram.types import CallbackQuery

callback_router = Router()


@callback_router.callback_query(F.data.startswith('call'))
async def call_handler(call: CallbackQuery) -> None:
    name = call.data[5:]
    match name:
        case "ivan":
            await call.message.answer("@Zunaaav")
        case "denist":
            await call.message.answer("@istomin14")
        case "pavel":
            await call.message.answer("@qwefurion")
        case "nikita":
            await call.message.answer("@ne_piwite_mne")
    await call.message.delete()


@callback_router.callback_query(F.data == "reject")
async def reject_handler(call: CallbackQuery) -> None:
    await call.message.delete()
