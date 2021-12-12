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


def register_handlers_dialog_router(dp: Dispatcher):
    dp.register_message_handler(
        dialog_router, content_types="any", is_dialog=True)
