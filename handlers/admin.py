# === handlers/admin.py ===
from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from db import get_vote_results
from config import ADMIN_IDS

router = Router()

@router.message(Command("natijalar"))
async def show_results(msg: Message):
    if msg.from_user.id not in ADMIN_IDS:
        await msg.answer("Sizga bu buyruqdan foydalanishga ruxsat yo'q.")
        return

    results = get_vote_results()
    if not results:
        await msg.answer("Hozircha hech qanday ovoz mavjud emas.")
        return

    response = "📊 <b>Ovozlar natijasi:</b>\n\n"
    current_subject = None
    for teacher, count in results:
        response += f"👨‍🏫 {teacher}: <b>{count}</b> ta ovoz\n"

    await msg.answer(response)