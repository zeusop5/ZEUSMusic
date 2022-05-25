
from modules.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message



@Client.on_message(
    filters.private & filters.edited
)
async def start_private(client: Client, message: Message):
 await message.reply_photo(
        photo=f"https://te.legra.ph/file/a4c16c60dd1c46bbe7385.jpg",
        caption=f"""**💥 𝐇𝐞𝐥𝐥𝐨, 𝐈 𝐚𝐦 𝐒𝐮𝐩𝐞𝐫𝐟𝐚𝐬𝐭 𝐇𝐢𝐠𝐡 𝐐𝐮𝐚𝐥𝐢𝐭𝐲
𝐍𝐨 𝐋𝐚𝐠 𝐕𝐂 𝐌𝐮𝐬𝐢𝐜 𝐏𝐥𝐚𝐲𝐞𝐫 𝐁𝐨𝐭.**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("⭐ 𝐎𝐰𝐧𝐞𝐫'𝐱𝐃 ✨", url=f"https://t.me/Shailendra34")
                ],
                [
                    InlineKeyboardButton(
                        "💝 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐂𝐡𝐚𝐭 💫", url=f"https://t.me/Yaaro_ki_yaarii"
                    ),
                    InlineKeyboardButton(
                        "🌸 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 ✨", url=f"https://t.me/HeroOfficialBots"
                    ),
                ],
            ]
        ),
    )


