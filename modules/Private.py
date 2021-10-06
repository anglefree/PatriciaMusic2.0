from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_photo("https://telegra.ph/file/5993e1a643d3986a27d9e.jpg")
    await message.reply_text(
        f"""**Hey, I'm AXEL 😊🎵

I can play ꬺᶙȿᶖɕ  in your group's voice CHAT Developed by [Axel](https://t.me/suraj_o_p)

Add me to your group and play music freely😆!**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Oᴡɴᴇʀ", url="https://t.me/suraj_o_p")
                  ],[
                    InlineKeyboardButton(
                        "🛡 SUPPORT GROUP 🛡", url="https://t.me/AXEL_SUPPORT"
                    ),
                ],[ 
                    InlineKeyboardButton(
                        "ADD ME TO YOUR GROUP😉", url="https://t.me/AXEL_MUSICBOT?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**AXELMUSIC BOT IS WORKING**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📚 COMMANDS 📚", url="https://t.me/AXEL_SUPPPORTXD/24")
                ]
            ]
        )
   )


