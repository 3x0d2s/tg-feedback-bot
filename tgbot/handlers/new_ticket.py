from asyncio import sleep
from datetime import datetime
from aiogram import types, Dispatcher
from tgbot.services.repository import Repo


async def new_ticket(msg: types.Message, repo: Repo):
    #
    if len(f"<b>{msg.from_user.full_name}:</b>\n\t{msg.html_text}") <= 4096:
        text = f"<b>{msg.from_user.full_name}:</b>\n\t{msg.html_text}"
    else:
        await msg.answer("Слишком большое сообщение! Попытайтесь, пожалуйста, описать свою проблему короче.")
        return

    # Добавление тикета в БД
    client_tg_id = msg.from_user.id
    msg_id = msg.message_id
    datetime_msg = datetime.now()
    await repo.add_ticket(client_tg_id, msg_id, datetime_msg)

    # Рассылка тикета свободным операторам
    freedom_operators = await repo.list_freedom_operators()
    #
    keyboard = types.InlineKeyboardMarkup()
    take_ticket_btn = types.InlineKeyboardButton(
        text="Взять тикет",
        callback_data=f"create_dialog_with_{client_tg_id}"
    )
    keyboard.add(take_ticket_btn)
    #
    for operator_id in freedom_operators:
        await msg.bot.send_message(
            chat_id=operator_id,
            text=text,
            reply_markup=keyboard
        )
        await sleep(0.1)


def register_handlers_new_ticket(dp: Dispatcher):
    dp.register_message_handler(new_ticket, is_operator=False)
