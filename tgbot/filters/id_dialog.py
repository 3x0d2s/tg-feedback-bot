from aiogram import types
from aiogram.dispatcher.filters import BoundFilter
from aiogram.dispatcher.handler import ctx_data
from tgbot.services.repository import Repo


class IsDialog(BoundFilter):
    key = 'is_dialog'

    def __init__(self, is_dialog) -> None:
        self.is_dialog = is_dialog

    async def check(self, message: types.Message) -> bool:
        user_tg_id = message.from_user.id

        data = ctx_data.get()
        repo: Repo = data.get('repo')

        check = await repo.check_user_in_dialog(user_tg_id)

        return check == self.is_dialog
