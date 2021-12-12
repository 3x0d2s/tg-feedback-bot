from aiogram import types, Dispatcher
from tgbot.data.config import OPERATORS_CHAT_ID


async def set_default_commands(dp: Dispatcher):
    """Устанавливает команды для бота."""

    # Для всеx
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
        ],
        scope=types.BotCommandScopeDefault()
    )

    # Для участников чата опреаторов
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", "Запустить бота"),
            types.BotCommand("help", "Вывести справку"),
            types.BotCommand("addoperator", "Добавить оператора"),
            types.BotCommand("disconnect", "Завершить диалог с клиентом"),
        ],
        scope=types.BotCommandScopeChat(chat_id=OPERATORS_CHAT_ID)
    )
