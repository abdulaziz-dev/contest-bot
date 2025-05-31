from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types import Message, CallbackQuery

from config import CHANNEL_USERNAME, CONTACT_GROUP_ID, INSTAGRAM_URL, \
    TELEGRAM_CHANNEL_URL
from db import add_vote, has_shared_contact, mark_contact_shared
from keyboards.default import contact_keyboard
from keyboards.inline import subject_keyboard, teacher_keyboard

router = Router()

@router.message(CommandStart())
async def start_handler(msg: Message, state: FSMContext):
    user_id = msg.from_user.id
    member = await msg.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)

    if member.status not in ["member", "creator", "administrator"]:
        subscribe_markup = InlineKeyboardMarkup(inline_keyboard=[
            [InlineKeyboardButton(text="📸 Instagram",
                                  url=INSTAGRAM_URL)],
            [InlineKeyboardButton(text="📢 Telegram",
                                  url=TELEGRAM_CHANNEL_URL)],
        ])
        await msg.answer(
            "Botdan foydalanish uchun quyidagi kanallarga obuna bo'ling:",
            reply_markup=subscribe_markup
        )
        return

    if not has_shared_contact(user_id):
        await msg.answer("Iltimos, kontakt ma'lumotingizni yuboring:", reply_markup=contact_keyboard())
        return

    await msg.answer("Fanlardan birini tanlang:", reply_markup=subject_keyboard())

@router.message(F.contact)
async def contact_handler(msg: Message):
    user_id = msg.from_user.id
    if not has_shared_contact(user_id):
        mark_contact_shared(user_id)
        group_id = CONTACT_GROUP_ID  # replace with your group chat id
        await msg.bot.send_message(chat_id=group_id, text=f"📱 Yangi kontakt: {msg.contact.phone_number} ({msg.from_user.full_name})")

    await msg.answer("Fanlardan birini tanlang:", reply_markup=subject_keyboard())

@router.callback_query(F.data.startswith("subject_"))
async def subject_callback(call: CallbackQuery, state: FSMContext):
    subject_id = int(call.data.split("_")[1])
    # await state.update_data(subject_id=subject_id)
    await call.message.edit_text("Ustozni tanlang:", reply_markup=teacher_keyboard(subject_id))

@router.callback_query(F.data.startswith("teacher_"))
async def teacher_callback(call: CallbackQuery, state: FSMContext):
    teacher_id = int(call.data.split("_")[1])
    user_id = call.from_user.id
    if add_vote(user_id, teacher_id):
        await call.message.edit_text("✅ Ovoz berildi. Rahmat!")
    else:
        await call.message.edit_text("Siz allaqachon ovoz bergansiz.")

@router.callback_query(F.data == "back")
async def back_callback(call: CallbackQuery):
    await call.message.edit_text("Fanlardan birini tanlang:", reply_markup=subject_keyboard())