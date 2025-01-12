

import random
from datetime import datetime

from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, Message

from config import OWNER_USERNAME
from AarohiX import AarohiX
from AarohiX.database.chats import add_served_chat
from AarohiX.database.users import add_served_user
from AarohiX.modules.helpers import PNG_BTN


#----------------IMG-------------#



# Random Start Images
IMG = [
    "https://graph.org/file/6510afc1c064e53ed2718-3033be560b88a71a0f.jpg",
    "https://graph.org/file/6510afc1c064e53ed2718-3033be560b88a71a0f.jpg",
    "https://graph.org/file/6510afc1c064e53ed2718-3033be560b88a71a0f.jpg",
    "https://graph.org/file/6510afc1c064e53ed2718-3033be560b88a71a0f.jpg",
    "https://graph.org/file/6510afc1c064e53ed2718-3033be560b88a71a0f.jpg",
    "https://graph.org/file/6510afc1c064e53ed2718-3033be560b88a71a0f.jpg",
    "https://graph.org/file/6510afc1c064e53ed2718-3033be560b88a71a0f.jpg",
    "https://graph.org/file/6510afc1c064e53ed2718-3033be560b88a71a0f.jpg",
    "https://graph.org/file/6510afc1c064e53ed2718-3033be560b88a71a0f.jpg",
    "https://graph.org/file/6510afc1c064e53ed2718-3033be560b88a71a0f.jpg",
    "https://graph.org/file/6510afc1c064e53ed2718-3033be560b88a71a0f.jpg",
    "https://graph.org/file/6510afc1c064e53ed2718-3033be560b88a71a0f.jpg",
    "https://graph.org/file/6510afc1c064e53ed2718-3033be560b88a71a0f.jpg",
    "https://graph.org/file/6510afc1c064e53ed2718-3033be560b88a71a0f.jpg",
]


#----------------IMG-------------#

#---------------STICKERS---------------#

# Random Stickers
STICKER = [
    "CAACAgUAAx0CYlaJawABBy4vZaieO6T-Ayg3mD-JP-f0yxJngIkAAv0JAALVS_FWQY7kbQSaI-geBA",
    "CAACAgUAAx0CYlaJawABBy4rZaid77Tf70SV_CfjmbMgdJyVD8sAApwLAALGXCFXmCx8ZC5nlfQeBA",
    "CAACAgUAAx0CYlaJawABBy4jZaidvIXNPYnpAjNnKgzaHmh3cvoAAiwIAAIda2lVNdNI2QABHuVVHgQ",
]

#---------------STICKERS---------------#



@AarohiX.on_cmd("ping")
async def ping(_, message: Message):
    await message.reply_sticker(sticker=random.choice(STICKER))
    start = datetime.now()
    loda = await message.reply_photo(
        photo=random.choice(IMG),
        caption="ᴘɪɴɢɪɴɢ...",
    )
    try:
        await message.delete()
    except:
        pass

    ms = (datetime.now() - start).microseconds / 1000
    await loda.edit_text(
        text=f"нey вαву!!\n{AarohiX.name} ιѕ alιve 🥀 αnd worĸιng ғιne wιтн a pιng oғ\n➥ `{ms}` ms\n\n<b>|| мαdє ωιтн ❣️ ву [king❣️](https://t.me/KingOfHellLuci) ||</b>",
        reply_markup=InlineKeyboardMarkup(PNG_BTN),
    )
    if message.chat.type == ChatType.PRIVATE:
        await add_served_user(message.from_user.id)
    else:
        await add_served_chat(message.chat.id)
