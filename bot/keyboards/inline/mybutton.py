from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
callback = CallbackData('ikb','action')
button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text="🔄PDFga ugirish",callback_data=callback.new(action='finish'))
        ],
        [
            InlineKeyboardButton(text=" ❌bekor qilish",callback_data=callback.new(action='canel'))
        ]
    ]
)