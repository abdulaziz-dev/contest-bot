# === keyboards/default.py ===
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def contact_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text="Kontaktni yuborish", request_contact=True)
        ]],
        resize_keyboard=True,
        one_time_keyboard=True
    )
