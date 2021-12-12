from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import ctx_data
from tgbot.services.repository import Repo


class IsOperator(BoundFilter):
    key = 'is_operator'

    def __init__(self, is_operator) -> None:
        self.is_operator = is_operator

    async def check(self, message: types.Message) -> bool:
        user_tg_id = message.from_user.id

        data = ctx_data.get()
        repo: Repo = data.get('repo')

        check = await repo.check_user_is_operator(user_tg_id)

        return check == self.is_operator
