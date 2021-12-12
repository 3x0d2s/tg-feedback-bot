from typing import List
from aiogram import types, Dispatcher
from tgbot.services.repository import Repo


async def dialog_router(msg: types.Message, repo: Repo):
    user_in_dialog_tg_id = msg.from_user.id

    dialog_data = await repo.get_dialog_data(user_in_dialog_tg_id)

    if user_in_dialog_tg_id == dialog_data["operator_tg_id"]:
        operator_data = await repo.get_operator_data(operator_tg_id=user_in_dialog_tg_id)
        operator_name = operator_data["name"]
        #
        if msg.content_type != "text":
            if msg.caption != None:
                text = f"<b>{operator_name}</b>\n\t{msg.caption}"
            else:
                text = f"<b>{operator_name}</b>"

            await msg.copy_to(
                chat_id=dialog_data["client_tg_id"],
                caption=text
            )
        else:
            text = f"<b>{operator_name}</b>\n\t{msg.html_text}"
            await msg.bot.send_message(
                chat_id=dialog_data["client_tg_id"],
                text=text
            )
    #
    elif user_in_dialog_tg_id == dialog_data["client_tg_id"]:
        #
        if msg.content_type != "text":
            if msg.caption != None:
                text = f"<b>{msg.from_user.full_name}</b>\n\t{msg.caption}"
            else:
                text = f"<b>{msg.from_user.full_name}</b>"

            await msg.copy_to(
                chat_id=dialog_data["operator_tg_id"],
                caption=text
            )
        else:
            text = f"<b>{msg.from_user.full_name}</b>\n\t{msg.html_text}"
            await msg.bot.send_message(
                chat_id=dialog_data["operator_tg_id"],
                text=text
            )


async def dialog_router_for_album(msg: types.Message, album: List[types.Message], repo: Repo):
    user_in_dialog_tg_id = msg.from_user.id

    dialog_data = await repo.get_dialog_data(user_in_dialog_tg_id)

    if user_in_dialog_tg_id == dialog_data["operator_tg_id"]:
        operator_data = await repo.get_operator_data(operator_tg_id=user_in_dialog_tg_id)
        operator_name = operator_data["name"]
        #
        try:
            media_group = create_media_group(
                album=album,
                caption_start=f"<b>{operator_name}</b>\n\t"
            )
        except ValueError:
            return await msg.answer("This type of album is not supported by aiogram.")

        await msg.bot.send_media_group(
            chat_id=dialog_data["client_tg_id"],
            media=media_group
        )
    elif user_in_dialog_tg_id == dialog_data["client_tg_id"]:
        #
        try:
            media_group = create_media_group(
                album=album,
                caption_start=f"<b>{msg.from_user.full_name}</b>\n\t"
            )
        except ValueError:
            return await msg.answer("This type of album is not supported by aiogram.")

        await msg.bot.send_media_group(
            chat_id=dialog_data["operator_tg_id"],
            media=media_group
        )


def create_media_group(album: List[types.Message], caption_start: str) -> types.MediaGroup:
    media_group = types.MediaGroup()
    for i, obj in enumerate(album):
        if obj.photo:
            file_id = obj.photo[-1].file_id
        else:
            file_id = obj[obj.content_type].file_id

        if obj.caption == None:
            if i == 0:
                media_group.attach(
                    {
                        "media": file_id,
                        "type": obj.content_type,
                        "caption": caption_start
                    }
                )
            else:
                media_group.attach(
                    {
                        "media": file_id,
                        "type": obj.content_type
                    }
                )
        else:
            if i == 0:
                media_group.attach(
                    {
                        "media": file_id,
                        "type": obj.content_type,
                        "caption": caption_start + obj.caption
                    }
                )
            else:
                media_group.attach(
                    {
                        "media": file_id,
                        "type": obj.content_type,
                        "caption": obj.caption
                    }
                )
    return media_group


def register_handlers_dialog_router(dp: Dispatcher):
    dp.register_message_handler(
        dialog_router_for_album, content_types="any", is_media_group=True, is_dialog=True)
    dp.register_message_handler(
        dialog_router, content_types="any", is_dialog=True)
