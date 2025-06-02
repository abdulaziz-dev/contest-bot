from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from config import ADMIN_IDS
from db import get_vote_results
from keyboards.inline import results_navigation_keyboard

router = Router()

RESULTS_PER_PAGE = 10

def format_results(results, page: int):
    if not results:
        return "Hali ovozlar yo'q."

    start_number = page * RESULTS_PER_PAGE + 1
    text = "📊 <b>Ovozlar natijasi:</b>\n\n"
    for idx, (teacher, count) in enumerate(results, start=start_number):
        text += f"👨‍🏫{idx}. {teacher}: {count} ta ovoz\n"
    return text

@router.message(Command("natijalar"))
async def results_command(msg: Message):
    if msg.from_user.id not in ADMIN_IDS:
        return
    page = 0
    offset = page * RESULTS_PER_PAGE
    results = get_vote_results(offset=offset, limit=RESULTS_PER_PAGE)
    await msg.answer(
        format_results(results, page),
        reply_markup=results_navigation_keyboard(page)
    )

@router.callback_query(F.data.startswith("respage_"))
async def results_pagination(call: CallbackQuery):
    if call.from_user.id not in ADMIN_IDS:
        return
    page = int(call.data.split("_")[1])
    offset = page * RESULTS_PER_PAGE
    results = get_vote_results(offset=offset, limit=RESULTS_PER_PAGE)
    await call.message.edit_text(
        format_results(results, page),
        reply_markup=results_navigation_keyboard(page)
    )
