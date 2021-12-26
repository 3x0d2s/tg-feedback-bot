from asyncio import sleep
from aiogram import types, Dispatcher
from tgbot.services.repository import Repo


async def close_dialog(msg: types.Message, repo: Repo):
    operator_tg_id = msg.from_user.id
    dialog_data = await repo.get_dialog_data(operator_tg_id)
    await repo.close_dialog(operator_tg_id)

    await msg.answer("✅ Диалог успешно закрыт!")

    await msg.bot.send_message(
        chat_id=dialog_data["client_tg_id"],
        text="🔹 Оператор закончил диалог."
    )

    await msg.bot.send_message(
        chat_id=operator_tg_id,
        text="🔹 Неотвеченные тикеты:"
    )
    tickets = await repo.list_tickets()
    for ticket in tickets:
        client_tg_id = ticket["client_tg_id"]

        keyboard = types.InlineKeyboardMarkup()
        take_ticket_btn = types.InlineKeyboardButton(
            text="Взять тикет",
            callback_data=f"create_dialog_with_{client_tg_id}"
        )
        keyboard.add(take_ticket_btn)

        await msg.bot.send_message(
            chat_id=operator_tg_id,
            text=ticket["ticket_text"],
            reply_markup=keyboard
        )
        await sleep(0.5)


def register_handlers_close_dialog(dp: Dispatcher):
    dp.register_message_handler(
        close_dialog,
        commands=["disconnect"],
        is_dialog=True,
        is_operator=True
    )
