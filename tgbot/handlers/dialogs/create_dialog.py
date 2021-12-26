from aiogram import types, Dispatcher
from tgbot.services.repository import Repo


async def create_dialog(call: types.CallbackQuery, repo: Repo):
    client_tg_id = int(call.data[len("create_dialog_with_"):])
    operator_tg_id = call.from_user.id
    await repo.add_dialog(operator_tg_id, client_tg_id)
    await call.message.edit_text(
        text=call.message.html_text +
        "\n\nВы создали диалог с автором этого тикета.\nПомогите ему!"
    )

    operator_data = await repo.get_operator_data(operator_tg_id=operator_tg_id)
    operator_name = operator_data["name"]
    await call.bot.send_message(
        chat_id=client_tg_id,
        text=f"🚀 Оператор <b>{operator_name}</b> взялся за ваш тикет.\nОжидайте ответа..."
    )

    await repo.close_ticket(client_tg_id)
    await call.answer()


def register_handlers_create_dialog(dp: Dispatcher):
    dp.register_callback_query_handler(
        create_dialog, text_startswith="create_dialog_with_")
