from pyrogram import filters, enums
from pyrogram.errors import UserIsBlocked, UserNotParticipant
from misskaty.vars import COMMAND_HANDLER
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from misskaty.core.decorator.errors import capture_err
from misskaty import app


@app.on_message(filters.command(["copy"], COMMAND_HANDLER))
async def copy(client, message):
    if len(message.command) == 1:
        if not message.reply_to_message:
            return await message.reply("Silahkan balas pesan yang mau dicopy.")
        try:
            await message.reply_to_message.copy(
                message.from_user.id,
                caption_entities=message.reply_to_message.entities,
                reply_markup=message.reply_to_message.reply_markup,
            )
            return await message.reply_text("Pesan berhasil dikirim..")
        except UserIsBlocked:
            return await message.reply(
                "Silahkan PM Saya untuk mengcopy pesan ke chat pribadi..",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="💬 Chat Aku Yahh", url="https://t.me/MissKatyRoBot"
                            )
                        ]
                    ]
                ),
            )
        except Exception as e:
            return await message.reply(f"ERROR: {str(e)}")
    elif message.reply_to_message:
        try:
            idtujuan = message.command[1]
            userstat = await app.get_chat_member(-1001686184174, message.from_user.id)
            if (
                userstat.status
                not in [
                    enums.ChatMemberStatus.ADMINISTRATOR,
                    enums.ChatMemberStatus.OWNER,
                ]
                and message.from_user.id != 2024984460
            ):
                return await message.reply_text("🦉🦉🦉")
            await message.reply_to_message.copy(
                idtujuan,
                caption_entities=message.reply_to_message.entities,
                reply_markup=message.reply_to_message.reply_markup,
            )
            return await message.reply_text("Pesan berhasil dikirim..")
        except UserNotParticipant:
            return await message.reply("Command ini hanya untuk admin YMoviezNew")
        except Exception as e:
            return await message.reply(f"ERROR: {e}")
    else:
        await message.reply("Silahkan balas pesan yang mau dicopy.")


@app.on_message(filters.command(["forward"], COMMAND_HANDLER))
@capture_err
async def forward(client, message):
    if len(message.command) == 1:
        if not message.reply_to_message:
            return await message.reply("Silahkan balas pesan yang mau dicopy.")
        try:
            await message.reply_to_message.forward(message.from_user.id)
            return await message.reply_text("Pesan berhasil dikirim..")
        except UserIsBlocked:
            return await message.reply(
                "Silahkan PM Saya untuk memforward pesan ke chat pribadi..",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton(
                                text="💬 Chat Aku Yahh", url="https://t.me/MissKatyRoBot"
                            )
                        ]
                    ]
                ),
            )
        except Exception as e:
            return await message.reply(f"ERROR: {str(e)}")
    elif message.reply_to_message:
        try:
            idtujuan = message.command[1]
            userstat = await app.get_chat_member(-1001686184174, message.from_user.id)
            if (
                userstat.status
                not in [
                    enums.ChatMemberStatus.ADMINISTRATOR,
                    enums.ChatMemberStatus.OWNER,
                ]
                and message.from_user.id != 2024984460
            ):
                return await message.reply_text("🦉🦉🦉")
            await message.reply_to_message.forward(idtujuan)
            return await message.reply_text("Pesan berhasil dikirim..")
        except UserNotParticipant:
            return await message.reply("Comman ini hanya untuk admin YMoviezNew")
        except Exception as e:
            return await message.reply(f"ERROR: {e}")
    else:
        await message.reply("Silahkan balas pesan yang mau diforward.")
