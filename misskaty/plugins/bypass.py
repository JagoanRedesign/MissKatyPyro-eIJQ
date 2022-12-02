"""
 * @author        yasir <yasiramunandar@gmail.com>
 * @date          2022-12-01 09:12:27
 * @lastModified  2022-12-01 09:32:31
 * @projectName   MissKatyPyro
 * Copyright @YasirPedia All rights reserved
"""
import re
from misskaty.helper.http import http
from misskaty import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import MessageTooLong, EntitiesTooLong
from misskaty.vars import COMMAND_HANDLER
from misskaty.helper.tools import rentry
from urllib.parse import unquote
from misskaty.core.decorator.errors import capture_err
from misskaty.helper.human_read import get_readable_file_size

LIST_LINK = """
- Pling and all aliases.
- Other link soon...
"""

__MODULE__ = "Bypass"
__HELP__ = f"""
/directurl [Link] - Bypass URL.

Supported Link:
{LIST_LINK}
"""


async def pling_bypass(url):
    try:
        id_url = re.search(r"https?://(store.kde.org|www.pling.com)\/p\/(\d+)", url)[2]
        link = f"https://www.pling.com/p/{id_url}/loadFiles"
        res = await http.get(link)
        json_dic_files = res.json().pop("files")
        msg = f"\n**Source Link** :\n`{url}`\n**Direct Link :**\n"
        msg += "\n".join(
            f'**→ [{i["name"]}]({unquote(i["url"])}) ({get_readable_file_size(int(i["size"]))})**'
            for i in json_dic_files
        )
        return msg
    except Exception as e:
        return e


@app.on_message(filters.command(["directurl"], COMMAND_HANDLER))
@capture_err
async def bypass(_, message):
    if len(message.command) == 1:
        return await message.reply(
            f"Gunakan perintah /{message.command[0]} untuk bypass url"
        )
    url = message.command[1]
    msg = await message.reply("Bypassing URL..", quote=True)
    mention = f"**Bypasser:** {message.from_user.mention} ({message.from_user.id})"
    if re.match(r"https?://(store.kde.org|www.pling.com)\/p\/(\d+)", url):
        data = await pling_bypass(url)
        try:
            await msg.edit(f"{data}\n\n{mention}")
        except (MessageTooLong, EntitiesTooLong):
            result = await rentry(data)
            markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Open Link", url=result),
                        InlineKeyboardButton("Raw Link", url=f"{result}/raw"),
                    ]
                ]
            )
            await msg.edit(
                f"{result}\n\nBecause your bypassed url is too long, so your link will be pasted to rentry.\n{mention}",
                reply_markup=markup,
                disable_web_page_preview=True,
            )
    else:
        await msg.edit("Unsupported link..")