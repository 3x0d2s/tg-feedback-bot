from aiogram import types, Dispatcher
from tgbot.services.repository import Repo


async def close_dialog(msg: types.Message, repo: Repo):
    operator_tg_id = msg.from_user.id
    dialog_data = await repo.get_dialog_data(operator_tg_id)
    await repo.close_dialog(operator_tg_id)

    await msg.answer("✅ Диалог успешно закрыт!")

    await msg.bot.send_message(
        chat_id=dialog_data["client_tg_id"],
        text="Оператор закончил диалог."
    )


def register_handlers_close_dialog(dp: Dispatcher):
    dp.register_message_handler(
        close_dialog,
        commands=["disconnect"],
        is_dialog=True,
        is_operator=True
    )
