# === keyboards/inline.py ===
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from db import get_subjects, get_teachers_by_subject

TEACHERS_PER_PAGE = 7

def subject_keyboard():
    builder = InlineKeyboardBuilder()
    for sub_id, name in get_subjects():
        builder.button(text=name, callback_data=f"subject_{sub_id}")
    builder.adjust(2)
    return builder.as_markup()

def teacher_keyboard(subject_id, page=0):
    all_teachers = get_teachers_by_subject(subject_id)
    builder = InlineKeyboardBuilder()

    start = page * TEACHERS_PER_PAGE
    end = start + TEACHERS_PER_PAGE
    teachers = all_teachers[start:end]

    for t_id, name in teachers:
        builder.button(text=name, callback_data=f"teacher_{t_id}")

    builder.adjust(1)  # ⬅️ This makes buttons appear vertically

    navigation_buttons = []
    if page > 0:
        navigation_buttons.append(InlineKeyboardButton(text="⬅️ Oldingi", callback_data=f"page_{subject_id}_{page - 1}"))
    if end < len(all_teachers):
        navigation_buttons.append(InlineKeyboardButton(text="➡️ Keyingi", callback_data=f"page_{subject_id}_{page + 1}"))

    if navigation_buttons:
        builder.row(*navigation_buttons)

    builder.button(text="⬅️ Orqaga", callback_data="back")
    return builder.as_markup()

def results_navigation_keyboard(page: int):
    buttons = []
    if page > 0:
        buttons.append(InlineKeyboardButton(text="⬅️ Oldingi", callback_data=f"respage_{page - 1}"))
    buttons.append(InlineKeyboardButton(text="➡️ Keyingi", callback_data=f"respage_{page + 1}"))
    return InlineKeyboardMarkup(inline_keyboard=[buttons])