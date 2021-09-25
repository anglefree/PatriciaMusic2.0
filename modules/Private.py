from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/cd1c80751b6c75a655b1d.jpg")
    await message.reply_text(
        f"""**Hey, I'm music bot by Aditya 😊🎵

I can play ꬺᶙȿᶖɕ  in your group's voice CHAT Developed by [Aditya](https://t.me/aboutmeaditya)

Add me to your group and play music freely😆!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Oᴡɴᴇʀ", url="https://t.me/aboutmeaditya")
                  ],[
                    InlineKeyboardButton(
                        "🛡 SUPPORT GROUP 🛡", url="https://t.me/quicktrivia"
                    ),
                ],[ 
                    InlineKeyboardButton(
                        "ADD ME TO YOUR GROUP😉", url="https://t.me/v4music_bot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**quick trivia music BOT IS WORKING**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 COMMANDS 📚", url="https://t.me/AXEL_SUPPPORTXD/24")
                ]
            ]
        )
   )


