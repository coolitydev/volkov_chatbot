from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

nikita_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅", callback_data="call_nikita"),
            InlineKeyboardButton(text="❌", callback_data="reject"),
        ],
    ]
)

denist_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅", callback_data="call_denist"),
            InlineKeyboardButton(text="❌", callback_data="reject"),
        ],
    ]
)

pavel_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅", callback_data="call_pavel"),
            InlineKeyboardButton(text="❌", callback_data="reject"),
        ],
    ]
)

ivan_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="✅", callback_data="call_ivan"),
            InlineKeyboardButton(text="❌", callback_data="reject"),
        ],
    ]
)
