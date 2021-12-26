from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from tgbot.services.repository import Repo


async def command_start(msg: types.Message, repo: Repo, state: FSMContext):
    await state.finish()

    if await repo.check_user_is_operator(msg.from_user.id) == False:
        await msg.answer(
            text="Приветствую! 🚀\n\nЯ - чат-бот технической поддержки.\n"
            "Ты можешь написать свой вопрос, а я свяжу тебя с свободным оператором."
        )
    else:
        await msg.answer(
            text="Приветствую! 🚀\n\nВы являетесь оператором, ожидайте новых тикетов."
        )


async def command_cancel(msg: types.Message, state: FSMContext):
    await state.finish()
    await msg.reply("Action canceled.")


def register_handlers_common(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=["start"], state="*")
    dp.register_message_handler(command_cancel, commands=["cancel"], state="*")
