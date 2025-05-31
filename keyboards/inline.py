# === keyboards/inline.py ===
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db import get_subjects, get_teachers_by_subject

def subject_keyboard():
    builder = InlineKeyboardBuilder()
    for sub_id, name in get_subjects():
        builder.button(text=name, callback_data=f"subject_{sub_id}")
    builder.adjust(2)
    return builder.as_markup()

def teacher_keyboard(subject_id):
    builder = InlineKeyboardBuilder()
    for t_id, name in get_teachers_by_subject(subject_id):
        builder.button(text=name, callback_data=f"teacher_{t_id}")
    builder.button(text="⬅️ Orqaga", callback_data="back")
    builder.adjust(2)
    return builder.as_markup()